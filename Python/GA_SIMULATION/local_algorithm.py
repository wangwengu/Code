import numpy as np
# 导入参数
from parameters import *

# 本地计算适应度
def Local_Fitness(WorkLoad, task_num, flow_num):
    # 本地时延
    Local_time = np.zeros((flow_num, task_num))
    # 本地能耗
    Local_energy = np.zeros((flow_num, task_num))
    # 遍历每个方案
    for i in range(flow_num):
        # 遍历每个任务
        for j in range(task_num):
            # 每个任务的执行时间
            Local_time[i, j] = WorkLoad[i, j] / c_M
            # 每个任务的能耗
            Local_energy[i, j] = Local_time[i, j] * p_M
    # 每个方案的平均时间
    Time = Local_time.sum() / flow_num
    # 每个方案的平均能耗
    Energy = Local_energy.sum() / flow_num
    # 适应度函数
    Fitness_Value = 0.5 * Time + 0.5 * Energy
    # 返回即可
    return Fitness_Value