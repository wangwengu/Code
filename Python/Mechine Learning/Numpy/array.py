import numpy as np

def part1():
    # 定义一个numpy矩阵
    array = np.array(
        [[1, 2, 3],
         [4, 5, 6]])

    # 矩阵的属性
    print('矩阵: ', array)
    print('矩阵维数: ', array.ndim)
    print('矩阵形状: ', array.shape)
    print('矩阵元素个数: ', array.size)

def part2():
    # 定义矩阵的元素类型
    # 通过设置dtype属性
    array = np.array([1, 2, 3], dtype = np.int64)
    # 生成3行4列的0矩阵
    array = np.zeros((3, 4))
    # 生成3行4列的1矩阵
    array = np.ones((3, 4))
    # 生成3行4列的空矩阵
    array = np.empty((3, 4))
    # 生成一个从10到20的步长为2的有序序列
    array = np.arange(10, 20, 2)
    # 生成一个从0到11的三行四列的矩阵
    array = np.arange(12).reshape((3, 4))
    # 生成一个从0到10，长度为10的线段，并且将其等分成6个点
    array = np.linspace(0, 10, 6)
    # 生成一个从0到10，长度为10的线段，并且将其等分成6个点，然后，变成2行3列的矩阵
    array = np.linspace(0, 10, 6).reshape((2, 3))
    print(array)

def part3():
    a = np.array([10, 20, 30, 40])
    b = np.arange(4)
    # 矩阵相加
    c = a - b
    # 矩阵相减
    c = a + b
    # 矩阵相乘
    c = a * b
    # 矩阵乘方
    c = a ** 2
    # 对于矩阵a的每一个数，求其sin值
    c = np.sin(a)
    # 对于矩阵a的每一个数，求其cos值
    c = np.cos(a)
    # 对于矩阵a的每一个数，求其tan值
    c = np.tan(a)
    # 判断b中的哪些元素大于2，返回一个列表
    c = b > 2
    # 判断b中的哪些元素小于2，返回一个列表
    c = b < 2
    # 判断b中的哪些元素等于2，返回一个列表
    c = b == 2
    # 计算矩阵a✖️矩阵b
    a = a.reshape((2, 2))
    b = b.reshape((2, 2))
    # 矩阵乘法，使用dot函数
    c = np.dot(a, b)
    # 随机生成一个2行4列的每个数都位于(0, 1)之间的矩阵a
    a = np.random.random((2, 4))
    # 获取矩阵的最大值
    c = np.max(a)
    # 获取矩阵的最小值
    c = np.min(a)
    # 获取矩阵的和
    c = np.sum(a)
    # 获取矩阵每一行的最大值
    c = np.max(a, axis = 1) # axis = 1 表示行
    # 获取矩阵每一列的最大值
    c = np.max(a, axis = 0) # axis = 0 表示列
    # 获取矩阵每一行的最小值
    c = np.min(a, axis = 1) # axis = 1 表示行
    # 获取矩阵每一列的最小值
    c = np.min(a, axis = 0) # axis = 0 表示列
    # 获取矩阵每一行的总和
    c = np.max(a, axis = 1) # axis = 1 表示行
    # 获取矩阵每一列的总和
    c = np.max(a, axis = 0) # axis = 0 表示列
    print(c)

def part4():
    a = np.arange(2, 14).reshape((3, 4))
    # 获取矩阵最小值的索引
    c = np.argmin(a)
    # 获取矩阵最大值的索引
    c = np.argmax(a)
    # 获取矩阵的平均值
    c = np.mean(a)
    # 获取矩阵的中位数
    c = np.median(a)
    # 获取矩阵的前缀和
    c = np.cumsum(a)
    # 获取矩阵的每一行的差分
    c = np.diff(a)
    # 获取矩阵中所有非零的数的索引
    # 第一个列表表示行的索引
    # 第二个列表表示列的索引
    c = np.nonzero(a)
    # 对矩阵进行逐行排序
    c = np.sort(a)
    # 对矩阵进行转置
    c = np.transpose(a)
    # 将矩阵中小于5的值变成5，大于9的数变成9，位于中间的数保持原样不变
    c = np.clip(a, 5, 9)
    # 计算矩阵每一行的平均值
    c = np.mean(a, axis = 1) # axis = 1 表示行
    # 计算矩阵每一列的平均值
    c = np.mean(a, axis = 0) # axis = 0 表示列
    print(c)

def part5():
    a = np.arange(3, 15).reshape((3, 4))
    # 获取矩阵第3行的所有数值，下标从0开始
    c = a[2, :]
    # 获取矩阵第3列的所有数据，下标从0开始
    c = a[:, 2]
    # 获取矩阵的第3行第2列的数值，下标从0开始
    c = a[2, 1]
    # 获取矩阵的第3行的第2～3列的数值
    c = a[2, 2 : 4] # 左闭右开
    # 遍历矩阵每一行
    for row in a:
        print(row)
    # 遍历矩阵每一列
    for col in a.T: # 将矩阵转置，然后，再遍历行即可
        print(col)
    # 将矩阵扁平化
    c = a.flatten() # 将其变成一维数组
    # 遍历矩阵
    for c in a.flat: # 遍历矩阵的迭代器的值
        print(c)

def part6():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    # 将矩阵a和矩阵b进行上下合并
    c = np.vstack((a, b))
    # 将矩阵a和矩阵b进行左右合并
    c = np.hstack((a, b))
    # 给矩阵a添加行纬度
    c = a[np.newaxis, :]
    # 给矩阵a添加列纬度
    c = a[:, np.newaxis]
    print(c)

if __name__ == '__main__':
    # part1()
    # part2()
    # part3()
    # part4()
    # part5()
    part6()