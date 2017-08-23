## 基本库安装

1. `apt-get install git -y`

如果使用 Chacha20 chacha20-ietf 等加密方式，请安装 libsodium ：

1. 更新包管理器 `apt-get update`

2. 包管理器安装 （非最新版本）`apt-get install libsodium-dev`

3. 推荐源码安装（最新版本）

- 获取最新的libsodium版本

```
libsodiumr_ver=$(wget --no-check-certificate -qO- https://github.com/jedisct1/libsodium/releases/latest | grep "<title>" |sed -r 's/.*Release (.+) · jedisct1.*/\1/') && echo -e ${libsodiumr_ver}
```

执行后会输出获取的最新版本号，比如 `x.x.x`这样的格式。然后执行 `libsodiumr_ver=x.x.x` (自己替换版本号)即可继续下面的下载步骤。

然后安装，编译所需组件包：`apt-get install build-essential -y`

下载最新 libsodium 版本编译文件：

```
wget -N --no-check-certificate https://github.com/jedisct1/libsodium/releases/download/${libsodiumr_ver}/libsodium-${libsodiumr_ver}.tar.gz
tar -xzf libsodium-${libsodiumr_ver}.tar.gz && cd libsodium-${libsodiumr_ver}
./configure && make -j2 && make install
ldconfig
```

编译安装完成后，就可以删除刚才下载和解压的文件了。

```
cd ..
rm -rf libsodium-${libsodiumr_ver}
rm -rf libsodium-${libsodiumr_ver}.tar.gz
```

## 获取源代码

1. `git clone -b manyuser https://github.com/ToyoDAdoubi/shadowsocksr.git`

执行完毕后此目录会新建一个shadowsocksr目录，其中根目录的是多用户版（即数据库版，个人用户请忽略这个），子目录中的是单用户版(即shadowsocksr/shadowsocks)。以下是相对路径，比如你在 /root 目录下执行上面的代码，那你的根目录就是 /root/shadowsocksr ，子目录就是 /root/shadowsocksr/shadowssocks

## 服务器端配置

进入根目录：`cd shadowsocksr`

初始化配置：`bash initcfg.sh`

通过配置文件运行：

- 打开并修改配置文件，根据下面的各选项说明来修改各个参数。 `vi user-config.json`

- 文件内容大概如下：

```
注意：新版ShadowsocksR服务端的 默认加密方式从 aes-256-cfb 改为 aes-128-ctr 了，大家注意一下。
```

```
{
  "server": "0.0.0.0",
  "server_ipv6": "::",
  "server_port": 8388,
  "local_address": "127.0.0.1",
  "local_port": 1080,
  
  "password": "m",
  "timeout": 120,
  "udp_timeout": 60,
  "method": "aes-128-ctr",
  "protocol": "auth_aes128_md5",
  "protocol_param": "",
  "obfs": "tls1.2_ticket_auth_compatible",
  "obfs_param": "",
  "speed_limit_per_con": 0,
  "speed_limit_per_user": 0,
  
  "dns_ipv6": false,
  "connect_verbose_info": 0,
  "redirect": "",
  "fast_open": false
}
```

- 进入子目录：

假设ShadowsocksR安装在 /root 目录，那么这时候我们是在 /root/shadowsocksr/shadowsocks 文件夹了。

> `cd shadowsocks`

前台运行(调试专用，断开SSH后就自动关闭)：

> python server.py

赋予脚本执行权限

> `chmod +x *.sh`

启动服务：

> `./logrun.sh`

停止服务：

> `./stop.sh`

查看日志：

> `./tail.sh`

## 开机启动

首先设置开机启动文件的权限，并打开该文件。

> `chmod +x /etc/rc.d/rc.local`

> `vi /etc/rc.d/rc.local`

然后在 exit 0 这一句代码（只有ubuntu/debian有这个 exit 0）的前面加上 下面这句代码(如果你的Shadowsocks文件夹不在root目录下，请自行修改路径)。

```
/bin/bash /root/shadowsocksr/shadowsocks/logrun.sh
```