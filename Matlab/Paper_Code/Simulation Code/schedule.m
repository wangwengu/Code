function [schedule] = schedule(Taskgraph,n,N,Rank,Comstartup,Transdata,Transferrate,Computecost,Q,schedule,Startsearch,Local,In,len,Timeslot)
%SCHEDULE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
%n��ʾ����ͼ�е�������Ŀ  N��ʾschedule�����е�����
FirstFinish=0;
Scheduletemp=zeros(2,N,Q);
for k=1:Q 
    if k~=Local && Isin(k,In,len)==0
        continue;
    end
    Scheduletemp(:,:,k)=(sortrows(schedule(:,:,k)',1))';%�����ܹ����յ�һ�е���˳������
end
processor=0;
     for p=1:n
         [MAX,temp]=Max(Rank,n);%temp�ǵ�ǰ����������ȼ���������
        Rank(1,temp)=-1;
        for j=Q:-1:1  %ж�ص���Ե������1��ִ��
             %if i==1&&j~=Local
            %continue; ���ܰ���ĳһ������
           %  end
           if j~=Local && Isin(j,In,len)==0
               continue;
           end
            if (temp==1||temp==n)&&j~=Local
                continue;
            end
        Finishtime=EFTcompute(Taskgraph,schedule,Scheduletemp(:,:,j),temp,j,Comstartup,Transdata,Transferrate,Computecost,N,Q,n,Startsearch,Timeslot);
        if j==Local || FirstFinish>Finishtime 
            FirstFinish=Finishtime;
            processor=j;
            tempcore=j;
        end
        end
      schedule(2,temp+Startsearch,processor)=FirstFinish;
      schedule(1,temp+Startsearch,processor)=FirstFinish-Computecost(temp,tempcore);
                   if Scheduletemp(1,N,processor)==-1
                   Scheduletemp(1,N,processor)=FirstFinish-Computecost(temp,tempcore);
                   Scheduletemp(2,N,processor)=FirstFinish;
                   else
                   Start=1;
                   End=N;
                   k=floor((Start+End)/2);
                   while Start~=End
                       if Scheduletemp(2,k,processor)==-1
                           Start=k+1;
                       else
                           End=k;
                       end
                       k=floor((Start+End)/2);
                   end
                   for t=k:N
                       if Scheduletemp(2,t,processor)>FirstFinish
                           Scheduletemp(1,t-1,processor)=FirstFinish-Computecost(temp,tempcore);
                           Scheduletemp(2,t-1,processor)=FirstFinish;
                           t=N-1;
                           break;
                       else
                           Scheduletemp(1,t-1,processor)=Scheduletemp(1,t,processor);
                           Scheduletemp(2,t-1,processor)=Scheduletemp(2,t,processor);
                       end
                   end
                   if t==N
                        Scheduletemp(1,t,processor)=FirstFinish-Computecost(temp,tempcore);
                        Scheduletemp(2,t,processor)=FirstFinish;
                   end
                   end
     end
    end


