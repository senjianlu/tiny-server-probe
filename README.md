# tiny-server-probe

## 项目功能
收集探针所部署的 Linux 服务器的 CPU、内存、硬盘和网络狀況，并以接口的形式暴露以方便远程查询和监控。  

## 原理
基于 Python，首先使用 psutil 模块获取本机的 CPU、内存和硬盘当前占用情况，然后使用 requests 模块访问需测试的网站链接并获取响应代码和延迟，将这两个模块的数据结果整理为 JSON 格式，最后通过 FastAPI 将整体功能以接口形式提供给外部请求。

## 演示
[API 测试](https://ceshiku.cn/tiny-server-probe/status?web_urls_a-fter_base64=WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0=)  

## 环境
| 模块 | 版本 |
| -----| ---- |  
|**Python**|**3.8.2**|  
|fastapi|0.62.0|  
|requests|2.24.0|  
|uvicorn|0.13.1|

## 部署
💡 **注意事项**：  
1. [probe-install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh) 安装脚本仅在 Centos7 下测试通过，其他 Linux 发行版本请自行测试修改。  
2. **程序的启动脚本 [start.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh) 中默认项目地址在 /root/tiny-server-probe 下**，因此**部署请在服务器的 /root 下执行**，这样通过 [probe-install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh) 第 [39](https://github.com/senjianlu/tiny-server-probe/blob/main/probe-install.sh#L39) 行命令才能将项目下载至正确位置。  
3. API 默认部署在 **57191** 端口，如需更改请在执行安装命令时更改参数，并将 [start.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh) 的第 [2](https://github.com/senjianlu/tiny-server-probe/blob/main/start.sh#L2) 行的端口进行替换。  

💻 **部署指令**：
```shell
wget https://raw.githubusercontent.com/senjianlu/tiny-server-probe/main/probe-install.sh  
chmod +x probe-install.sh
# 57191 可替换为所需端口
./probe-install.sh 57191
```  

## 使用手册
路由请自行查询 [API 文档](http://ceshiku.cn:57191/docs)。
|参数|说明|例子|
|---|---|--|
|web_urls_a-fter_base64|将 Python list 格式的待测试链接转为 str 格式|WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0=（转换前：["https://baidu.com", "https://google.com"]）|
