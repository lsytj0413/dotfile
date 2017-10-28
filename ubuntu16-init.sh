# /bin/bash

# 本脚本需要使用管理员权限启动
if [ $(id -u) -ne 0 ]; then
    echo "this script must be run at *ROOT* permissions." >&2
    exit 1
fi

remove_unused_software() {
    echo "-> Start remove unused software ..."

    echo "remove Amazon ..."
    apt remove -y unity-lens-shopping
    apt remove -y unity-webapps-common

    echo "remove libreoffice ..."
    apt remove -y libreoffice-common

    echo "remove other software ..."
    apt remove -y thunderbird totem rhythmbox empathy
    apt remove -y brasero simple-scan gnome-mahjongg
    apt remove -y aisleriot gnome-mines cheese
    apt remove -y gransmission-common gnome-orca
    apt remove -y webbrowser-app gnome-sudoku landscape-client-ui-install
    apt remove -y onboard deja-dup
}

# 1. 安装媒体解码器
apt install -y ubuntu-restricted-extras

# 2. 移动启动栏位置
gsettings set com.canonical.Unity.Launcher launcher-position Botton

# 4. 升级系统补丁
apt update -y
apt upgrade -y
apt autoclean -y
apt clean -y

# 7. 安装vim
apt install -y vim

# 8. 安装chrome
apt install -y chromium-browser
apt install -y libappindicator1 libindicator7
apt -f install

# 9. 安装搜狗输入法
wget http://cdn2.ime.sogou.com/dl/index/1491565850/sogoupinyin_2.1.0.0086_amd64.deb?st=8DYo627xnhnZof-LmEdxng&e=1507858558&fn=sogoupinyin_2.1.0.0086_amd64.deb -O sogoupinyin.deb
# apt install -y sogoupinyin
sudo dpkg -i sogoupinyin.deb

# 10. 安装wps
apt install -y wap-office
# 可使用命令: wps, wpp, et

# 11. 安装cmake, git
apt install -y cmake
apt install -y git

# 12. 安装unrar
apt install -y unrar

# 13. 安装java8
# license
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
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
# apt install -y alien

# 15. 安装cloc, 代码行统计工具
apt install -y cloc

# golang1.8
add-apt-repository -y ppa:longsleep/golang-backports
apt-get update
apt-get install -y golang-go
apt-get install -y golang-golang-x-tools

# emacs25
sudo add-apt-repository -y ppa:kelleyk/emacs
sudo apt update
sudo apt install -y emacs25

# vscode
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
apt update
apt install code

# docker

sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
sudo apt update
# 安装 latest 版本的 docker-ce
sudo proxychains4 apt install docker-ce
# 获取 docker-ce 版本
sudo apt-cache madison docker-ce
# 安装特定版本的 docker-ce
# apt install docker-ce=<version>

exit 0
