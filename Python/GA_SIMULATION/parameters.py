#导入相关模块
import copy
import random
import numpy as np
import taskinitial as ti
import matplotlib.pyplot as plt
#全局参数设置
flow_num=1#本以为文章提到的N=50为任务流50个，后发现指在遗传算法中备选染色体个数，在本次仿真中用不上，设为1即可
task_num=50#每个任务流中含有task_num个任务，对应遗传算法编码长度为task_num
c_M=1#移动设备计算能力
P_M=0.5#本地工作时，设备功耗
P_up=0.1#上传时，设备功耗
P_down=0.1#下载时,设备功耗
c_E=3#边缘处理能力
Omiga=0.5#目标函数权重参数,当移动设备的电池充满时,增大;当其能量下降到阈值以下时,降低。
Up_Speed=8#上传速度未知，根据仿真的情况单位应为Mb
Down_Speed=8#下载速度未知，根据仿真的情况单位应为Mb