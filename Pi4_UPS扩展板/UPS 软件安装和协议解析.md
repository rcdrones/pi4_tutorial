# UPS扩展板软件安装和协议解析

## 软件安装
详细请见B站视频：
分为以下步骤配置Pi4的硬件串口。   
1. 串口激活   
2. 软件串口和硬件串口配置交互   
3. 安装minicom  
`sudo apt-get install minicom`    
4. 利用minicom 对串口进行监听   
`sudo minicom -D /dev/ttyAMA0 -b 9600`   
5.退出minicom   
```
ctrl+a z x 回车
```

## 协议解析   

例如：   
$ SmartUPS V1.00,Vin NG,BATCAP 32,Vout 5124 $

```
$ SmartUPS V1.00		协议帧头部。软件提示V1.00版本
Vin NG 				表示没有插入电源。或者外部电源输入已停电
Vin GOOD				表示外部电源输入恢复正常。
BATCAP 32			表示剩余电量的百分比。
Vout 5124			表示UPS输出的电压值。（放大了1000倍，去除小数点）


```
