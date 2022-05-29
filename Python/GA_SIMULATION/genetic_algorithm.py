#遗传算法
#*********************************************************************************************
#对于给定的一个任务流，在遵守任务前后顺序下，存在不同的位置编码和不同的排序编码
#比如对于任务流S，可以通过初始化得到N个位置编码，N个排序编码
	#1.调用Order_initial生成一个带前后固定顺序（即前驱任务固定）的任务流
	#2.调用N次Position_initial生成N个任务位置编码，可能存在重复
	#3.调用N次Order_re_initial生成N个重新排序的任务排序编码，可能存在重复
	#4.遗传算法执行过程
			#(1)对每一组(位置，排序)进行适应度函数测试,如果终止条件满足，则退出。否则执行步骤如下:
			#(2)利用轮盘赌方法，选择两个适应度较高的个体
			#(3)对这两个个体的位置和排序分别进行交叉操作得到新的两个个体
			#(4)对交叉得到的新的两个个体进行位置和排序进行变异操作
			#(5)计算两个新个体的适应度值,如果比现有的个体适应度低则进行替换，有几个换几个
			#(6)否则返回第(1)步
#终止条件可以有以下几种:(1)达到迭代次数;(2)达到目标;(3)与前一次比不在发再明显变化;本仿真采用第1种
#*********************************************************************************************
#导入相应的库
from parameters import *
import random_algorithm as ra#用于计算RANDOM和GA算法的适应度
import local_algorithm as la#用于计算LOCAL算法的适应度

#如果终止条件不满足，利用轮盘赌算法实现找出根据概率找出两个适应度较小的染色体
def RouletteWheelSelection(genetic_fitness_list):#genetic_fitness_list为第(1)步得到的适应度列表
	#计算适应度总和与每个适应度的比例，由于本文要求适应度越低越好，所以是反着来
	max_fitness=np.max(genetic_fitness_list)
	genetic_fitness_list=max_fitness/genetic_fitness_list
	sum_fitness=genetic_fitness_list.sum()
	prob_fitness=genetic_fitness_list/sum_fitness
	#需要随机生成两个概率用于染色体选择
	prob1=random.random()
	prob2=random.random()
	#待选的两个染色体的在列表中位置
	selection1=0
	selection2=0

	#因为要选择两个染色体，所以要转两次，轮盘转起来啦，具体原理应该能看懂吧，小哥哥
	prob_total=0
	for i in range(len(genetic_fitness_list)):
		prob_total=prob_total+prob_fitness[i]
		if prob_total>prob1:
			selection1=i
			break
	prob_total=0	
	for i in range(len(genetic_fitness_list)):
		prob_total=prob_total+prob_fitness[i]
		if prob_total>prob2 and i!=selection1:
			selection2=i
			break
	return selection1,selection2

#交叉函数实现位置交叉和排序交叉，父母一交叉生了一对双胞胎，参考论文算法3和4
def CrossOver(Ga_location,Ga_sequence,Ga_workload,Ga_outputsize,task_num,genetic_fitness_list,s1,s2):
	#交叉的位置
	cross_point=np.random.randint(0,task_num)

	#双胞胎位置编码
	Ga_new_location1=np.zeros((1,task_num))
	Ga_new_location2=np.zeros((1,task_num))

	#双胞胎排序编码
	Ga_new_sequence1=np.zeros((1,task_num))
	Ga_new_sequence2=np.zeros((1,task_num))

	#工作量和输出数据大小是跟着任务排序编码来的，因为每个任务的工作量和输出数据大小是不变的
	Ga_new_workload1=np.array(np.zeros((1,task_num)[1]))
	Ga_new_workload2=np.array(np.zeros((1,task_num)[1]))
	Ga_new_outputsize1=np.array(np.zeros((1,task_num)[1]))
	Ga_new_outputsize2=np.array(np.zeros((1,task_num)[1]))

	#开始生孩子了！！！！！
	#位置交叉
	Ga_new_location1[0,:cross_point]=Ga_location[s1,:cross_point]
	Ga_new_location1[0,cross_point:]=Ga_location[s2,cross_point:]
	Ga_new_location2[0,:cross_point]=Ga_location[s2,:cross_point]
	Ga_new_location2[0,cross_point:]=Ga_location[s1,cross_point:]
	#排序交叉
	#先将任务排序数据转化为列表，下一个注释告诉你转化的原因
	temp1=list(Ga_sequence[s1,:cross_point])+list(Ga_sequence[s2])
	temp2=list(Ga_sequence[s2,:cross_point])+list(Ga_sequence[s1])
	#去除重复的元素，并且保留重复元素中第一个元素
	#由于任务编号为1,2,3,...，不存在重复，可以使用set去重，而set强制类型转化对数组无效，所以有了前一步列表转化
	temp1=sorted(set(temp1),key=temp1.index)
	temp2=sorted(set(temp2),key=temp2.index)
	#再转回数组类型
	Ga_new_sequence1=np.array(temp1)
	Ga_new_sequence2=np.array(temp2)

	#排序交叉结束后，还要将相应发生排序改变的任务的工作量和输出数据大小一并进行交叉改变
	#此处无法使用set，因为可能存在不同任务工作量和输出数据大小相同的情况
	for i in range(task_num):
		#交叉第一个孩子的工作量和输出数据
		#如果排序未发生变化，则工作量和输出数据原位置复制
		if Ga_sequence[s1,i]==Ga_new_sequence1[i]:
			Ga_new_workload1[i]=Ga_workload[s1,i]
			Ga_new_outputsize1[i]=Ga_outputsize[s1,i]
		#如果排序发生变化，则先找到原先的位置，
		#然后将父母(父亲，母亲都可以，相同编号的任务工作量和输出数据没差)的工作量和输出数据复制到新的数组
		elif Ga_sequence[s1,i]!=Ga_new_sequence1[i]:
			k=int(np.where(Ga_sequence[s1]==Ga_new_sequence1[i])[0])
			Ga_new_workload1[i]=Ga_workload[s1,k]
			Ga_new_outputsize1[i]=Ga_outputsize[s1,k]
		
		#交叉第二个孩子的工作量和输出数据
		if Ga_sequence[s2,i]==Ga_new_sequence2[i]:
			Ga_new_workload2[i]=Ga_workload[s2,i]
			Ga_new_outputsize2[i]=Ga_outputsize[s2,i]
		elif Ga_sequence[s2,i]!=Ga_new_sequence2[i]:
			k=int(np.where(Ga_sequence[s2]==Ga_new_sequence2[i])[0])
			Ga_new_workload2[i]=Ga_workload[s2,k]
			Ga_new_outputsize2[i]=Ga_outputsize[s2,k]

	# 另一种工作量和输出数据的交叉方式，无重复数值的情况
	#-----------------------------------------------------------------------------------
	# #工作量以同样的方式进行交叉
	# temp1=list(Ga_workload[s1,:cross_point])+list(Ga_workload[s2])
	# temp2=list(Ga_workload[s2,:cross_point])+list(Ga_workload[s1])
	# #去除重复的元素，并且保留重复元素中第一个元素
	# temp1=sorted(set(temp1),key=temp1.index)
	# temp2=sorted(set(temp2),key=temp2.index)
	# Ga_new_workload1=np.array(temp1)
	# Ga_new_workload2=np.array(temp2)

	# #输出量以同样的方式进行交叉
	# temp1=list(Ga_outputsize[s1,:cross_point])+list(Ga_outputsize[s2])
	# temp2=list(Ga_outputsize[s2,:cross_point])+list(Ga_outputsize[s1])
	# print("temp1:",temp1)
	# #去除重复的元素，并且保留重复元素中第一个元素
	# temp1=sorted(set(temp1),key=temp1.index)
	# temp2=sorted(set(temp2),key=temp2.index)
	# print("temp1:",temp1)
	# Ga_new_outputsize1=np.array(temp1)
	# Ga_new_outputsize2=np.array(temp2)
	#-----------------------------------------------------------------------------------
	#返回双胞胎的位置、排序、工作量、输出数据大小
	return 	Ga_new_location1,Ga_new_location2,Ga_new_sequence1,Ga_new_sequence2,Ga_new_workload1,Ga_new_workload2,Ga_new_outputsize1,Ga_new_outputsize2

#位置、工作量、输出数据变异函数
def Order_mutation(Pre_task,Sub_task,task_num,Gs,Gw,Go,mutation_point):
	#排序变异
	#针对变异点，找到变异区间[a:b],具体过程可参照文章
	a=0;	b=0
	for i in range(1,task_num):
		if set(Pre_task[0][Gs[mutation_point]]).issubset(set(Gs[:i])):
			a=i
			break
	for i in range(task_num-1,0,-1):
		if set(Sub_task[0][Gs[mutation_point]]).issubset(set(Gs[i:])):
			b=i
			break
	#在变异区间内找到一个新的插入点
	new_insert_index=mutation_point
	while new_insert_index==mutation_point:
		new_insert_index=np.random.randint(0,b-a)

	#在变异区间内进行移形换影大法
	Gs_sub=Gs[a:b].tolist()
	Gs_sub.remove(Gs[mutation_point])
	Gs_sub.insert(new_insert_index,Gs[mutation_point])

	Gw_sub=Gw[a:b].tolist()
	Gw_sub.remove(Gw[mutation_point])
	Gw_sub.insert(new_insert_index,Gw[mutation_point])

	Go_sub=Go[a:b].tolist()
	Go_sub.remove(Go[mutation_point])
	Go_sub.insert(new_insert_index,Go[mutation_point])

	#再重新拼接成完整的染色体
	Gs=np.concatenate((Gs[:a],np.array(Gs_sub),Gs[b:]),axis=0)
	Gw=np.concatenate((Gw[:a],np.array(Gw_sub),Gw[b:]),axis=0)
	Go=np.concatenate((Go[:a],np.array(Go_sub),Go[b:]),axis=0)
	# print(Gs)
	return Gs,Gw,Go

#交叉之后是变异操作,参考论文算法5和6
def Mutation(Pre_task,Sub_task,task_num,Gl1,Gl2,Gs1,Gs2,Gw1,Gw2,Go1,Go2):
	
	#两个孩子，所以有两个变异点
	mutation_point1=np.random.randint(1,task_num-1)
	mutation_point2=np.random.randint(1,task_num-1)

	#位置变异，较简单直接将变异点设为相反数
	Gl1[0,mutation_point1]=np.abs(Gl1[0,mutation_point1]-1)
	Gl2[0,mutation_point2]=np.abs(Gl2[0,mutation_point2]-1)
	
	#调用单独的排序变异函数，进行排序变异,工作量和输出量要以同样的方式进行变异
	Gs1,Gw1,Go1=Order_mutation(Pre_task,Sub_task,task_num,Gs1,Gw1,Go1,mutation_point1)
	Gs2,Gw2,Go2=Order_mutation(Pre_task,Sub_task,task_num,Gs2,Gw2,Go2,mutation_point2)

	return Gl1,Gl2,Gs1,Gs2,Gw1,Gw2,Go1,Go2

#遗传算法主函数
def Genetic_Fitness(Ga_location,Ga_sequence,Pre_task,Sub_task,Ga_workload,Ga_outputsize,task_num,iteration):
	#LOCAL算法本来不应该放在Genetic_Fitness中，但此处为了方便，就忽略结构的严谨
	#LOCAL算法的适应值，因为LOCAL算法只是在本地进行操作，而任一任务流中每个任务的工作量都是固定不变的
	#变化的只是顺序，所以直接将任一个任务流中的任务量传递给LOCAL算法，让它算就完了，此处选择第1个
	local_fitness=la.Local_Fitness(np.mat(Ga_workload[0]),task_num,1)
	#RANDOM算法迭代得到适应值的存放在列表中，而GA算法的第一次得到的适应值就是RANDOM算法的适应值
	random_fitness_list=[]
	for i in range(iteration):
		print("第",i,"次迭代")
		#GA算法的适应值
		genetic_fitness_list=[]

		#遗传算法第(1)步，得到N(N==len(Ga_workload))个工作流的适应值
		for j in range(len(Ga_workload)):
			
			#遗传算法的第一步，计算得到的适应度值就是RANDOM算法的适应度值
			random_j=np.random.randint(0,len(Ga_workload))
			if i==0:
				random_fitness=ra.Random_Fitness(np.mat(Ga_location[random_j]),np.mat(Ga_sequence[random_j]),Pre_task,Sub_task,np.mat(Ga_workload[random_j]),np.mat(Ga_outputsize[random_j]),task_num,1)
				random_fitness_list.append(random_fitness)#N个工作量通过RANDOM算法得到的适应度值放入列表保存			
			

			genetic_fitness=ra.Random_Fitness(np.mat(Ga_location[j]),np.mat(Ga_sequence[j]),Pre_task,Sub_task,np.mat(Ga_workload[j]),np.mat(Ga_outputsize[j]),task_num,1)
			genetic_fitness_list.append(genetic_fitness)
		#遗传算法第(2)步，利用轮盘赌方法，选择两个适应度较高的个体
		s1,s2=RouletteWheelSelection(genetic_fitness_list)
		#遗传算法第(3)步,对位置和排序分别进行交叉操作,当然还包括任务量和输出数据
		Gl1,Gl2,Gs1,Gs2,Gw1,Gw2,Go1,Go2=CrossOver(Ga_location,Ga_sequence,Ga_workload,Ga_outputsize,task_num,genetic_fitness_list,s1,s2)
		#遗传算法第(4)步,对交叉得到的个体进行位置和排序进行变异操作
		Gl1,Gl2,Gs1,Gs2,Gw1,Gw2,Go1,Go2=Mutation(Pre_task,Sub_task,task_num,Gl1,Gl2,Gs1,Gs2,Gw1,Gw2,Go1,Go2)
		#计算两个新个体的适应度值,
		genetic_fitness1=ra.Random_Fitness(Gl1,np.mat(Gs1),Pre_task,Sub_task,np.mat(Gw1),np.mat(Go1),task_num,1)
		genetic_fitness2=ra.Random_Fitness(Gl2,np.mat(Gs2),Pre_task,Sub_task,np.mat(Gw2),np.mat(Go2),task_num,1)
		#找到2个适应度最差任务的对应的下标，暂时用不上
		#replace_index = map(genetic_fitness_list.index, heapq.nlargest(2,genetic_fitness_list))

		#找到和新个体1适应度差距最大的个体,replace_index1记录其位置
		replace_index1=-1
		min_fitness_diff=0
		for i in range(len(genetic_fitness_list)):
			if (genetic_fitness_list[i]-genetic_fitness1)>min_fitness_diff:
				min_fitness_diff=genetic_fitness_list[i]-genetic_fitness1
				replace_index1=i

		#找到剩下的个体中和新个体２适应度差距最大的个体,replace_index2记录其位置
		replace_index2=-1
		min_fitness_diff=0
		for i in range(len(genetic_fitness_list)):
			if (genetic_fitness_list[i]-genetic_fitness2)>min_fitness_diff and i!=replace_index1:
				min_fitness_diff=genetic_fitness_list[i]-genetic_fitness2
				replace_index2=i

		#进行替换包括位置、排序、工作量、输出数据大小
		if replace_index1>=0:
			Ga_location[replace_index1]=Gl1[0]
			Ga_sequence[replace_index1]=Gs1
			Ga_workload[replace_index1]=Gw1
			Ga_outputsize[replace_index1]=Go1
		if replace_index2>=0:
			Ga_location[replace_index2]=Gl2[0]
			Ga_sequence[replace_index2]=Gs2
			Ga_workload[replace_index2]=Gw2
			Ga_outputsize[replace_index2]=Go2
	#返回LOCAL,RANDOM,GA算法得到的适应度值
	return 	local_fitness,sum(random_fitness_list)/len(Ga_workload),sum(genetic_fitness_list)/len(Ga_workload)