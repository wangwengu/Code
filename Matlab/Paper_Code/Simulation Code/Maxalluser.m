function [MAX,temp,user] = Maxalluser(Rank,Tasknum,Usernum)
%MAXALLUSER �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
MAX=-1;
temp=1;
for j=1:Usernum
for i=1:Tasknum(1,j)
    if(MAX<Rank(1,i,j))
        MAX=Rank(1,i,j);
        user=j;
        temp=i;
    end
end
end
end

