## shadowsocks 服务器安装

- 更新软件源

1. `sudo apt-get update`

- 安装PIP环境

1. `sudo apt-get install python-pip`

- 直接安装shadowsocks

1. `sudo pip install shadowsocks`

## 运行 shadowsocks 服务器

启动命令如下：如果要停止运行，将命令中的start改成stop。

1. `sudo ssserver -p 8388 -k password -m rc4-md5 -d start`

也可以使用配置文件进行配置，方法创建 /etc/shadowsocks.json 文件，填入如下内容：

```
{
  "server": "my_server_ip",
  "server_port": 8388,
  "local_host": "127.0.0.1",
  "local_port": 1080,
  "password": "password",
  "timeout": 300,
  "method": "rc4-md5"
}
```

Tips: 如果需要配置多个用户，可以这样来设置：

```
{
  "server": "my_server_ip",
  "port_password": {
    "端口1": "密码1",
    "端口2": "密码2"
  },
  "timeout": 300,
  "method": "rc4-md5",
  "fast_open": false
}
```

创建完毕后， 服务文件权限：

1. `sudo chmod 755 /etc/shadowsocks.json`

为了支持这些加密方式，你需要安装

1. `sudo apt-get install python-m2crypto`

然后使用配置文件在后台运行:

1. `sudo ssserver -c /etc/shadowsocks.json -d start`

## 配置开机自启动

编辑 /etc/rc.local 文件

1. `sudo vi /etc/rc.local`

在 exit 0 这一行的上边加入如下：

1. `/usr/local/bin/ssserver -c /etc/shadowsocks.json`

或者 不用配置文件 直接加入命令启动如下：

1. `/usr/local/bin/ssserver -p 8388 -k password -m aes-256-cfb -d start`

