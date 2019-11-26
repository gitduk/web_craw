# mycode

## getwallpaper.py

特点：

1，多线程爬取 [ZOL桌面壁纸](http://desk.zol.com.cn/ "wallpaper") 上的壁纸,并自动归档。

2，可自选爬取壁纸的种类，页数(线程)

说明：
URL中的[type]字段为爬取壁纸的种类，具体可为：

【
风景、动漫、美女、创意、卡通、汽车、游戏、可爱、
明星、建筑、植物、动物、静物、影视、车模、体育、
模特、手抄报、美食、星座、节日、品牌、背景、其他
】
的中文拼音。
+ fengjing,
+ dongman,
+ meinv,
+ chuangyi,
+ katong,
+ qiche,
+ youxi,
+ keai,
+ mingxing,
+ jianzhu,
+ zhiwu,
+ dongwu,
+ jingwu,
+ yingshi,
+ chemo,
+ tiyu,
+ model,
+ shouchaobao,
+ meishi,
+ xingzuo,
+ jieri,
+ pinpai,
+ beijing,
+ qita

[num] 字段为程序运行时需输入的整数变量，代表下载页数，也代表着线程数（每页用一个线程下载）


爬取页面展示：

输入分类、下载页数
![1](https://github.com/gitduk/mycode/blob/master/screenshots/show1.png)

开始下载
![2](https://github.com/gitduk/mycode/blob/master/screenshots/show2.png)

爬取结果展示:
![3](https://github.com/gitduk/mycode/blob/master/screenshots/show3.png)
