function [Rank] = Rankup(A,N)
%RANKUP �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Rank=zeros(1,N);
for i=1:N
    if A(i,i)<0
    Rank(1,i)=-2;
    continue;
    end
    Rank(1,i)=Rankrecursion(A,i,N);
end
end

