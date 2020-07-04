# 关于argon one 程序的一些解析（2）



要把一个python程序变成一种服务进行自动启动，可以用到systemd（system daemon）的技术。其中systemctl只systemd中的一个管理控制程序。实现过程如下：



* 编程自己的py源程序。并且调试都通过了。（powerbuttonscript=/usr/bin/argononed.py）

* 编写xxx.service的配置表（/lib/systemd/system/argononed.service）

  ```
  [Unit]
  Description=Test Service
  After=multi-user.target
  
  [Service]
  Type=idle
  ExecStart=/usr/bin/python3 /usr/bin/argononed.py > /home/pi/x.log  2>&1
  
  [Install]
  WantedBy=multi-user.target
  ```

  ```
  sudo chmod  644  /lib/systemd/system/argononed.service
  ```

* 激活配置文件

  ```
  sudo systemctl daemon-reload
  
  sudo systemctl enable argononed.service  #反操作就是disable。会提示"Created symlink /etc/systemd/system/multi-user.target.wants/argononed.service → /lib/systemd/system/argononed.service."
  
  sudo systemctl start argononed.service   #反操作就是stop
  
  ```

  

