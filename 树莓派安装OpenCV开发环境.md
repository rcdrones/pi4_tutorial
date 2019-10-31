# 树莓派安装OpenCV开发环境

# 简述

OpenCV是一种开源的计算机图形视觉库。简单的说，就是程序员用这个库可以在二次开发一些关于摄像头的应用。摄像头就是计算机的眼睛对吧？ OpenCV就是大脑采集到眼睛的数据，进行后端处理的一段小程序。典型的应用，例如：颜色识别、人脸检测、人脸识别、二维码解密、车牌号识别……

问：OpenCV在树莓派上怎么用？？

答：配合Python，这种胶水语言。把OpenCV库加载到Python里面，然后在库的基础上做二次开发。That’s all! 

问：如何搭建OpenCV的Python开发环境？

答:分为Python2 和 Python3。2条支线。由于Python2和Python3差异很大，所以我们下面就开干吧！



问：UP主你用的系统是什么？？

答：Pi4 刷上全新的2019-09-26-raspbian-buster-full.zip 



## 前期准备

1. apt源地址的更改
2. 配置好你的Pi4 Wifi，或者用有线网络！确保能上网。
3. 不要用ssh。直接把Pi4接到显示器上，在进行安装。由于安装时间较长，SSH可能有假死，导致你无法知道安装进度的情况！
4. 更改pip源地址
5. 配置好输入法、时区、键盘型号。
6. 想到了在补充。
7. 原则上就是把你的Pi4搞成能舒舒服服用的状态就对了，后面还有很多坑，等你跳。做完了这些准备。让我们一起跳坑吧！！哈哈哈哈！



## Python2 上的OpenCV库

* 安装
```
sudo apt-get install libopencv-dev sudo

apt-get install python-opencv 
```


* 测试
```
import cv2 

cv2.__version__
```

>  为啥叫cv2而不叫opencv呢？这是因为OpenCV是基于C/C++开发的，有两个版本，’‘cv”版本的API是C语言开发的，’‘cv2’'版本的API是基于C++语言开发的，为了保持向后兼容性所以叫"cv2"，但我们都知道cv2就是OpenCV本尊。 


* 应用

```
git clone https://github.com/TommyZihao/opencvtest.git
cd opencvtest
python2 testopencv.py
```

  



## Python3 上的OpenCV库



