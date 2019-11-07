# Pi4 Raspbian中文字库及输入法设置

## 常规安装软件格式 

```shell
sudo apt-get install xxxxxx
```


## 软件源更改

```shell
sudo cp /etc/apt/sources.list  /etc/apt/sources.list_backup 

sudo nano /etc/apt/sources.list 

把官方网址改成国内源的网址，例如：
http://mirrors.aliyun.com/raspbian/raspbian/

sudo apt-get update
```

  

## 安装中文输入法
```shell
sudo apt-get install fcitx fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-sunpinyin 
```


## 设置中文输入法

* 设置模糊音

## 百度进行测试

google浏览器访问[baidu音乐](mp3.baidu.com)进行测试