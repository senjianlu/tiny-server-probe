#!/bin/bash
# 作者：Rabbir

# 探针所部署的端口
if  [ ! "$1" ] ;
then
    tiny_server_probe_port=57191
else
    tiny_server_probe_port=$1
fi

# 获取脚本执行的绝对路径
work_path=$(dirname $(readlink -f $0))

# 判断服务器是否在境内以使用不同源
origin=$(curl -s https://gitee.com/senjianlu/one-click-scripts/raw/main/CentOS7%20%E4%B8%8B%E5%88%A4%E6%96%AD%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%98%AF%E5%90%A6%E5%9C%A8%E5%A2%83%E5%86%85%E4%BB%A5%E4%BD%BF%E7%94%A8%E4%B8%8D%E5%90%8C%E6%BA%90/origin-check.sh | bash)

# 开放指定端口
opened_port=$(curl -s https://gitee.com/senjianlu/one-click-scripts/raw/main/CentOS7%20%E4%B8%8B%E4%B8%80%E9%94%AE%E5%BC%80%E5%90%AF%E9%98%B2%E7%81%AB%E5%A2%99%E6%8C%87%E5%AE%9A%E7%AB%AF%E5%8F%A3/open-port.sh | bash -s $tiny_server_probe_port)

# 判断 Python3 是否存在
if [[ "command not found" =~ "$(python3 -V)" ]]
then
    # 脚本安装 Gitee，脚本地址使用 Gitee 源的防止在境内服务器上无法下载脚本
    curl -s https://gitee.com/senjianlu/one-click-scripts/raw/main/CentOS7%20%E4%B8%8B%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%20Python3%20%E7%8E%AF%E5%A2%83/install.sh | bash
else
    echo "Python3 已经存在！开始准备环境......"
fi

# 默认克隆地址
install_path=/root/GitHub

# 安装 GCC 和 Python3 开发环境防止安装 psutil 时出现错误
# 参照：https://github.com/giampaolo/psutil/issues/1143
yum -y install gcc libffi-devel pyt
yum -y install python3-devel
yum -y install git
yum -y install screen

# 克隆项目
echo "开始 Clone 项目......"
mkdir $install_path
cd $install_path
git clone https://$origin.com/senjianlu/tiny-server-probe.git

# 安装所需 Python 包
cd tiny-server-probe
pip install --upgrade pip
python3 -m pip install -r requirements.txt

# 建立 FastAPI 启动所需 Uvicorn 的软连接
ln -f /usr/local/python3/bin/uvicorn /usr/bin/uvicorn

# 修改启动器 start.sh 中的项目路径
sed -i "4c cd $install_path/tiny-server-probe/main" start.sh
# 修改启动器 start.sh 中的端口信息
sed -i "s/57191/$tiny_server_probe_port/" start.sh

# 启动
chmod +x start.sh
./start.sh

# 配置 Screen 能读取环境变量
echo 'shell -$SHELL' >> /etc/screenrc
# 加入开机自启动项中
echo "@reboot bash $install_path/tiny-server-probe/start.sh" >> /var/spool/cron/root
service crond restart

# 完成
echo "探针安装完成！使用以下命令在本机尝试访问："
echo "curl http://127.0.0.1:$tiny_server_probe_port/status?web_urls_after_base64=WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0="