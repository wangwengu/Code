function [MAX,temp] = Max(Rank,N)
%MAX �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
MAX=-2;
temp=1;
for i=1:N
    if(MAX<Rank(1,i))
        MAX=Rank(1,i);
        temp=i;
    end
end
end

