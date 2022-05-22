import numpy as np
import pandas as pd
import graphviz
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

# 计算香农熵
def calEnt(dataSet):
    n = dataSet.shape[0]
    iset = dataSet.iloc[:, -1].value_counts()
    p = iset / n
    ent = (-p * np.log2(p)).sum()
    return ent

# 构建数据
def createDataSet():
    row_data = {
        'no surfacing': [1, 1, 1, 0, 0],
        'flippers': [1, 1, 0, 1, 1],
        'fish': ['yes', 'yes', 'no', 'no', 'no']
    }
    dataSet = pd.DataFrame(row_data)
    return dataSet

# 划分数据
def bestSplit(dataSet):
    baseEnt = calEnt(dataSet)
    bestGain = 0
    axis = -1
    for i in range(dataSet.shape[1] - 1): # 对特征的每一列进行循环
        levels = dataSet.iloc[:, i].value_counts().index # 取出所有的值 ['yes', 'no']
        ents = 0
        for j in levels: # 对当前列的每一个值进行循环
            childSet = dataSet[dataSet.iloc[:, i] == j]
            ent = calEnt(childSet) # 计算某一个子节点的信息熵
            ents += (childSet.shape[0] / dataSet.shape[0]) * ent
        infoGain = baseEnt - ents # 计算当前列的信息熵
        if infoGain > bestGain:
            bestGain = infoGain
            axis = i
    return axis

# 按照给定列切分数据集
def mySplit(dataSet, axis, value):
    col = dataSet.columns[axis]
    redataSet = dataSet.loc[dataSet[col] == value, :].drop(col, axis = 1) # 扔掉当前col列数据 axis = 0 是行 1 是列
    return redataSet

# 创建决策树
def createTree(dataSet):
    featList = list(dataSet.columns) # 提取出所有列
    classList = dataSet.iloc[:, -1].value_counts() # 获取最后一列类标签
    # 判断是否已经是纯数据或者只有一列数据
    if classList[0] == dataSet.shape[0] or dataSet.shape[1] == 1:
        return classList.index[0] # 取出具体值 'no' or 'yes'
    axis = bestSplit(dataSet)
    bestFeat = featList[axis]
    myTree = {bestFeat: {}}
    del featList[axis] # 删除当前特征
    valueList = set(dataSet.iloc[:, axis])
    for value in valueList:
        myTree[bestFeat][value] = createTree(mySplit(dataSet, axis, value))
    return myTree

# 树的存储
def saveTree(myTree):
    np.save('./myTree.npy', myTree)

# 树的读取
def readTree():
    myTree = np.load('./myTree.npy', allow_pickle = True).item()
    return myTree

# 决策树分类
def classify(inputTree, labels, testVec):
    firstStr = next(iter(inputTree)) # 获取决策树的第一个标签 例如：'no surfacing'
    secondDict = inputTree[firstStr]
    featIndex = labels.index(firstStr) # 获取下标
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]) == dict:
                classLabel = classify(secondDict[key], labels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

# 决策树预测
def acc_classify(train, test):
    inputTree = createTree(train) # 根据训练集生成一棵树
    labels = list(train.columns) # 数据集所有的列名称
    result = []
    for i in range(test.shape[0]): # 枚举测试集中的每一条数据
        testVec = test.iloc[i, :-1]
        classLabel = classify(inputTree, labels, testVec)
        result.append(classLabel)
    test['predict'] = result
    acc = (test.iloc[:, -1] == test.iloc[:, -2]).mean()
    print(f'该模型预测准确率为{acc}')
    return test

# 绘制可视化决策树
def drawDecideTree(dataSet):
    Xtrain = dataSet.iloc[:, :-1] # 特征
    Ytrain = dataSet.iloc[:, -1] # 标签
    labels = Ytrain.unique().tolist() # 标签去重 转成列表
    Ytrain = Ytrain.apply(lambda x : labels.index(x)) # 将文本转化成数字
    # 绘制树模型
    clf = DecisionTreeClassifier()
    clf = clf.fit(Xtrain, Ytrain)
    tree.export_graphviz(clf)
    dot_data = tree.export_graphviz(clf, out_file = None)
    graph1 = graphviz.Source(dot_data)
    graph1.render('./fish_gray')
    # 给图形增加标签和颜色
    dot_data = tree.export_graphviz(
        clf,
        out_file = None,
        feature_names = ['no surfacing', 'flippers'],
        class_names = ['fish', 'not fish'],
        filled = True,
        rounded = True,
        special_characters = True
    )
    # 利用render方法生成图形
    graph2 = graphviz.Source(dot_data)
    # 保存决策树
    graph2.render('./fish_color')
    print('绘制完成')

# 手动绘制决策树
# 计算叶子节点
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = next(iter(myTree)) # 获取第一个键值
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict: # 若是字典 则继续递归
            numLeafs += getNumLeafs(secondDict[key])
        else: # 到达叶子节点
            numLeafs += 1
    return numLeafs

# 计算树的深度
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = next(iter(myTree))
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            thisDepth = getTreeDepth(secondDict[key] + 1)
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

# 绘制节点
def plotNode(nodeTxt, cntrPt, parentPt, nodeType, createPlot=None):
    arrow_args = dict(arrowstyle = '<-') # 定义箭头格式
    createPlot.axl.annotate(
        nodeTxt,
        xy = parentPt,
        xycoords = 'axes fraction',
        va = 'center',
        ha = 'center',
        bbox = nodeType,
        arrowprops = arrow_args
    )