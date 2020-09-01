import requests
from bs4 import BeautifulSoup
from amazon.data_preparation import header, cookie
from tfuc.logger import Logger
import time
import threading

lock = threading.Lock()

lg = Logger()


def get_review_num(url):
    resp = requests.get(url=url, headers=header, cookies=cookie, timeout=5)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'html.parser')
    num_str = soup.find("div", id="filter-info-section").span.text
    return num_str


def get_review_data(asin, conn, url):
    resp = requests.get(url=url, headers=header, cookies=cookie, timeout=5)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find_all("div", class_="a-section review aok-relative")

    for review in reviews:
        lg.info("===================================================")
        review_id = review.get("id")
        cons_id = review.find("a", class_="a-profile").get("href").split("account.")[1].split("/")[0]
        cons_name = review.find("span", class_="a-profile-name").text
        star = float(review.find("span", class_="a-icon-alt").text.split(" ")[0])
        date = review.find("span", class_="a-size-base a-color-secondary review-date").text
        txt = review.find("span", class_="a-size-base review-text review-text-content").span.text

        values = (review_id, cons_id, cons_name, asin, star, date, txt)
        cur = conn.cursor()

        lock.acquire()
        try:
            # if not cur.execute("SELECT review_id FROM Reviews WHERE review_id == ?", (review_id,)):
            #     lg.warning("INSERT")
            cur.execute(
            "INSERT INTO Reviews (review_id, consumer_id, consumer_name, asin, star, date, review) VALUES (?, ?, ?, ?, ?, ?, ?)",
            values)
            conn.commit()
        except:
            lg.error("Repeat insert")

        lg.info("ReviewID :{}".format(review_id))
        lg.info("Cus ID:{}".format(cons_id))
        lg.info("Cus Name:{}".format(cons_name))
        lg.info("ASIN :{}".format(asin))
        lg.info("Star:{}".format(star))
        lg.info("Date:{}".format(date))
        lg.info("Txt:{}".format(txt))
        lock.release()
