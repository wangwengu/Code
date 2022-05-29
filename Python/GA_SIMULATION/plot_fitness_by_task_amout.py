#******************************************************************
#根据任务量变化画图，本例子任务量分别取[10,20,30,40,50]
#******************************************************************
#导入相关库
from parameters import *
import local_algorithm as la
import random_algorithm as ra
import genetic_algorithm as ga

#画图函数
def plot_fitness_by_task_amout():
	#定义三个列表，分别用来保存不同任务量前提下,LOCAL,RANDOM,GA算法得到的适应度值
	local_fitnesses_list=[];random_fitnesses_list=[];genetic_fitnesses_list=[]
	
	for i in range(50,251,50):
		print("--------------------------任务数为",i,"时:--------------------------")
		task_num=i
		#随机生成一个任务流，并保存前驱任务和后驱任务
		Task_order,Pre_task_dict,Sub_task_dict=ti.Order_initial(task_num)

		#前驱任务和后驱任务保存为一个列表，其值为一个字典
		Pre_task=[];Sub_task=[];Pre_task.append(Pre_task_dict);Sub_task.append(Sub_task_dict)

		#随机生成10个位置编码,对应10个排序，而不是10个工作流
		Ga_initial_location=np.zeros((10,task_num))
		Ga_initial_location=ti.Position_intial(10,task_num,Ga_initial_location)

		#生成这个工作流中每个任务对应的工作量和输出数据大小
		WorkLoad=np.random.uniform(1,100,(1,task_num))#工作量
		OutputSize=np.random.uniform(1,25,(1,task_num))#输出数据大小

		#由于用到了遗传算法，所以需要先进行初始化
		Ga_initial_sequence=np.int32(np.zeros((10,task_num)))
		WorkLoad_initial=np.zeros((10,task_num))
		OutputSize_initial=np.zeros((10,task_num))

		#再遵循任务流依赖关系，生成10个排序编码，工作量编码和输出量编码
		for j in range(10):
			Ga_initial_sequence[j],WorkLoad_initial[j],OutputSize_initial[j]=ti.Order_re_initial(np.array(Task_order),Pre_task_dict,WorkLoad,OutputSize)
		
		#调用遗传算法，输出LOCAL,RANDOM,GA算法的适应度值
		local_fitness,random_fitness,genetic_fitness=ga.Genetic_Fitness(Ga_initial_location,Ga_initial_sequence,Pre_task,Sub_task,WorkLoad_initial,OutputSize_initial,task_num,10)
		local_fitnesses_list.append(local_fitness)
		random_fitnesses_list.append(random_fitness)
		genetic_fitnesses_list.append(genetic_fitness)

	plt.plot(list(range(50,251,50)),local_fitnesses_list,'r-o',list(range(50,251,50)),random_fitnesses_list,'b-^',list(range(50,251,50)),genetic_fitnesses_list,'g-s')
	plt.legend(('LOCAL', 'RANDOM','GA'), loc='best')
	plt.xlabel('Task Amount')
	plt.ylabel('Fitness')
	plt.ylim(bottom=0)
	plt.show()