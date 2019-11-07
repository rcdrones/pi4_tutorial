# 树莓派4 无显示器和键盘，该怎么玩？（关于激活WIFI、使能SSH、搭建VNC的教程）

## 前期准备

Pi4 TF卡刷入最新的官方系统，我用的是：`2019-09-26-raspbian-buster-full.zip`

## 激活WIFI

在windows电脑上，进去boot分区，建一个 `wpa_supplicant.conf` 文件，文件的内容如下

```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
 
 
network={
ssid="WiFi-B"		#ssid:网络的ssid
psk="12345678"		#psk:密码
key_mgmt=WPA-PSK	# WiFi 使用WPA/WPA2加密
priority=1			#priority:连接优先级，数字越大优先级越高（不可以是负数）
scan_ssid=0   		#scan_ssid:连接隐藏WiFi时需要指定该值为1
}
```



扩展阅读：

```
#如果你的 WiFi 没有密码
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=NONE
}

#如果你的 WiFi 使用WEP加密
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=NONE
wep_key0="你的wifi密码"
}

#如果你的 WiFi 使用WPA/WPA2加密
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=WPA-PSK
psk="你的wifi密码"
}
```





## 使能SSH

SSH，可以简单的理解为Linux的远程命令行工具。在windows电脑上，进去boot分区。建立一个名字为ssh的空白文件即可。*注意要小写且不要有任何扩展名。*
树莓派在启动之后会在检测到这个文件之后自动启用 ssh 服务。随后即可通过*登录路由器*找到树莓派的 IP 地址，通过 ssh 连接到树莓派了。 



### windows

用windows下的Putty来链接Pi4！



### mac

打开mac终端，输入：

```
ssh pi@192.168.1.66			#IPv4地址是Pi4的实际局域网IP地址
```





## 搭建VNC远程桌面

SSH打命令对新手不友好。那么就用用Linux的远程桌面吧。

```
sudo raspi-config 	#进如Pi的系统配置程序
sudo reboot
```



在windows或者mac下，访问[ https://www.realvnc.com/en/connect/download/viewer/ ]( https://www.realvnc.com/en/connect/download/viewer/ )，下载对应的客户端。

然后在windows下远程桌面访问Pi4。



