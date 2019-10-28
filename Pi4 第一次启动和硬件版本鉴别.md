# Pi4 第一次启动和硬件版本鉴别

## 硬件
连接MicroHDMI接口（主从接口，注意：插到底！），5V3A电源适配器，Type-C电源口。已经刷好系统的TF卡，插入Pi4背后的TF卡座里面。



## 软件

* 过了raspbian自检流程后，设置系统的一些配置：

1. 设置地区

2. 设置文字

3. 设置时区

4. 设置US-104键盘

5. 设置wifi

   

* 硬件鉴别

1. 内存版本鉴别最简单的命令
   pinout

2. htop查看占用和总容量

3. gpio -v （通过WiringPi） *目前系统是：2019-09-26-raspbian-buster-full.zip*

4. 查看CPU信息

   lscpu
   查看CPU 序列号：
   cat /proc/cpuinfo 
   查看CPU频率：

   sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq 

   sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq 

   sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq 





