# Raspbian终端命令补充

## 查询开放的端口
```
netstat -tnl
```
##  反查询开放端口的PID或者程序名称
```
netstat -apn | grep 8888
sudo kill 1234(PID)
```

## 查询可执行文件在哪里？
`whereis ls`



