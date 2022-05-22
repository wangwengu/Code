import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as ast
import seaborn as sns

mean = [-5, 0, 5]
cov = np.array([[10, 0], [0, 10]])
X, Y = [], []
marker = [".", "x", "o"]
color = ['y', 'g', 'c']
for i in range(3):
    mean1 = (mean[i], mean[i])
    data = np.random.multivariate_normal(mean1, cov, 1000)
    x, y = data.T
    X.append(x)
    Y.append(y)
# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure(figsize = (10, 10))
ax1 = ast.Subplot(fig, 211)
fig.add_axes(ax1)
ax1.axis[:].set_visible(False)
ax1.axis["x"] = ax1.new_floating_axis(0, 0)
ax1.axis["x"].set_axisline_style("->", size = 1.0)
ax1.axis["y"] = ax1.new_floating_axis(1, 0)
ax1.axis["y"].set_axisline_style("-|>", size = 1.0)
ax1.set_title("二维高斯散点图如下所示")
for i in range(3):
    plt.scatter(X[i], Y[i], s = 15, marker = marker[i])
plt.axis()
plt.xlabel("x")
plt.ylabel("y")
ax2 = ast.Subplot(fig, 212)
fig.add_axes(ax2)
for i in range(3):
    sns.kdeplot(X[i], Y[i], shade = True, color = color[i])
ax2.set_title("二维高斯分布图如下所示")
plt.show()
