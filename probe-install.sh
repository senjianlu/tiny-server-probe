# 安装 Python3
if [[ "command not found" =~ "$(python3 -V)" ]]
then
    echo "需要先安装 Python3！"
    version='3.8.2'
    yum -y install zlib zlib-devel bzip2 bzip2-devel ncurses ncurses-devel readline readline-devel openssl openssl-devel openssl-static xz lzma xz-devel sqlite sqlite-devel
    yum -y install gdbm gdbm-devel
    yum -y install tk tk-devel
    yum -y install libffi libffi-devel
    yum -y install zlib* libffi-devel
    yum install gcc* glien* -y
    wget https://www.python.org/ftp/python/$version/Python-$version.tgz
    tar -xvf Python-$version.tgz && mkdir /usr/local/python3 && cd Python-$version
    ./configure --prefix=/usr/local/python3 && make && make install
    ln -f /usr/local/python3/bin/python3.8 /usr/bin/python3
    ln -f /usr/local/python3/bin/pip3.8 /usr/bin/pip3
    PATH=$PATH:/usr/bin/python3
else
    echo "Python3 已经存在！"
fi

# 安装所需 Python 包
pip3 install fastapi
pip3 install requests
pip3 install psutil

# 安装 FastAPI 启动所需的 Uvicorn 并建立软连接
pip3 insatll uvicorn
ln -f /usr/local/python3/bin/uvicorn /usr/bin/uvicorn

# 判断是只下载了个 install.sh 然后运行还是已经 Clone 了项目并从文件夹中启动
if [[ "tiny-server-probe" =~ "$(pwd)" ]]
then
    echo "已经 Clone 了项目！"
else
    echo "尚未 Clone 项目或者更改了项目名，开始重新 Clone 项目！"
    # 安装 Git
    yum -y install git

    # Clone 下整个项目
    git clone https://github.com/senjianlu/tiny-server-probe.git
    cd tiny-server-probe
fi

# 开放端口
if [ "$1" = "" ] || [ $1 = 0 ]; then
    firewall-cmd --add-port=57191/tcp --permanent
else
    firewall-cmd --add-port=$1/tcp --permanent
    # 修改启动器 start.sh 中的端口信息
    sed -i "s/57191/$1/" start.sh
fi

# 启动
chmod +x start.sh
./start.sh

# 加入开机自启动项中
sed -i '$a su - root -c "$(pwd)/start.sh"' /etc/rc.d/rc.local
chmod +x /etc/rc.d/rc.local

# 完成
firewall-cmd --reload
echo "Completed!"