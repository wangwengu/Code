#LOCAL算法
from parameters import *
def Local_Fitness(WorkLoad,task_num,flow_num):
	Local_time=np.zeros((flow_num,task_num))
	Local_energy=np.zeros((flow_num,task_num))
	for i in range(flow_num):
	    for j in range(task_num):
	        Local_time[i,j]=WorkLoad[i,j]/c_M
	        Local_energy[i,j]=Local_time[i,j]*P_M
	Time=Local_time.sum()/flow_num
	Energy=Local_energy.sum()/flow_num
	Fitness_Value=0.5*Time+0.5*Energy
	return Fitness_Value 