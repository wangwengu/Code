#*******************************************************************************
#初始化模块，用于生成任务流的位置、排序
#*******************************************************************************
import random
import numpy as np
#1.任务位置随机初始化，参考论文算法1
def Position_intial(N,n,X_):
    for i in range(N):
        for j in range(n):
            X_[i][j]=random.random()
    #大于0.5为1,小于0.5为0
    X_=np.int32(X_>0.5)
    return X_

#2.产生具有一定顺序的任务流，记录前驱任务Pre_task_dict和后驱任务Sub_task_dict
def Order_initial(n):
    Pre_task_dict=dict()
    Sub_task_dict=dict()
    Pre_task_dict[1]=[]#第一个任务先放进前驱任务列字典中，其前驱任务为空
    Task_order=[1]#第一个任务先放进任务列表中
    task_previous=[1]#第一个任务先放进前驱任务列列表中
    Y_list=list(range(2,n+1))
          
    while Y_list:
        #在剩下的任务中随机选择random_temp_num个任务
        random_temp_num=np.random.randint(1,len(Y_list)+1)
        task_temp=random.sample(Y_list,random_temp_num)
        #为每个任务随机生成前驱任务
        for j in range(len(task_temp)):
            random_previous_num=np.random.randint(1,len(task_previous)+1)
            task_previous_temp=random.sample(task_previous,random_previous_num)
            #保存前驱任务字典
            Pre_task_dict[task_temp[j]]=task_previous_temp
            Y_list.remove(task_temp[j])
        task_previous=task_temp
        Task_order=Task_order+task_temp

    #找出后驱任务，保存进字典
    for key1 in range(1,n+1):
        temp=[]
        for key2 in range(1,n+1):
            if key1 in Pre_task_dict[key2]:
                temp.append(key2)
        Sub_task_dict[key1]=temp
    return Task_order,Pre_task_dict,Sub_task_dict

#3.在既定的随机任务顺序下，再次进行随机初始化，参考论文算法2
def Order_re_initial(Original,Prelist,WorkLoad,OutputSize):
    R=[]
    S=[]
    R.append(Original[0])
    S=list(Original[1:])
    WorkLoad_New=np.zeros((WorkLoad.shape))
    OutputSize_New=np.zeros((OutputSize.shape))
    while S:
        E=[]
        for i in range(len(S)):
            if set(Prelist[S[i]]).issubset(set(R)) and S[i] not in E:#Pre如何确定？
                E.append(S[i])
        s_index=random.choice(E)
        R.append(s_index)#随机选取，加入排序列表
        E.remove(s_index)
        S.remove(s_index)
    for i in range(len(R)):
        k=int(np.where(Original==R[i])[0])#原来的位置
        WorkLoad_New[0,i]=WorkLoad[0,k]
        OutputSize_New[0,i]=OutputSize[0,k]
    return R,WorkLoad_New,OutputSize_New