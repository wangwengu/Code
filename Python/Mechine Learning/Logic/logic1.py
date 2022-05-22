import numpy as np
import matplotlib.pyplot as plt

def one():
    rowdata = [
    257, 276, 297, 252, 228, 310, 240, 228,
    265, 278, 271, 292, 261, 281, 301, 274,
    267, 280, 291, 258, 272, 284, 268, 303,
    273, 282, 263, 322, 249, 269, 290]

    # (1)
    # 计算日平均销售额
    average_money = sum(rowdata) / len(rowdata)
    print('日平均销售额: %d' % average_money)

    # 计算标准差
    std = np.std(rowdata, ddof = 1)
    print('标准差: %d' % std)

    # 计算中位数
    medium = int(np.median(rowdata))
    print('中位数: %d' % medium)

    # (2)
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 以10元为组距对该资料进行分组，分为10组，并画出直方图
    plt.xticks(range(min(rowdata),max(rowdata))[::10])
    plt.hist(rowdata, 10, edgecolor='k', alpha=0.35) # 设置直方边线颜色为黑色，不透明度为 0.35
    plt.xlabel('日销售额')
    plt.ylabel('次数')
    plt.title('某菜店元月份销售额(元)直方图')
    plt.show()

    # (3)
    # 以10元为组距分为11组，将该数据用茎叶图表示出来
    # 绘制茎叶图
    list1 = []
    list2 = []

    for i in rowdata:
        if i // 10 not in list1:
            list1.append(i // 10)
    list1.sort()

    for i in list1:
        lis_temp = []  # 存储每个茎的叶
        for j in rowdata:
            if j // 10 == i:
                lis_temp.append(j % i)
            if j % 10 > i:
                break
        list2.append(lis_temp)

    plt.plot([2, 2], [1, len(list1) + 0.5])
    plt.xlim((1.9, 3.5))

    # 去除坐标轴
    plt.axis('off')

    # 输出茎
    for i in range(len(list1)):
        plt.text(1.9, len(list1) - i, str(list1[i]), fontsize=16)
    plt.text(1.9, len(list1) + 1, '茎', fontsize=18)

    # 输出叶
    for j in range(len(list2)):
        plt.text(2.1, len(list2) - j, '，'.join(map(str, list2[j])), fontsize=16)
    plt.text(2.1, len(list1) + 1, '叶', fontsize=18)
    plt.show()

    # (4)
    # 计算上述资料的两个四分位数
    lower = np.quantile(rowdata, 0.25, interpolation='lower')
    higher = np.quantile(rowdata, 0.75, interpolation='higher')
    print('下四分位数: %d\n上四分位数: %d\n' % (lower, higher))

def two():
    data = [2, 10, 3, 6, 2, 9, 2, 4, 5, 2]
    labels = [
        '皖',
        '京',
        '闽',
        '粤',
        '湘',
        '苏',
        '鲁',
        '沪',
        '川',
        '浙'
    ]

    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.axes(aspect = 'equal')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.pie(x = data,
            labels = labels,
            autopct = '%.2f%%',
            frame = 1)
    plt.xticks(())
    plt.yticks(())

    # 添加图形标题
    plt.title('2020福布斯中国上市公司潜力企业榜(前十省及自治区)')

    # 显示图形
    plt.show()

    plt.pie(x = data,
            labels = labels,
            autopct = '%.2f%%',
            startangle = 90,
            counterclock = False,
            frame = 1)
    plt.xticks(())
    plt.yticks(())

    # 添加图形标题
    plt.title('2020福布斯中国上市公司潜力企业榜(前十省及自治区)')

    # 显示图形
    plt.show()

    plt.pie(x = data,  # 绘制数据
            labels = labels,
            autopct = '%.2f%%',
            pctdistance = 0.8,
            labeldistance = 1.0,
            startangle = 180,
            center = (4, 4),
            radius = 3.8,
            counterclock = False,
            frame = 1)
    plt.xticks(())
    plt.yticks(())

    # 添加图形标题
    plt.title('2020福布斯中国上市公司潜力企业榜(前十省及自治区)')

    # 显示图形
    plt.show()

def three():
    data = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(data, '-*', linewidth = 2,)
    plt.xticks(range(len(data)), range(11, 31))

    # 设置图表标题
    plt.title('11-30岁每年交往女(男)朋友数量折线图', fontsize = 20)
    plt.xlabel('年龄', fontsize=14)
    plt.ylabel('交往的男(女)朋友数量', fontsize=14)

    # 设置坐标轴刻度标记
    plt.tick_params(axis = 'both',labelsize = 10)
    plt.show()

if __name__ == '__main__':
    one()
    two()
    three()