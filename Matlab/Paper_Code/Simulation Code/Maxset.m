function [Rankfirstset,Actualnum] = Maxset(Rank,Tasknum,Usernum)
%MAXSET �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Rankfirstset=zeros(1,Usernum);
Actualnum=0;
for i=1:Usernum
    [max,temp]=Max(Rank(:,:,i),Tasknum(1,i));
    if max>=0
    Rankfirstset(1,i)=temp;
    Actualnum=Actualnum+1;
    else
        Rankfirstset(1,i)=-1;
    end
end
end

