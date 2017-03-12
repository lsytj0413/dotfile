# ubuntu使用shadowsocks

## 安装shadowsocks ##

```
sudo apt update
sudo apt install python-pip
sudo apt install python-setuptools m2crypto
apt install shadowsocks
```

## 启动shadowsocks ##

```
sslocal -c /path/to/config.json
```

## proxychains ##

proxychains可以将请求转发到shadowsocks客户端.

首先从git上获取源码并编译安装:

```
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure
make
sudo make install
```

然后配置proxychains, 将以下配置保存到 /etc/proxychains.conf

```
strict_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
quite_mode

[ProxyList]
socks5 127.0.0.1 1080
```

测试:

```
proxychains4 wget www.google.com
```

备注: proxychains不是全局代理, 若需要使用全局代理可以尝试 **redsocks**
