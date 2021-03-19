#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/Github/server-probe/server_status.py
# @DATE: 2021/03/19 Fri
# @TIME: 14:55:30
#
# @DESCRIPTION: 探针获取服务器硬件状态模块


import psutil
import time


# 全局变量
EXPAND = 1024 * 1024


"""
@description: 获取 CPU 当前状态
-------
@param:
-------
@return:
"""
def get_cpu_status():
    status_infos = {}
    # 当前 CPU 占用率
    status_infos["percent"] = str(psutil.cpu_percent(0)) + "%"
    return status_infos

"""
@description: 获取内存使用状态
-------
@param:
-------
@return:
"""
def get_memory_status():
    status_infos = {}
    mem = psutil.virtual_memory()
    # 当前内存使用量
    status_infos["used"] = str(round(mem.used/EXPAND, 2)) + "Mb"
    # 当前内存总量
    status_infos["total"] = str(round(mem.total/EXPAND, 2)) + "Mb"
    # 当前内存占用率
    status_infos["percent"] = str(psutil.virtual_memory().percent) + "%"
    return status_infos

"""
@description: 获取硬盘使用情况
-------
@param:
-------
@return:
"""
def get_disk_status():
    status_infos = {}
    # 获取所有磁盘
    disks = psutil.disk_partitions()
    for disk in disks:
        disk_key = disk.device
        # 初始化这个磁盘的所有信息
        status_infos[disk_key] = {}
        disk = psutil.disk_usage(disk_key)
        # 当前该磁盘使用量
        status_infos[disk_key]["used"] = str(round(disk.used/EXPAND, 2)) + "Mb"
        # 当前该磁盘总量
        status_infos[disk_key]["total"] = str(round(disk.total/EXPAND, 2)) + "Mb"
        # 当前该磁盘剩余空间
        status_infos[disk_key]["free"] = str(round(disk.free/EXPAND, 2)) + "Mb"
        # 磁盘利用率
        status_infos[disk_key]["percent"] = str(
            round(disk.used/disk.total, 2)) + "%"
    return status_infos

"""
@description: 获取所有状态
-------
@param:
-------
@return:
"""
def get_all():
    server_status_infos = {}
    server_status_infos["cpu"] = get_cpu_status()
    server_status_infos["memory"] = get_memory_status()
    server_status_infos["disk"] = get_disk_status()
    return server_status_infos

"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    for _ in range(0, 100):
        print(get_cpu_status())
        print(get_memory_status())
        print(get_disk_status())
        time.sleep(1)