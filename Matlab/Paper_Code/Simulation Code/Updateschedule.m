function [Schedule] =Updateschedule(Schedule,Schedulelocal,Tasknum,Usernum,Servernum)
%UPDATESCHEDULE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
offset1=1;
offset2=1;
for j=1:Usernum
    offset1=offset2;
    offset2=offset2+Tasknum(1,j);
Schedule(:,offset1:offset2-1,Servernum+j)=Schedulelocal(:,offset1:offset2-1,j);
end

%Schedule(:,Startsearch+offset1:Startsearch+offset2,:)=Schedule1(:,offset1:offset2,:);

end

