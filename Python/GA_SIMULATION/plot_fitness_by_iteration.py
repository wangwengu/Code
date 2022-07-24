#******************************************************************
#根据迭代数变化画图，本例子任务量分别取[10,20,30,40,50]
#******************************************************************

#导入相关库
from parameters import *
import local_algorithm as la
import random_algorithm as ra
import genetic_algorithm as ga
import copy
import random
import numpy as np
import taskinitial as ti
import matplotlib.pyplot as plt
#画图函数
def plot_fitness_by_iteration():

	#定义三个分别用来保存不同任务量前提下,LOCAL,RANDOM,GA算法得到的适应度值
	local_fitnesses_list=[];random_fitnesses_list=[];genetic_fitnesses_list=[]
	

	#随机生成一个任务流，并保存前驱任务和后驱任务
	Task_order,Pre_task_dict,Sub_task_dict=ti.Order_init(task_num)

	#前驱任务和后驱任务保存为一个列表，其值为一个字典
	Pre_task=[];Sub_task=[];Pre_task.append(Pre_task_dict);Sub_task.append(Sub_task_dict)

	#随机生成50个位置编码,对应50个排序，而不是50个工作流
	Ga_initial_location=np.zeros((10,task_num))
	Ga_initial_location=ti.Position_init(10,task_num,Ga_initial_location)

	#由于用到了遗传算法，所以需要先进行初始化
	Ga_initial_sequence=np.int32(np.zeros((10,task_num)))
	WorkLoad_initial=np.zeros((10,task_num))
	OutputSize_initial=np.zeros((10,task_num))

	#生成该任务流中每个任务对应的输出数据大小
	OutputSize=np.random.uniform(1,25,(1,task_num))#输出数据大小
	WorkLoad=np.random.uniform(1,100,(1,task_num))#工作量

	#再遵循任务流依赖关系，生成10个排序编码，工作量编码和输出量编码
	for j in range(10):
		Ga_initial_sequence[j],WorkLoad_initial[j],OutputSize_initial[j]=ti.Order_re_init(np.array(Task_order),Pre_task_dict,WorkLoad,OutputSize)

	#迭代次数为[10,20,30,40,50]
	for i in range(10,51,10):
		print("--------------------------迭代数为",i,"时:--------------------------")

		#深度拷贝，记住数组不能直接用“=”来进行复制
		Ga_workload=copy.deepcopy(WorkLoad_initial)
		Ga_location=copy.deepcopy(Ga_initial_location)
		Ga_sequence=copy.deepcopy(Ga_initial_sequence)
		Ga_outputsize=copy.deepcopy(OutputSize_initial)
		
		#调用遗传算法，输出LOCAL,RANDOM,GA算法的适应度值
		local_fitness,random_fitness,genetic_fitness=ga.Genetic_Fitness(Ga_location,Ga_sequence,Pre_task,Sub_task,Ga_workload,Ga_outputsize,task_num,i)		
		
		local_fitnesses_list.append(local_fitness)
		random_fitnesses_list.append(random_fitness)
		genetic_fitnesses_list.append(genetic_fitness)

	plt.plot(list(range(10,51,10)),random_fitnesses_list,'r-^',list(range(10,51,10)),genetic_fitnesses_list,'g-s')
	plt.legend(('RANDOM',"GA"), loc='best')
	plt.xlabel('Iteration')
	plt.ylabel('Fitness')
	# plt.xlim(left=10)
	plt.ylim(bottom=0)
	plt.show()