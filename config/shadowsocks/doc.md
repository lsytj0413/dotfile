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

## 配置chrome ##

chrome可以使用 SwitchyOmega插件配置自动模式.

### 安装SwitchyOmega ###

1. 从 [Release](https://github.com/FelisCatus/SwitchyOmega/releases/) 下载插件

2. 从浏览器打开地址 [chrome://extensions/](chrome://extensions/)

3. 将下载的插件拖放到该页面即可进行安装

### 设置代理地址 ###

1. 打开插件的选项页面, 新建情景模式-选择代理服务器-命名(如SS), 其他选择默认, 并创建

2. 代理协议选择 SOCKS5, 地址为 127.0.0.1, 端口默认为1080, 然后保存(应用选项)

### 设置自动切换 ###

1. 点击自动切换, 在按照规则列表匹配请求后面选择刚才新建的SS, 默认情景模式选择直接链接, 然后保存

2. 规则列表设置选择 AutoProxy, 然后填入[这个地址](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt), 点击立即更新情景模式, 提示更新成功即可.

3. 点击浏览器右上角的SwitchyOmega图标, 选择自动切换即可.

## 自动运行shadowsocks ##

### 安装supervisor ###

```
sudo apt install supervisor
```

### 配置supervisor ###

编辑文件 /etc/supervisor/supervisor.conf, 或者在 /etc/supervisor/conf.d/ 新建文件 ss.conf, 加上以下内容:

```
[program:shadowsocks]
command=sslocal -c /path/to/config.json
autostart=true
autorestart=true
user=root
log_stderr=true
logfile=/var/log/shadowsocks.log
```

### supervisor开机启动 ###

编辑 /etc/rc.local, 在exit 0 之前添加:

```
service supervisor start
```
