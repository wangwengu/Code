function [scheduletemp,usercurrent] = Centraluservote(User,scheduletemp,Taskgraph,n,N,Rank,Comstartup,Transdata,Transferrateini,Computecost,Channel,Servernum,Usernum,Startsearch,End1,End2,servercandidate,Local,Timeslot)
%USERVOTE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Transferrate=Transferrateini;
if servercandidate~=Local
[Transferrate]=Recomputecom(servercandidate,Channel,Transferrate,Transferrateini,Usernum,Servernum);
end
[Comstartuptemp]=Comstartupart(Comstartup,Servernum,User);
scheduletemp(:,1:N,:)=schedule(Taskgraph,n,N,Rank,Comstartuptemp,Transdata,Transferrate(:,:,User),Computecost,Servernum+1,scheduletemp(:,1:N,:),Startsearch,Local,servercandidate,1,Timeslot);
usercurrent=scheduletemp(2,Startsearch+End1,Servernum+1)-scheduletemp(1,Startsearch+End2,Servernum+1); %�û�1ж�ص���Ե������1��ִ��
end


