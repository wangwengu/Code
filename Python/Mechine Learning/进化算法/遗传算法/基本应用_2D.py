import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 10               # DNA的长度
POP_SIZE = 100              # 种群的大小
CROSS_RATE = 0.8            # 发生交叉的比例
MUTATION_RATE = 0.003       # 发生变异的比例
N_GENERATIONS = 200         # 繁衍的代数
X_BOUND = [0, 5]            # 横坐标的取值范围

# 进化的函数
def F(x):
    return np.sin(10 * x) * x + np.cos(2 * x) * x

# 获取适应度
def get_fitness(pred):
    # 返回与最小值的差值
    # 差值越大，适应度越高
    return pred + 1e-3 - np.min(pred)

# 翻译DNA以便获取信息
def translateDNA(pop):
    # dot的函数计算乘积
    # 将基因代码翻译成[0, 5]之间的数字
    return pop.dot(2 ** np.arange(DNA_SIZE)[:: -1]) / float(2 ** DNA_SIZE - 1) * X_BOUND[1]

# 适者生存 优胜劣汰
def select(pop, fitness):
    """
    choice参数说明:
        参数1: 矩阵
        参数2: 矩阵的样式
        参数3: 是否允许重复
        参数4: 每个数出现的概率, 长度和矩阵的长度保持一致
    """
    idx = np.random.choice(np.arange(POP_SIZE), size = POP_SIZE, replace = True, p = fitness / fitness.sum())
    return pop[idx]

# 交叉
def crossover(parent, pop):
    # 产生0到1之间的随机数
    if np.random.rand() < CROSS_RATE:
        # 在族群里随机选择一个数
        i_ = np.random.randint(0, POP_SIZE, size = 1)
        # astype判断每个位置上的类型是否是布尔类型
        # [0, 1, 0, 0, 1] ===> [false, true, false, false, true]
        # 选择哪几个点进行交叉，不一定是连续点
        cross_points = np.random.randint(0, 2, size = DNA_SIZE).astype(np.bool_)
        """
        parent = np.array(      [1,     0,    1,     0,     1,    0,     0,     0,    1,    0])
        cross_points = np.array([False, True, False, False, True, False, False, True, True, False])
        以cross_points中的True为下标，将所有下标为True对应的值按照顺序依次输出出来
        parent[cross_points] = array([0, 1, 0, 1])
        b = np.array(           [1,     0,    1,     0,     0,    0,     1,     1,    1,    0])
        cross_points = np.array([False, True, False, False, True, False, False, True, True, False]) 
        以cross_points中的True为下标，将所有下标为True对应的值按照顺序依次输出出来
        b[cross_points] = array([0, 0, 1, 1])
        赋值即可
        """
        # 交叉
        parent[cross_points] = pop[i_, cross_points]
    # 此时的parent已经是交叉之后的后代了，可以称之为儿子
    return parent

# 变异
def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

# 生成DNA的二进制矩阵
pop = np.random.randint(2, size = (POP_SIZE, DNA_SIZE))

# 画动态图
plt.ion()
# X_BOUND = [0, 5], *X_BOUND将0和5拿出来
# linspace(0, 5, 200)在0到5之间均匀生成200个点
x = np.linspace(*X_BOUND, 200)
plt.plot(x, F(x))

# 繁衍N_GENEATIONS代
for _ in range(N_GENERATIONS):
    # 获取值
    F_values = F(translateDNA(pop))
    if 'sca' in globals():
        sca.remove()
    sca = plt.scatter(translateDNA(pop), F_values, s = 200, c = 'red')
    plt.pause(0.05)
    # 获取适应度
    fitness = get_fitness(F_values)
    # np.argmax(a)返回a中元素最大值所对应的索引值
    # 通过索引值获取其在pop矩阵中的二进制值
    # print("Most fitted DNA: ", pop[np.argmax(fitness), :])
    pop = select(pop, fitness)
    pop_copy = pop.copy()
    for parent in pop:
        # 交叉进化
        child = crossover(parent, pop_copy)
        # 遗传变异
        child = mutate(child)
        parent[:] = child
plt.ioff()
plt.show()
