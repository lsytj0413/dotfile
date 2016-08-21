# /bin/bash

# Need sudo

# 1. 安装媒体解码器
apt-get install ubuntu-restricted-extras

# 2. 移动启动栏位置
gsettings set com.canonical.Unity.Launcher launcher-position Botton

# 3. 删除Amazon
apt remove unity-lens-shopping
apt-get remove unity-webapps-common

# 4. 升级系统补丁
apt update -y
apt upgrade -y
apt autoclean -y
apt clean -y

# 5. 删除libreoffice
apt-get remove libreoffice-common

# 6. 删除多余的自带软件
apt-get remove thunderbird totem rhythmbox empathy
apt-get remove brasero simple-scan gnome-mahjongg
apt-get remove aisleriot gnome-mines cheese
apt-get remove gransmission-common gnome-orca
apt-get remove webbrowser-app gnome-sudoku landscape-client-ui-install
apt-get remove onboard deja-dup

# 7. 安装vim
apt-get install vim

# 8. 安装chrome
apt-get install chrominm-browser
apt-get install libappindicator1 libindicator7
apt-get -f install

# 9. 安装搜狗输入法
apt-get install sogoupinyin

# 10. 安装wps
apt-get install wap-office

# 11. 安装cmake, git
apt-get install cmake
apt-get install git

# 12. 安装unrar
apt-get install unrar
