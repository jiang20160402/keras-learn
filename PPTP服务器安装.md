## Step1 - PPTP Installation

You will have to select one server to be responsible for handling out IPs to others and authenticating all of your servers into your VPN. This will become your PPTP Server.

```
apt-get install pptpd
```

Now you should edit /etc/pptpd.conf and add the following lines:

```
localip 10.0.0.1
remoteip 10.0.0.100-200
```

Where localip is IP address of your server and remoteip are IPs that will be assigned to clients that connect to it.

Next, you should setup authentication for PPTP by adding users and passwords. Simply add them to /etc/ppp/chap-secrets :

Where client is the username, server is type of service – pptpd for our example, secret is the password, and IP addresses specifies which IP address may authenticate. By setting ‘*’ in IP addresses field, you specify that you would accept username/password pair for any IP.

## Step2 - Add DNS servers to /etc/ppp/pptpd-options

```
ms-dns 8.8.8.8
ms-dns 8.8.4.4
```

Now you can start PPTP daemon:

```
service pptpd restart
```

Verify that it is running and accepting connections:

```
netstat -alpn | grep :1723
```

## Step3 - Setup Forwarding

It is important to enable IP forwarding on your PPTP server. This will allow you to forward packets between public IP and private IPs that you setup with PPTP. Simply edit /etc/sysctl.conf and add the following line if it doesn’t exist there already:

```
net.ipv4.ip_forward = 1
```

To make changes active, run `sysctl -p`

## Step4 - Create a NAT rule for iptables

执行

```
iptables -t nat -A POSTROUTING -o eth0 -s 10.100.55.0/24 -j SNAT --to-source 000.000.000.000 && iptables-save
```

注意要把000.000.000.000改成服务器的IP地址，10.100.55.0也要改成你之前设置的IP段，比如IP在10.100.55.*段内，就要使用10.100.55.0表示整个IP段。

另外，eth0是你的网卡，可以通过ifconfig查询，如果不是eth0则需相应修改一下。


```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && iptables-save
```

If you would also like your PPTP clients to talk to each other, add the following iptables rules:

```
iptables --table nat --append POSTROUTING --out-interface ppp0 -j MASQUERADE
iptables -I INPUT -s 10.0.0.0/8 -i ppp0 -j ACCEPT
iptables --append FORWARD --in-interface eth0 -j ACCEPT
```

Now your PPTP server also acts as a router.

If you would like to restrict which servers can connect to your droplets, you can setup an iptables rule that restricts TCP connects to port 1723.

## 监控

当我们架设好PPTP服务端时，如果我们想知道连接者的信息怎么办呢？很简单，结合以下命令即可：

首先，执行last | grep still | grep ppp可以查到使用者的IP地址。last命令用于查询连接到该服务器的计算机的信息，包括历史信息。grep still表示筛选仍在连接的信息，grep ppp表示筛选有关PPTP连接的信息。被我涂红的地方就是IP地址，最左边的一列表示连接者登录PPTP时使用的用户名，第二列是连接号。

其次，执行ifconfig可以查到某一连接号使用的总流量以及PPTP分配的内网IP等信息

最后，安装iptraf并执行（必须以root权限执行），选择General interface statistics，可以查到当前每个连接号占用的网速。其中，eth0是网卡，速度约为所有ppp连接总和的两倍，因为PPTP要转发数据包，得接收和发送各一次。

## VPN 很慢解决办法

查阅相关资料后发现是TCP的MSS大小设置的问题。具体可以参考文末给出的链接。执行

```
iptables -I FORWARD -p tcp --syn -i ppp+ -j TCPMSS --set-mss 1356
```