# #Random算法
# #**********************************************************************************
# #随机算法，也可看做是求解的目标函数的过程，分别求以下几个部分
# #1.本地时间：本地服务器处理数据时间
# #2.卸载服务时间:(1)上传(输入)数据时间,(2)边缘服务器处理数据时间,(3)下载（输出）数据时间
# #3.本地能耗：本地数据处理能耗
# #4.边缘能耗：上传及下载能耗
# #**********************************************************************************
import numpy as np
import copy
# 导入参数
from parameters import *

# 定义随机算法函数
def Random_Fitness(Location, Sequence, PreTask, PostTask, WorkLoad, OutputSize, task_num, flow_num):
    """
    :param Location: 卸载位置（本地卸载or边缘卸载）
    :param Sequence: 任务卸载序列
    :param PreTask: 前驱任务
    :param PostTask: 后继任务
    :param WorkLoad: 任务工作量
    :param OutputSize: 任务输出大小
    :param task_num: 任务数量
    :param flow_num: 解的数量
    """

    # 参数设置
    """
    设置并行点
    并行点之前的所有任务都是具有依赖性质的，例如，任务a和任务b，他们具有的依赖关系如下：
    1）任务a和任务b是相邻任务
    2）任务a和任务b运行在不同的位置，假设，任务a运行在本地，任务b运行在边缘端
    3）任务a和任务b不互为前驱关系
    上述三项约束，必须全部满足才可
    """
    # 设置并行点
    Para_point = np.ones((flow_num, 1)) * (task_num + 1)
    # 设置上传数据的大小
    Up_size = np.zeros((flow_num, task_num))
    # 设置下载数据的大小
    Down_size = np.zeros((flow_num, task_num))
    # 并行点之前的本地时延
    Localtime1 = np.zeros((flow_num, 1))
    # 并行点之后的本地时延
    Localtime2 = np.zeros((flow_num, 1))
    # 并行点之前的边缘计算时延
    Edgetime1 = np.zeros((flow_num, 1))
    # 并行点之后的边缘计算时延
    Edgetime2 = np.zeros((flow_num, 1))
    # 本地的能耗
    Local_energy = np.zeros((flow_num, 1))
    # 上传到边缘服务器的能耗
    Edge_energy = np.zeros((flow_num, 1))
    # 适应度
    Fitness_value = np.zeros((flow_num, 1))

    # 找出可以并行执行的首个任务
    # 遍历所有方案
    for i in range(flow_num):
        # 遍历所有任务
        for j in range(task_num):
            # 找到第一个可以并行的点
            if j + 1 <= task_num and Location[i, j] != Location[i, j + 1] and Sequence[i, j] not in PreTask[i][Sequence[i, j + 1]]:
                # 记录并行点
                Para_point[i, 0] = j
                # 退出循环
                break
    # 遍历所有方案
    for i in range(flow_num):
        # 遍历所有任务
        for j in range(task_num):
            # 如果该任务在边缘执行
            if Location[i, j] == 1:
                # 遍历该任务的所有的前驱任务
                for item in PreTask[i][Sequence[i, j]]:
                    # 找到任务j的索引位置
                    k = int(np.where(Sequence[i] == item)[0])
                    # 如果该子任务在任务执行，才需要将其上传到边缘服务器
                    if Location[i, k] == 0:
                        # 累加上传大小
                        Up_size[i, j] = Up_size[i, j] + OutputSize[i, k]
                        # 累加k的下载大小
                        Down_size[i, k] = Down_size[i, k] + OutputSize[i, j]
    # 上传时延，使用深拷贝
    Up_time = copy.deepcopy(Up_size / up_Speed)
    # 下载时延，使用深拷贝
    Down_time = copy.deepcopy(Down_size / down_Speed)
    # 遍历每个方案
    for i in range(flow_num):
        # 遍历每个任务
        for j in range(task_num):
            # 如果该任务在并行点之前
            if j < Para_point[i, 0]:
                # 如果该任务在本地执行
                if Location[i, j] == 0:
                    # 计算本地时延
                    Localtime1[i, 0] = Localtime1[i, 0] + WorkLoad[i, j] / c_M
                else: # 该任务在边缘端执行
                    # 计算边缘时延
                    Edgetime1[i, 0] = Edgetime1[i, 0] + Up_time[i, j] + WorkLoad[i, j] / c_E + Down_time[i, j]
            else: # 任务在并行点之后
                # 如果该任务在本地执行
                if Location[i, j] == 0:
                    # 计算本地时延
                    Localtime2[i, 0] = Localtime2[i, 0] + WorkLoad[i, j] / c_M
                else: # 该任务在边缘端执行
                    # 计算边缘时延
                    Edgetime2[i, 0] = Edgetime2[i, 0] + Up_time[i, j] + WorkLoad[i, j] / c_E + Down_time[i, j]
        # 计算本地能耗
        Local_energy[i, 0] = (Localtime1[i, 0] + Localtime2[i, 0]) * p_M
        # 计算边缘能耗
        Edge_energy[i, 0] = Up_time.sum() * p_up_M + Down_time.sum() * p_down_M
        # 如果边缘端时延小，并行点之后选择边缘端
        if Localtime2[i, 0] > Edgetime2[i, 0]:
            Fitness_value[i, 0] = Omiga * (Localtime1[i, 0] + Edgetime1[i, 0] + Edgetime2[i, 0]) + Omiga * (Local_energy[i, 0] + Edge_energy[i, 0])
        else: # 如果边缘端时延大，并行点之后选择本地端
            Fitness_value[i, 0] = Omiga * (Localtime1[i, 0] + Edgetime1[i, 0] + Localtime2[i, 0]) + Omiga * (Local_energy[i, 0] + Edge_energy[i, 0])
    # 目标：最小化时延和能耗
    return Fitness_value.sum() / flow_num