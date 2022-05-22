import random
import pandas as pd

# 导入数据集
lenses = pd.read_table('lenses.txt', header = None)
lenses.columns = ['age', 'prescript', 'astigmatic', 'tearRate', 'class']

def randSplit(dataSet, rate):
    l = list(dataSet.index) # 提取出所有索引 [1, 2, 3, ..., n]
    random.shuffle(l) # 随机打乱索引 [3, ..., 1, ..., n]
    dataSet.index = l # 将打乱后的索引重新赋值给原数据集
    n = dataSet.shape[0] # 行数
    m = int(n * rate) # 训练集的数量
    train = dataSet.loc[range(m), :] # 提取前 m 个作为训练集
    test = dataSet.loc[range(m, n), :] # 提取剩下的作为测试集
    dataSet.index = range(dataSet.shape[0]) # 更新愿数据集的索引 将打乱的数据下标重新更新
    test.index = range(test.shape[0]) # 更新测试集的索引
    return train, test