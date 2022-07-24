#*******************************************************************************
#初始化模块，用于生成任务流的位置、排序
#*******************************************************************************
import random
import numpy as np

# 任务位置初始化，0表示在本地执行，1表示在边缘服务器执行
# 对应论文算法1
def Position_init(N, n, X_):
    # 遍历种群
    for i in range(N):
        # 遍历个体
        for j in range(n):
            # 产生0～1之间的随机数
            X_[i][j] = random.random()
    # 大于0.5为1，小于0.5为0
    X_ = np.int32(X_ > 0.5)
    return X_

# 生成每个任务的前驱任务列表和后驱任务列表
def Order_init(n):
    # 前驱任务字典
    # 任务A的前驱[a, b, c, ..., ]，任务B的前驱[...] 依次类推
    Pre_task_dict = dict()
    # 后驱任务字典， 同理
    Post_task_dict = dict()
    # 任务1是第一个任务，其无前驱，定义为空列表即可
    Pre_task_dict[1] = []
    # 任务执行列表
    Task_order = [1]
    # 前驱任务
    Task_previous = [1]
    # 待处理的任务
    Y_list = list(range(2, n + 1))

    # 处理每个任务
    while Y_list:
        # 从未进行处理的任务中随机生成需要处理的任务的数量k
        random_temp_num = np.random.randint(1, len(Y_list) + 1)
        # 从未进行处理的任务中随机挑选出k个任务
        task_temp = random.sample(Y_list, random_temp_num)
        # 遍历挑选出的k个任务
        for j in range(len(task_temp)):
            # 随机生成当前任务的前驱任务的数量k
            random_previous_num = np.random.randint(1, len(Task_previous) + 1)
            # 从前驱任务列表中随机选择k个任务
            task_previous_temp = random.sample(Task_previous, random_previous_num)
            # 将这k个任务作为任务task_temp[j]的前驱任务
            Pre_task_dict[task_temp[j]] = task_previous_temp
            # 将任务task_temp[j]移除，表明其前驱任务已经搞定
            Y_list.remove(task_temp[j])
        # 更新前驱任务列表
        Task_previous = task_temp
        # 更新任务执行顺序
        Task_order = Task_order + task_temp

    # 找出每个任务的后驱任务列表
    # 遍历所有任务
    for task1 in range(1, n + 1):
        temp = []
        # 遍历所有任务
        for task2 in range(1, n + 1):
            # 如果任务2的前驱任务里有任务1，说明任务2是任务1的后驱任务
            if task1 in Pre_task_dict[task2]:
                # 保存
                temp.append(task2)
        # 更新后驱任务列表
        Post_task_dict[task1] = temp
    # 返回任务执行顺序，前驱任务列表和后驱任务列表
    return Task_order, Pre_task_dict, Post_task_dict

# 将原始任务序列再次进行随机初始化，对应论文算法2
# 原始任务序列，前驱任务列表，任务量，输出任务量
def Order_re_init(Original, Prelist, WorkLoad, OutputSize):
    # 随机新生成的任务序列
    R = []
    # 还未新生成的任务序列
    S = []
    # 第一个任务无前驱任务，因此，将其放入随机新生成任务序列的第一位
    R.append(Original[0])
    # 第2到第n个任务还未进行处理
    S = list(Original[1:])
    # 初始化新任务的工作量
    WorkLoad_New = np.zeros((WorkLoad.shape))
    # 初始化新任务的输出数据的大小
    OutputSize_New = np.zeros((OutputSize.shape))
    # 依次按照顺序处理每个还未处理的任务
    while S:
        # 临时任务列表
        E = []
        # 遍历每个还未处理的任务
        for i in range(len(S)):
            # 如果任务S[i]的所有前驱任务已经处理完毕并且任务S[i]还未被处理，则将其加入E
            if set(Prelist[S[i]]).issubset(set(R)) and S[i] not in E:
                E.append(S[i])
        # 从待处理任务列表中，随机选择一个任务进行处理
        task = random.choice(E)
        # 将任务加入到已处理的任务列表中
        R.append(task)
        # 在待处理任务中，将其进行删除，表示已经处理完毕
        E.remove(task)
        # 在全局待处理任务中，将任务删除
        S.remove(task)
    # 遍历新生成的任务列表
    for i in range(len(R)):
        # 将此任务的原来的位置和现在的位置进行互换
        # 二维的原因：生成的是一个1 x n的二维矩阵
        k = int(np.where(Original == R[i])[0])
        # 交换两者的位置
        WorkLoad_New[0, i] = WorkLoad[0, k]
        # 交换两者的位置
        OutputSize_New[0, i] = OutputSize[0, k]
    # 返回新生成的任务序列、新工作量、新输出数据的大小
    return R, WorkLoad_New, OutputSize_New