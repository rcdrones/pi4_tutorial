# Pi4如何和Windows交互文件

## 前语
日常办公电脑跑windows的是多数。今天来讨论下Pi4如何和Windows进行文件传输。

## 方案
1. 通过boot分区（默认是fat32格式），用读卡器在windows上copy需要的文件到raspbian上。优点：不用安装和设置任何东西。缺点:boot分区空闲只有50MB不到，只适合小文件的交换。
2. 利用sftp进行文件交互。raspbian原生就支持sftp，不用额外安装软件。
3. 利用samba进行交互。大文件不想copy到raspbian，又想直接映射来使用。类似NAS远程看片子，这类用途。


## boot分区交互
见视频操作。

## SFTP篇
SSH里面有3个组件，分别时ssh、sftp、scp。 

* ssh就是远程命令行，之前讲过的。     
* scp是进行2个节点文件的copy。说人话就是本地单个文件copy到远程服务器的某个目录下。   
* sftp可以用软件批量从一个目录传到远程另外一个目录里。可以看作是scp的加强版。

windows上用到的软件：



## samba篇
samba就是windows最早提出的**网上邻居共享文件夹**。
我们在Pi4上安装samba服务。共享一个目录。让windows来读取和修改。这样就不存在copy过去在修改，过于缓慢的过程了。





