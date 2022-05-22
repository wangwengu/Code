import pandas as pd
from pyecharts.charts import Scatter, Grid, Boxplot
from pyecharts import options as opt

def clean_aset():
    aset = pd.read_csv('./alphaforestdataset.csv')
    cols = aset.columns
    new_cols = ['Classes']
    for i in cols:
        if aset[i].dtype == 'object' and i != 'Classes':
            new_cols.append(i)
    for i in cols:
        if aset[i].dtype == 'int64' or aset[i].dtype == 'float64':
            new_cols.append(i)
    print(new_cols)
    aset = aset.reindex(columns = new_cols)
    aset.to_csv('./new_alphaforestdataset.txt')
    return aset

def clean_iset():
    iset = pd.read_csv('./iris.csv')
    columns = iset.columns
    new_cols = ['label']
    for i in columns:
        if iset[i].dtype != 'float64' and i != 'label':
            new_cols.append(i)
        if iset[i].dtype == 'float64' and i != 'label':
            new_cols.append(i)
    iset = iset.reindex(columns = new_cols)
    iset.to_csv('./new_iris.csv')
    return iset

def get_iris():
    iris = pd.read_csv('./new_iris.csv')
    scatterData = {}
    grid = Grid()
    scatterList = []
    for i in iris.columns:
        if i != 'label':
            list = []
            list.extend(iris[i].tolist())
            list.append(iris[i].median())
            list.extend(iris[i].quantile([.25, .75]))
            list.append(iris[i].mean())
            list.append(iris[i].std())
            list.append(iris[i].max())
            list.append(iris[i].min())
            scatterData[i] = list
            scatterList.append(calc(list, i))
    grid.add(scatterList[0], grid_opts=opt.GridOpts(pos_top='5%', pos_bottom='55%', pos_right='55%'))
    grid.add(scatterList[1], grid_opts=opt.GridOpts(pos_top='5%', pos_bottom='55%', pos_left='55%'))
    grid.add(scatterList[2], grid_opts=opt.GridOpts(pos_top='55%', pos_bottom='5%', pos_right='55%'))
    grid.add(scatterList[3], grid_opts=opt.GridOpts(pos_top='55%', pos_bottom='5%', pos_left='55%'))
    grid.render('./scatter.html')

def calc(colVal, name):
    res = (
        Scatter()
            .add_xaxis(range(len(colVal[:-7])))
            .add_yaxis(
            '',
            colVal,
            symbol_size = 10,
            label_opts = opt.LabelOpts(is_show = False),
            markline_opts = opt.MarkLineOpts(
                data = [
                    opt.MarkLineItem(
                        name = '中位数',
                        y = colVal[-1]
                    ),
                    opt.MarkLineItem(
                        name = '下分位数',
                        y = colVal[-2]
                    ),
                    opt.MarkLineItem(
                        name = '上分位数',
                        y = colVal[-3]
                    )
                ],
                label_opts = opt.LabelOpts(is_show = False),
                linestyle_opts = opt.LineStyleOpts(width = 1)
            ),
            markpoint_opts = opt.MarkPointOpts(
                data = [
                    opt.MarkPointItem(
                        type_ = 'max',
                        name = '最大值'
                    ),
                    opt.MarkPointItem(
                               type_ = 'min',
                               name = '最小值'
                    ),
                    opt.MarkPointItem(
                        type_='average',
                        name = '均值'
                    )
                ],
                label_opts=opt.LabelOpts(position='inside'))
            )
            .set_global_opts(
                xaxis_opts = opt.AxisOpts(
                    name = name,
                    name_location = 'center',
                    name_gap = 15,
                    type_ = 'value',
                    splitline_opts=opt.SplitLineOpts(is_show = True)
                ),
                yaxis_opts = opt.AxisOpts(
                    name = 'value',
                    type_ = 'value',
                    axistick_opts = opt.AxisTickOpts(is_show = True),
                    splitline_opts = opt.SplitLineOpts(is_show = True)
                )
            )
        )
    return res

def calc_draw():
    aset = pd.read_csv('./alphaforestdataset.csv')
    new_aset = aset.dropna()
    data = [
        new_aset['Temperature'].tolist(),
        new_aset[' RH'].tolist(),
        new_aset[' Ws'].tolist(),
        new_aset['Rain '].tolist(),
        new_aset['FFMC'].tolist(),
        new_aset['DMC'].tolist(),
        new_aset['DC'].tolist(),
        new_aset['ISI'].tolist(),
        new_aset['BUI'].tolist(),
        new_aset['FWI'].tolist()
    ]
    columns = [
        'Temperature', ' RH', ' Ws', 'Rain ', 'FFMC',
        'DMC', 'DC', 'ISI', 'BUI', 'FWI'
    ]
    b_plot = Boxplot()
    b_plot = (
        b_plot
            .add_xaxis(xaxis_data = columns)
            .add_yaxis(
                series_name = '',
                y_axis = b_plot.prepare_data(data)
            )
            .set_global_opts(
                title_opts = opt.TitleOpts(
                    pos_left = 'center',
                    title = '盒图'
                ),
                tooltip_opts = opt.TooltipOpts(
                    trigger = 'item',
                    axis_pointer_type = 'shadow'
                ),
                xaxis_opts = opt.AxisOpts(
                    type_ = 'category',
                    boundary_gap = True,
                    splitarea_opts = opt.SplitAreaOpts(is_show = False),
                    axislabel_opts = opt.LabelOpts(formatter = '{value}'),
                    splitline_opts = opt.SplitLineOpts(is_show = False),
                ),
                yaxis_opts=opt.AxisOpts(
                    type_ = 'value',
                    name = 'value',
                    splitarea_opts=opt.SplitAreaOpts(
                        is_show = True,
                        areastyle_opts = opt.AreaStyleOpts(opacity = 1)
                    ),
                ),
            )
            .set_series_opts(
                tooltip_opts = opt.TooltipOpts(formatter = "{b}: {c}")
            )
            .render('./box.html')
    )

def get_result():
    aset = pd.read_csv('./alphaforestdataset.csv')
    new_aset = aset.dropna()
    print('四分位数')
    for i in new_aset.columns:
        if i != 'Classes':
            print(new_aset[i].quantile([.25, .75]))

if __name__ == '__main__':
    clean_aset()
    clean_iset()
    get_iris()
    calc_draw()
    get_result()
