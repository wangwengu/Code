function [Scheduletemp,Usercurrent] = Centralschedule(Scheduletemp,Taskgraph,N,Rank,Comstartup,Transdata,Transferrateini,Computecost,Channel,Servernum,Usernum,servercandidate,Local,Timeslot,Tasknum,Num,perm,Usercurrent)
%CENTRALSCHEDULE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Startsearch=0;
        for k=1:Usernum
           if Isin(k,perm,Num)==0
               Startsearch=Startsearch+Tasknum(1,k);
               continue;
           end
       schedulepart=zeros(2,N,Servernum+1);  
       schedulepart(:,:,1:Servernum)=Scheduletemp(:,:,1:Servernum);
       schedulepart(:,:,Servernum+1)=Scheduletemp(:,:,Servernum+k);
       [schedulepart,Usercurrent(1,servercandidate,k)]=Centraluservote(k,schedulepart,Taskgraph(:,:,k),Tasknum(1,k),N,Rank(:,:,k),Comstartup,Transdata(:,:,k),Transferrateini,Computecost(:,:,k),Channel,Servernum,Usernum,Startsearch,Tasknum(1,k),1,servercandidate,Local(1,k),Timeslot); 
        Scheduletemp(:,:,1:Servernum)=schedulepart(:,:,1:Servernum);
       Scheduletemp(:,:,Servernum+k)=schedulepart(:,:,Servernum+1);  
        Startsearch=Startsearch+Tasknum(1,k);
        end
end

