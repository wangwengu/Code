# 约会网站预测

import pandas as pd
import matplotlib.pyplot as plt

# 准备数据
datingTest = pd.read_table('./datingTestSet.txt', header = None)

# 分析数据

# 区分不同颜色
Colors = []
for i in range(datingTest.shape[0]):
    m = datingTest.iloc[i, -1]
    if m == 'didntLike':
        Colors.append('black')
    if m == 'smallDoses':
        Colors.append('orange')
    if m == 'largeDoses':
        Colors.append('red')

# 绘制两两之间的散点图
plt.rcParams['font.sans-serif'] = ['SimHei']
pl = plt.figure(figsize = (12, 8))
fig1 = pl.add_subplot(221)
plt.scatter(datingTest.iloc[:, 0], datingTest.iloc[:, 1], marker = '.', c = Colors)
plt.xlabel('每年飞行常客里程')
plt.ylabel('玩游戏视频所占时间比')

fig2 = pl.add_subplot(222)
plt.scatter(datingTest.iloc[:, 1], datingTest.iloc[:, 2], marker = '.', c = Colors)
plt.xlabel('玩游戏视频所占时间比')
plt.ylabel('每周消费冰淇淋公升数')

fig3 = pl.add_subplot(223)
plt.scatter(datingTest.iloc[:, 2], datingTest.iloc[:, 0], marker = '.', c = Colors)
plt.xlabel('每周消费冰淇淋公升数')
plt.ylabel('每年飞行常客里程')
# plt.show()

# 数据归一化
def minmax(dataSet):
    minDf = dataSet.min()
    maxDf = dataSet.max()
    normSet = (dataSet - minDf) / (maxDf - minDf)
    return normSet

# 代入数据 归一化
datingT = pd.concat([minmax(datingTest.iloc[:, :3]), datingTest.iloc[:, 3]], axis = 1)

# 切分数据
def randSplit(dataSet, rate = 0.9):
    n = dataSet.shape[0]
    m = int(n * rate)
    train = dataSet.iloc[:m, :]
    test = dataSet.iloc[m:, :]
    test.index = range(test.shape[0]) # 获取范围 结果为(0, 100)
    return train, test

def datingClass(train, test, k):
    n = train.shape[1] - 1
    m = test.shape[0]
    result = []
    for i in range(m):
        dist = list((((train.iloc[:, :n] - test.iloc[i, :n]) ** 2).sum(1)) ** 0.5)
        dist_l = pd.DataFrame({'dist': dist, 'labels': (train.iloc[:, n])})
        dr = dist_l.sort_values(by = 'dist')[:k]
        re = dr.loc[:, 'labels'].value_counts()
        result.append(re.index[0])
    result = pd.Series(result)
    test['predict'] = result
    acc = (test.iloc[:, -1] == test.iloc[:, -2]).mean()
    print(f'该模型预测准确率为{acc}')

if __name__ == '__main__':
    pass