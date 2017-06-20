# /bin/bash

# 本脚本需要使用管理员权限启动
if [ $(id -u) -ne 0 ]; then
    echo "this script must be run at *ROOT* permissions." >&2
    exit 1
fi

# 1. 安装媒体解码器
apt install -y ubuntu-restricted-extras

# 2. 移动启动栏位置
gsettings set com.canonical.Unity.Launcher launcher-position Botton

# 3. 删除Amazon
apt remove -y unity-lens-shopping
apt remove -y unity-webapps-common

# 4. 升级系统补丁
apt update -y
apt upgrade -y
apt autoclean -y
apt clean -y

# 5. 删除libreoffice
apt remove -y libreoffice-common

# 6. 删除多余的自带软件
apt remove -y thunderbird totem rhythmbox empathy
apt remove -y brasero simple-scan gnome-mahjongg
apt remove -y aisleriot gnome-mines cheese
apt remove -y gransmission-common gnome-orca
apt remove -y webbrowser-app gnome-sudoku landscape-client-ui-install
apt remove -y onboard deja-dup

# 7. 安装vim
apt install -y vim

# 8. 安装chrome
apt install -y chrominm-browser
apt install -y libappindicator1 libindicator7
apt -f install

# 9. 安装搜狗输入法
apt install -y sogoupinyin

# 10. 安装wps
apt install -y wap-office

# 11. 安装cmake, git
apt install -y cmake
apt install -y git

# 12. 安装unrar
apt install -y unrar

# 13. 安装java8
# 添加PPA源
apt-get install -y software-properties-common
add-apt-repository -y ppa:webupd8team/java
# 更新源
apt-get update
# 安装oracle java8
apt install -y oracle-java8-installer
# 查看java版本
java -version
# 设置java8环境变量
apt install -y oracle-java8-set-default
# java版本切换
update-java-alternatives -s java-8-oracle

# 14. 安装alien, 一个rpm包转换为deb包的工具
apt install -y alien

# 15. 安装cloc, 代码行统计工具
apt install -y cloc

# golang1.8
add-apt-repository -y ppa:longsleep/golang-backports
apt-get update
apt-get install -y golang-go

# emacs
apt install emacs

exit 0
