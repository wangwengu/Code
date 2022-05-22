import numpy as np

# 定义常量
TAGRET_PHRASE = 'You get it!'       # 目标DNA
POP_SIZE = 300                      # 种群大小
CROSS_RATE = 0.4                    # 交叉概率
MUTATION_RATE = 0.01                # 变异概率
N_GENERATIONS = 1000                # 迭代次数
DNA_SIZE = len(TAGRET_PHRASE)       # DNA的长度
TARGET_ASCII = np.fromstring(TAGRET_PHRASE, dtype = np.uint8) # 将字符串转成数字
ASCII_BOUND = [32, 126]             # ASCII码的范围

class GA():
    def __init__(self, DNA_size, DNA_bound, cross_rate, mutation_rate, pop_size):
        self.DNA_size = DNA_size
        DNA_bound[1] += 1
        self.dna

if __name__ == '__main__':
    ga = GA(
        DNA_size = DNA_SIZE,
        DNA_bound = ASCII_BOUND,
        cross_rate = CROSS_RATE,
        mutation_rate = MUTATION_RATE,
        pop_size = POP_SIZE
    )

