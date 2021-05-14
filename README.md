# tiny-server-probe

## 项目功能
收集探针所部署的 Linux 服务器的 CPU、内存、硬盘和网络狀況，并以接口的形式暴露以方便远程查询和监控。  

## 演示
[API 测试](https://ceshiku.cn/tiny-server-probe/docs)  

## 环境
| 模块 | 版本 |
| -----| ---- |  
|Python|3.8.2|  
|fastapi|0.62.0|  
|requests|2.24.0|  
|uvicorn|0.13.1|

## 部署
💡 **注意事项**：  
1. [probe-install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh) 安装脚本仅在 Centos7 下测试通过，其他 Linux 发行版本请自行测试修改。  
2. **程序的启动脚本 [start.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh) 中默认项目地址在 /root/tiny-server-probe 下**，因此**部署请在服务器的 /root 下执行**，这样通过 [probe-install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh) 第 [35](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh#L35) 行命令才能将项目下载至正确位置。  
3. API 默认部署在 **57191** 端口，如需更改请在执行安装命令时更改参数，并将 [start.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh) 的第 [2](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh#2) 行的端口进行替换。  

💻 **部署指令**：
```shell
wget https://raw.githubusercontent.com/senjianlu/tiny-server-probe/main/probe-install.sh  
chmod +x probe-install.sh
# 57191 可替换为所需端口
./probe-install.sh 57191
```  

## 使用手册
请自行查询 [API 文档](https://ceshiku.cn/tiny-server-probe/docs)。