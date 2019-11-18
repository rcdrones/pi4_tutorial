# UPS github代码库下载和运行

## 下载

```
git clone https://github.com/rcdrones/UPSPACK_V2.git

```

下载大约消耗5分钟。


## 目录介绍

* GUI_py 是用tkinter编写的UPS图形上位机程序
* Email_warning 是python3编写的，监听外部断电，Pi4自动发送Email到指定邮箱的程序。
* console_py 是python3编写的终端解析程序。能解析是否外部断电，剩余电量百分比等
* single_io_warning 用这个程序可以不用使用Pi4的串口，而只使用一个IO口来监听UPS的断电消息。
* cPlusPlus 是国外玩家，补充的C++版本的应用程序
* time_count 是一个记录UPS最大续航运行时间的程序。




## 运行

```
cd UPSPACK_V2/

cd GUI_py/

python3 UPS_GUI_demo.py
```
