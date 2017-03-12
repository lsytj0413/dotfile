# /bin/bash
# 本脚本需要使用管理员权限启动

# 1. 安装媒体解码器
apt install ubuntu-restricted-extras

# 2. 移动启动栏位置
gsettings set com.canonical.Unity.Launcher launcher-position Botton

# 3. 删除Amazon
apt remove unity-lens-shopping
apt remove unity-webapps-common

# 4. 升级系统补丁
apt update -y
apt upgrade -y
apt autoclean -y
apt clean -y

# 5. 删除libreoffice
apt remove libreoffice-common

# 6. 删除多余的自带软件
apt remove thunderbird totem rhythmbox empathy
apt remove brasero simple-scan gnome-mahjongg
apt remove aisleriot gnome-mines cheese
apt remove gransmission-common gnome-orca
apt remove webbrowser-app gnome-sudoku landscape-client-ui-install
apt remove onboard deja-dup

# 7. 安装vim
apt install vim

# 8. 安装chrome
apt install chrominm-browser
apt install libappindicator1 libindicator7
apt -f install

# 9. 安装搜狗输入法
apt install sogoupinyin

# 10. 安装wps
apt install wap-office

# 11. 安装cmake, git
apt install cmake
apt install git

# 12. 安装unrar
apt install unrar

# 13. 安装java8
# 添加PPA源
app-apt-repository ppa:webupd8team/java
# 更新源
apt-get update
# 安装oracle java8
apt install oracle-java8-installer
# 查看java版本
java -version
# 设置java8环境变量
apt install oracle-java8-set-default
# java版本切换
update-java-alternatives -s java-8-oracle
