#Random算法
#**********************************************************************************
#随机算法，也可看做是求解的目标函数的过程，分别求以下几个部分
#1.本地时间：本地服务器处理数据时间
#2.卸载服务时间:(1)上传(输入)数据时间,(2)边缘服务器处理数据时间,(3)下载（输出）数据时间
#3.本地能耗：本地数据处理能耗
#4.边缘能耗：上传及下载能耗
#**********************************************************************************
#导入参数库
from parameters import *
#定义随机算法函数
def Random_Fitness(Location,Sequence,PreTask,SubTask,WorkLoad,OutputSize,task_num,flow_num):
    #定义各种中间数组
    para_point=np.ones((flow_num,1))*(task_num+1)#并行点初始化为0
    Up_Size=np.zeros((flow_num,task_num))#上传数据大小
    Down_Size=np.zeros((flow_num,task_num))#下载数据大小
    Localtime1=np.zeros((flow_num,1))#并行点前本地时间
    Localtime2=np.zeros((flow_num,1))#并行点后本地时间
    Edgetime1=np.zeros((flow_num,1))#并行点前边缘时间
    Edgetime2=np.zeros((flow_num,1))#并行点后边缘时间
    Local_energy=np.zeros((flow_num,1))#本地能耗
    Edge_energy=np.zeros((flow_num,1))#边缘能耗
    Fitness_Value =np.zeros((flow_num,1))#目标函数(适应度函数)值

    #找出第一个可以并行的点，即任务流中两个连续的任务编码不相同（一个是0,另一个是1），并且前一个非后一个的前驱任务
    for i in range(flow_num):
        for j in range(task_num):
            if j+1!=task_num and Location[i,j]!=Location[i,j+1] and Sequence[i,j] not in PreTask[i][Sequence[i,j+1]]:
                para_point[i,0]=j
                break
    #计算上传和下载数据大小
    for i in range(flow_num):
        for j in range(task_num):
            #计算本地上传到边缘端的数据大小，将每个任务的前驱任务中的本地任务输出数据求和
            #Up_Size数组保存每个任务前驱任务中本地任务的输出数据和，用来计算上传时间
            if Location[i,j]==1:#发生数据传输必定是在边缘端
                for item in PreTask[i][Sequence[i,j]]:#遍历每个边缘端的任务的前驱任务
                    k=int(np.where(Sequence[i]==item)[0])#定位每个前驱任务的下标，方便进行数据量查询
                    if Location[i,k]==0:#如果这个前驱任务的在本地执行才需要进行数据传输
                        Up_Size[i,j]=Up_Size[i,j]+OutputSize[i,k]#将满足条件的前驱任务的数据量求和
                #计算边缘端下载到本地的数据大小，如果某个任务的后驱任务中有本地任务，则将该任务输出数据求和
                #Down_Size数组保存某个满足条件的任务输出数据和，用来计算上传时间
                for item in SubTask[i][Sequence[i,j]]:#遍历每个边缘端的任务的后驱任务
                    k=int(np.where(Sequence[i]==item)[0])#定位每个后驱任务的下标，方便进行数据量查询
                    if Location[i,k]==0:#如果这个前驱任务的在本地执行才需要进行数据传输
                        Down_Size[i,j]=Down_Size[i,j]+OutputSize[i,j]#将满足条件的前驱任务的数据量求和

    #上传时间等于上传数据除以上传速度，下载时间等与下载数据除以下载速度
    Up_time=copy.deepcopy(Up_Size/Up_Speed)
    Down_time=copy.deepcopy(Down_Size/Down_Speed)
    #分别计算本地和边缘端时耗            
    for i in range(flow_num):
        for j in range(task_num):
            #如果在并行点之前，本地时间等于工作量除以本地服务器处理能力，边缘时间等于上传时间＋下载时间＋工作量／边缘服务器处理能力
            if j<para_point[i,0]:
                if Location[i,j]==0:
                    Localtime1[i,0]=Localtime1[i,0]+WorkLoad[i,j]/c_M#公式(2)
                else:
                    Edgetime1[i,0]=Edgetime1[i,0]+Up_time[i,j]+WorkLoad[i,j]/c_E+Down_time[i,j]#公式(4)
            #如果在并行点之后，时间计算如上
            else:
                if Location[i,j]==0:
                    Localtime2[i,0]=Localtime2[i,0]+WorkLoad[i,j]/c_M
                else:
                    Edgetime2[i,0]=Edgetime2[i,0]+Up_time[i,j]+WorkLoad[i,j]/c_E+Down_time[i,j]
        #能耗计算
        Local_energy[i,0]=(Localtime1[i,0]+Localtime2[i,0])*P_M#公式(3)
        Edge_energy[i,0]=Up_time.sum()*P_up+Down_time.sum()*P_down#公式(5)
        #比较并行点之后，本地运行时长和边缘运行时长，哪个长就用它加上并行点前面的本地时间和边缘时间作为最终的时长
        if Localtime2[i,0]>Edgetime2[i,0]:
            Fitness_Value[i,0] =Omiga*(Localtime1[i,0]+Edgetime1[i,0]+Localtime2[i,0])+Omiga*(Local_energy[i,0]+Edge_energy[i,0])
        else:
            Fitness_Value[i,0] =Omiga*(Localtime1[i,0]+Edgetime1[i,0]+Edgetime2[i,0])+Omiga*(Local_energy[i,0]+Edge_energy[i,0])
    return Fitness_Value.sum()/flow_num
