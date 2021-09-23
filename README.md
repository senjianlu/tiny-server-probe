# tiny-server-probe

## 项目功能
收集探针所部署的 Linux 服务器的 CPU、内存、硬盘和网络狀況，并以接口的形式暴露以方便远程查询和监控。  

## 原理
基于 Python，首先使用 psutil 模块获取本机的 CPU、内存和硬盘当前占用情况，然后使用 requests 模块访问需测试的网站链接并获取响应代码和延迟，将这两个模块的数据结果整理为 JSON 格式，最后通过 FastAPI 将整体功能以接口形式提供给外部请求。

## 演示
[API 测试](https://tiny-server-probe.ceshiku.cn/status?web_urls_after_base64=WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0=)  

## 环境
| 系统 | 版本 |  
| -----| ---- |  
| Linux | CentOS7 |  

| 语言 | 版本 |
| -----| ---- |  
| Python | 3.8.2 |  

| 模块 | 版本 |
| -----| ---- |   
| fastapi |0.62.0|  
| requests |2.24.0|  
| uvicorn |0.13.1|

## 部署与卸载
💡 **注意事项**：  
1. [install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/install.sh) 安装脚本仅在 CentOS7 下测试通过，其他 Linux 发行版本请自行测试修改。  
2. **程序的默认安装路径为 /root/GitHub/tiny-server-probe**，如需自定义请修改 [install.sh](https://github.com/senjianlu/tiny-server-probe/blob/main/install.sh) 第 [31](https://github.com/senjianlu/tiny-server-probe/blob/main/install.sh#L31) 行。  
3. API 默认部署在 **57191** 端口，如需更改请在执行安装命令时更改参数（带参数启动安装脚本的情况下，安装程序会自动开放指定端口的防火墙）。  

💻 **部署指令**：  
```bash
# $tiny_server_probe_port 替换为探针所部署的端口
curl -s https://gitee.com/senjianlu/tiny-server-probe/raw/main/install.sh | bash -s $tiny_server_probe_port
```  

🗑️ **卸载方法**：  
1. 删除安装路径下名为 tiny-server-probe 的文件夹。
2. 删除 crontab 中的自启动任务。
3. 卸载 Python3 和对应模块：
```bash
# 卸载 Python3 模块
pip3 uninstall fastapi
pip3 uninstall requests
pip3 uninstall uvicorn
# 删除软连接
rm -rf /usr/bin/python3
rm -rf /usr/bin/pip3
# 卸载 Python3
rm -rf /usr/local/python3
```

## 使用手册
路由请自行查询 [API 文档](https://tiny-server-probe.ceshiku.cn/docs)。
|参数|说明|例子|
|---|---|--|
|web_urls_a-fter_base64|将 Python list 格式的待测试链接转为 str 格式|WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0=（转换前：["https://baidu.com", "https://google.com"]）|  

## 特别鸣谢
- 感谢 [HostVDS](https://hostvds.com/) 为本项目提供演示用服务器