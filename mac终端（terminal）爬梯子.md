# mac终端（terminal）爬梯子



## 前期知识

mac终端如果要上梯子。只要先期待ss client gui版。然后在gui里面选择listening  sock5:1080
http 1087 。 all done！
```
export    http_proxy=http://127.0.0.1:1087

export    https_proxy=http://127.0.0.1:1087

export    ALL_PROXY=socks5://127.0.0.1:1080
```

## 制作~/.bash_profile

```
alias ss1="export ALL_PROXY=socks5://127.0.0.1:1080"
alias ss0="unset ALL_PROXY"
alias ip="curl https://ip.cn"
```
## 然后生效.bash_profile
`source ./.bash_profile`

## 使用
```
ss1 表示 ss on
ss0 表示 ss off
ip 表示查看是否已经爬到外面ip



```



