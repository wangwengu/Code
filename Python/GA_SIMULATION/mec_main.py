#导入自定义的模块
import plot_fitness_by_task_amout as pfbta
import plot_fitness_by_datasize as pfbd
import plot_fitness_by_workload as pfbw
import plot_fitness_by_iteration as pfbi
#根据文章实验要求进行绘图，分别为任务量、输出数据大小、工作量、迭代次数
pfbta.plot_fitness_by_task_amout()
pfbd.plot_fitness_by_datasize()
pfbw.plot_fitness_by_workload()
pfbi.plot_fitness_by_iteration()
