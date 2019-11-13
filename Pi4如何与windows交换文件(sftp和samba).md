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

windows上用到的软件：filezilla.exe （绿色版）

```
host：sftp://192.168.2.101
user：pi
password：raspberry
```



## samba篇
samba就是windows最早提出的**网上邻居共享文件夹**。
我们在Pi4上安装samba服务。共享一个目录。让windows来读取和修改。这样就不存在copy过去在修改，过于缓慢的过程了。

### 安装过程
1. 安装samba软件
`sudo apt-get install samba samba-common-bin - y`
  
2. 配置/etc/samba/smb.conf文件

```
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.back
sudo nano /etc/samba/smb.conf

```

跳到最后一行，加入如下语句：

```
#加到文件的末尾
[MyFiles]
    # 说明信息
    comment = Pi4 Storage
    # 可以访问的用户
    valid users = pi,root
    # 定义主目录
    path = /home/pi/
    # 可被其他人看到资源名称（非内容）
    browseable = yes
    # 可写
    writable = yes
    # 新建文件的权限为 777或者664
    create mask = 0777
    # 新建目录的权限为 777或者775
    directory mask = 0777
```

3. 用`testparm`进行samba配置文件的测试
    正确的画，会列出来配置表。如果格式不正确，就会提示解析错误。


4. 为samba添加和创建密码，必须是linux里面已有的用户名！！

```
sudo smbpasswd -a pi
# 之后会要求输入密码。只用于samba的远程登录，可以和linux本身pi用户的密码不一样！
# 重启 samba 服务
sudo samba restart
```


5. pi4收尾工作 

  `sudo reboot`重启之后`netstat -tnl` ，查看是否有139和445端口开放。如果开放就表示准确了！回到windows上进行读取和写入的测试。

  

6. 添加自动运行

```
sudo nano /etc/rc.local

在文件的最后的exit 0 之前添加

sudo samba restart
```

   


