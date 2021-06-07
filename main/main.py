#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/server-probe/main.py
# @DATE: 2021/03/19 Fri
# @TIME: 14:49:11
#
# @DESCRIPTION: 探针主模块


import time
import base64
from fastapi import FastAPI
from fastapi import HTTPException
import server_status
import web_access


# FastAPI 初始化
app = FastAPI()


"""
@description: BASE64 解码传来的需要测试访问性的网址列表
-------
@param:
-------
@return:
"""
def deocde_web_urls(web_urls_after_base64):
    web_urls_str = base64.b64decode(web_urls_after_base64.encode("utf-8"))
    # 转为字符串并去掉空格
    web_urls_str = str(web_urls_str.decode("utf-8"))
    web_urls_str = web_urls_str.replace(" ", "")
    # 如果出现字符串类型转换错误则手动纠正
    if ("b'" in web_urls_str):
        web_urls_str = web_urls_str.replace("b'[", "").replace("]'", "")
    else:
        web_urls_str = web_urls_str.replace("[", "").replace("]", "")
    # 去掉引号
    web_urls_str = web_urls_str.replace("'", "").replace('"', "")
    # 分割
    web_urls = web_urls_str.split(",")
    return web_urls


"""
@url: /status
@method:
-------
@description:
-------
@param:
-------
@return:
"""
@app.get("/status")
async def get_status(web_urls_after_base64: str = None):
    # 当前时间戳
    status = {"timestamp": time.time()}
    try:
        # 服务器当前硬件状态
        status["server_status"] = server_status.get_all()
        # 测试该服务器对网站的访问可行性
        if (web_urls_after_base64):
            web_urls = deocde_web_urls(web_urls_after_base64)
            status["web_access"] = web_access.test_all(web_urls)
        # 返回
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    for _ in range(0, 10):
        time.sleep(1)
        # print(server_status.get_all())
        # print(web_access.test_all(["https://baidu.com", "https://google.com"]))
        print(get_status(
            "WyJodHRwczovL3d3dy5iYWlkdS5jb20iLCAiaHR0cHM6Ly9nb29nbGUuY29tIl0="))