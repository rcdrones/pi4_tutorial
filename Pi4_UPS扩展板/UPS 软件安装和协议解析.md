# Pi4 UPS扩展板

## 前言

Pi4用UPS的好处？

* 方便带到户外供电

* 长期给监控项目的树莓派供电

* 制作树莓派官方屏一体机，网友做的[利用UPS做官方屏一体机]( https://post.smzdm.com/p/a5k697e8/ )

![](https://am.zdmimg.com/201905/18/5cdfc1c411bd32633.jpg_e680.jpg)

![](https://qnam.smzdm.com/201906/09/5cfbf6650fdd59181.jpg_e680.jpg)

* 作为一个学习python的开源项目。用Pi4与UPS进行信息交互，学习如何编写python GUI程序、python终端程序。学习如何在低电量情况下进行发送email到云端的后台程序。
* 任何需要供电平稳高可靠性的场合。



## 安装

1. 熟悉板子的接口和用途：

   * micro usb input
   * two USB-A output
   * 开关
   * 4个电量绿色led
   * 1个充电PMU红色状态灯（充电闪烁，拔出电源异常检测，充满常亮）
   * GPIO口，分为2组：UART口和POWER口
   * ISP工厂烧录、测试口：把程序灌入进去。

2. 通电测试：

   * 插入电池

   * 插入Micro USB进行充电（电源头5V2A-3A都可以）

   * 插入4B Typc-c转USB线（或者3B MicroUSB 转 USB线） 

   * 开关on/off
     如果想充满电的话，不接入负载，大约等几小时，观察电量和状态LED灯。来判断充满。



## 简单的使用树莓派进行互联测试

* 驱动树莓派和5寸屏幕  
* 外部电源断开和闭合，模拟跌落的情况
* 短路测试   



## 外壳安装和GPIO焊接

见B站视频

[B站视频]( https://www.bilibili.com/video/av75546668?p=3)





