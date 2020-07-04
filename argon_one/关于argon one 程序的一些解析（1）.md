# 关于argon one 程序的一些解析（1）



### 获取脚本

* 下载地址

```
wget https://download.argon40.com/argon1.sh

```

* 安装

```
# for raspberry pi OS (raspbian)
curl https://download.argon40.com/argon1.sh | bash 

# for other OS
curl https://download.argon40.com/argonone-setup-recalbox.sh | bash

curl https://download.argon40.com/argonone-setup-osmc.sh | bash

curl https://download.argon40.com/argonone-setup-libreelec.sh | bash
```

> 多个教程地址：
>
>  https://www.waveshare.com/wiki/PI4-CASE-ARGON-ONE 
>
>  https://www.argon40.com/learn/index.php/2020/03/10/argon-one-installation-guide-for-recalbox/ 
>
>  https://www.argon40.com/learn/index.php/2020/03/10/argon-one-installation-guide-for-osmc/ 
>
>  https://www.argon40.com/learn/index.php/2020/03/10/argon-one-installation-guide-for-libreelec/ 



### 脚本的解析

argon的脚本第一次看会感觉超级累。因为脚本很多都是在执行release file的过程。大部分用到了echo语句。我先整理了一下脚本的框架

1. 3个shell函数。其实总结为2个功能：
   * **强制**创建一个文件
   * 检查一大堆包有没有被安装，这里可能存在一个语言系统的bug。
   
2. 一堆文件名的宏定义：

   程序：

   * powerbuttonscript=/usr/bin/argononed.py

   * shutdownscript=/lib/systemd/system-shutdown/argononed-poweroff.py

   配置表：

   * daemonconfigfile=/etc/argononed.conf

   * configscript=/usr/bin/argonone-config

   * removescript=/usr/bin/argonone-uninstall

   自动运行的服务：

   * daemonfanservice=/lib/systemd/system/argononed.service



