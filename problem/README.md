# 问题解决方案集合 #

## 无线网无法访问 ##

### 描述 ###

某天启动电脑后, 发现无线网络无法连接, 并且网络设置界面没有 **启用 WIFI** 按钮, 使用 **ifconfig** 命令没有查找到无线网络接口.

```
soren@soren-ubuntu16:~$ ifconfig
lo        Link encap:本地环回  
          inet 地址:127.0.0.1  掩码:255.0.0.0
          inet6 地址: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  跃点数:1
          接收数据包:16879 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:16879 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1 
          接收字节:26186598 (26.1 MB)  发送字节:26186598 (26.1 MB)
```

可以确认无线网卡没有被识别. 同时插上 U 盘发现无法自动挂载.

### 解决方案 ###

使用 **dmesg** 命令时输出包含如下内容:

```
Failed to start Load Kernel Modules.
See 'systemctl status systemd-modules-load.service' for details.
```

使用 **journalcrl | grep module** 命令查看输出, 包含如下内容:

```
Could not open moddep file '/lib/modules/**/modules.dep.bin'
```

使用 **lshw -C network** 查看输出:

```
*-network UNCLAIMED
       description: Wireless interface
       product: Wireless 8260
       vendor: Intel Corporation
       physical id: 0
       bus info: pci@0000:02:00.0
       logical name: wlp2s0
       version: 3a
       serial: a0:c5:89:40:2a:b8
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless
       configuration: broadcast=yes driver=iwlwifi driverversion=4.4.0-89-generic firmware=16.242414.0 ip=192.168.0.106 latency=0 link=yes multicast=yes wireless=IEEE 802.11abgn
       resources: irq:286 memory:a4100000-a4101fff
```

使用 **lspci** 查看输出:

```
00:00.0 Host bridge: Intel Corporation Sky Lake Host Bridge/DRAM Registers (rev 08)
00:02.0 VGA compatible controller: Intel Corporation Sky Lake Integrated Graphics (rev 07)
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI (rev 21)
00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
00:1c.0 PCI bridge: Intel Corporation Device 9d10 (rev f1)
00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port (rev f1)
00:1d.0 PCI bridge: Intel Corporation Device 9d18 (rev f1)
00:1f.0 ISA bridge: Intel Corporation Sunrise Point-LP LPC Controller (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
01:00.0 3D controller: NVIDIA Corporation Device 134b (rev a2)
02:00.0 Network controller: Intel Corporation Wireless 8260 (rev 3a)
03:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller (rev 01)
```

#### 针对小米 Air13.3 的 WIFI 不能使用 ####

```
vim /etc/modprobe.d/blacklist.conf
# 最后一行加入
blacklist acer-wmi
```

#### 针对 Ubuntu16 的 WIFI 不能使用 ####

1. 打开 系统设置->系统->软件和更新->开发者选项, 选择提前释放出的更新
2. 软件和更新 -> 附加驱动, 启用设备

#### Intel wireless 8260 UNCLAIMED ####

[Intel wireless 8260 - unclaimed network](https://askubuntu.com/questions/693109/intel-wireless-8260-unclaimed-network)

[Intel wireless controller 8260 unclaimed - ubuntu 15.10](https://askubuntu.com/questions/751504/intel-wireless-controller-8260-unclaimed-ubuntu-15-10)

[Installing Intel iwlwifi firmware for UNCLAIMED Wireless 8260?](https://askubuntu.com/questions/697279/installing-intel-iwlwifi-firmware-for-unclaimed-wireless-8260)

#### Load Kernel Modules Failed ####

[Failed to start Load Kernel Modules Ubuntu 16.04](https://askubuntu.com/questions/809199/failed-to-start-load-kernel-modules-ubuntu-16-04)

#### Could not open moddep file ####

[“Could not open moddep file '/lib/modules/3.XX-generic/modules.dep.bin'” when mounting using a loop](https://askubuntu.com/questions/459296/could-not-open-moddep-file-lib-modules-3-xx-generic-modules-dep-bin-when-mo)

#### 最终生效方案 ####

使用以下命令然后重启即生效:

```
dpkg-reconfigure linux-image-$(uname -r)
reboot
```

## 安装 emacs25 之后启动总是会 resume-layouts ##

### 描述 ###

升级 emacs25 之后, 每次启动 emacs 总是会默认恢复上次关闭时打开的所有 buffer 以及 layouts, 即使关闭 **dotspacemacs-display-default-layout** 变量也没有用. 现象就和使用 **SPC q r** 退出 emacs 相同.

### 解决方案 ###

在启动emacs 之后, 使用 ps 查看发现 emacs 总是使用 --resume-layouts 选项启动, 这应该就是造成这个现象的原因. 因为 emacs 的启动图标放在 ubuntu 的启动栏(launcher) 上, 所以应该是这个配置的原因.

编辑 ~/.local/share/applications/emacs.desktop 文件, 将 Exec 的值修改为:

```
/usr/bin/emacs %F
```

即可.
