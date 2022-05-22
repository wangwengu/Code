import os
import pandas as pd
from Levenshtein import hamming

# 得到训练集
def get_train():
    path = './digits/trainingDigits'
    trainingFileList = os.listdir(path)
    train = pd.DataFrame()
    img = []
    labels = []
    for i in range(len(trainingFileList)):
        filename = trainingFileList[i]
        txt = pd.read_csv(f'./digits/trainingDigits/{filename}', header = None)
        num = ''
        for j in range(txt.shape[0]):
            num += txt.iloc[j, :]
        # num结束之后是一个列表
        img.append(num[0])
        filelabel = filename.split('_')[0]
        labels.append(filelabel)
    train['img'] = img
    train['labels'] = labels
    return train

# 得到测试集
def get_test():
    path = './digits/testDigits'
    testFileList = os.listdir(path)
    test = pd.DataFrame()
    img = []
    labels = []
    for i in range(len(testFileList)):
        filename = testFileList[i]
        txt = pd.read_csv(f'./digits/testDigits/{filename}', header = None)
        num = ''
        for j in range(txt.shape[0]):
            num += txt.iloc[j, :]
        img.append(num[0])
        filelabel = filename.split('_')[0]
        labels.append(filelabel)
    test['img'] = img
    test['labels'] = labels
    return test

# 手写数字识别
def handwritingClass(train, test, k):
    n = train.shape[0]
    m = test.shape[0]
    result = []
    for i in range(m):
        dist = []
        for j in range(n):
            d = str(hamming(train.iloc[j, 0], test.iloc[i, 0]))
            dist.append(d)
        dist_l = pd.DataFrame({'dist': dist, 'labels': (train.iloc[:, 1])})
        dr = dist_l.sort_values(by = 'dist')[:k]
        re = dr.loc[:, 'labels'].value_counts()
        result.append(re.index[0])
    result = pd.Series(result)
    test['predict'] = result
    acc = (test.iloc[:, -1] == test.iloc[:, -2]).mean()
    print(f'模型预测准确率为{acc}')
    return test