import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


def first_problem():
    dset = pd.read_csv('./iris.csv')
    cols = dset.columns
    nData = []
    for i in range(len(cols) - 1):
        label = cols[i]
        data = dset[label]
        mean = np.mean(data)
        std = np.std(data)
        nCols = []
        for j in range(len(data)):
            z_score = (data[j] - mean) / std
            nCols.append(z_score)
        nData.append(nCols)
    fig, axes = plt.subplots(2, 2, figsize = (12, 8))
    x = np.arange(0, 150)
    axes[0][0].scatter(x, nData[0], marker = 'D', color = 'b')
    axes[0][0].set_xlabel(cols[0])
    axes[0][1].scatter(x, nData[1], marker = '+', color = 'y')
    axes[0][1].set_xlabel(cols[1])
    axes[1][0].scatter(x, nData[2], marker = 'x', color = 'g')
    axes[1][0].set_xlabel(cols[2])
    axes[1][1].scatter(x, nData[3], marker = 'o', color = 'c')
    axes[1][1].set_xlabel(cols[3])
    plt.show()

def second_problem():
    dset = pd.read_csv('./discrete_coefficient.txt', header = None, sep = ' ')
    cols = dset.columns
    for i in range(len(cols)):
        label = cols[i]
        data = dset[label]
        mean = np.mean(data)
        jicha = np.max(data) - np.min(data)
        std = np.std(data)
        k = std / mean
        print('第%d列\n极差：%lf\n标准差：%lf\n离散系数：%lf\n' % (i + 1, jicha, std, k))

def third_problem():
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dset = pd.read_csv('./SK.txt', header = None)
    list = dset.values[0]
    list = np.delete(list, len(list) - 1)
    sk = pd.Series(list)
    print('SK数据\n偏态系数：%lf\n峰态系数：%lf' % (sk.skew(), sk.kurt()))
    x = np.array(list)
    mu = np.mean(x)
    sigma = np.std(x)
    nums = 60
    n, bins, patches = plt.hist(x, nums, density = 1, alpha = 0.75)
    y = norm.pdf(bins, mu, sigma)
    plt.grid(True)
    plt.plot(bins, y)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title('数据直方图和最大似然高斯分布拟合图')
    plt.show()

if __name__ == '__main__':
    first_problem()
    second_problem()
    third_problem()