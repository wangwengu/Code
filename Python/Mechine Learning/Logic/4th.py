import math
from scipy.stats import norm

u = 50
a = 5.8
a2 = 5.8 ** 2
number = 40
left = 48.2
right = 52.6
x1 = (left - u) * math.sqrt(number) / a
x2 = (right - u) * math.sqrt(number) / a
y1 = norm.cdf(x1)
y2 = norm.cdf(x2)
p = y2 - y1
print("样本均值落在48.2与52.6之间的概率: %.20lf" % (p))
