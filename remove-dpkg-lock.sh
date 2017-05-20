# /bin/bash

# 本脚本需要使用管理员权限启动
if [ $(id -u) -ne 0 ]; then
    echo "this script must be run at *ROOT* permissions." >&2
    exit 1
fi

rm /var/cache/apt/archives/lock
rm /var/lib/dpkg/lock

exit 0
