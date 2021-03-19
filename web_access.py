#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/server-probe/web_access.py
# @DATE: 2021/03/19 Fri
# @TIME: 14:56:03
#
# @DESCRIPTION: 探针获取该服务器对外访问状态模块


import time
import requests


"""
@description: 访问页面
-------
@param:
-------
@return:
"""
def test_access(web_url):
    access_info = {}
    start_time = time.time()
    try:
        response = requests.get(web_url, timeout=5)
        if (response.status_code == 200):
            access_info["200"] = "OK"
        else:
            access_info[str(response.status_code)] = response.text
        # 响应时间
        access_info["time"] = str(int((time.time()-start_time)*1000)) + "ms"
    except Exception as e:
        access_info["500"] = str(e)
        access_info["time"] = None
    return access_info

"""
@description: 获取所有需要测试网址的状态
-------
@param:
-------
@return:
"""
def test_all(web_urls):
    access_infos = {}
    for web_url in web_urls:
        access_infos[web_url] = test_access(web_url)
    return access_infos


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    print(test_all(["https://www.baidu.com", "https://www.google.com"]))