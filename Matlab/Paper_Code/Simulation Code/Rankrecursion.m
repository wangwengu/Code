function [Rank] = Rankrecursion(A,i,N)
%RANKRECURSION �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
MAX=0;
for j=1:N
    if abs(A(i,j))~=abs(A(j,i))
        continue;
    end
       if A(i,j)>0 && i~=j
           temp=Rankrecursion(A,j,N)+A(i,j);
          if(MAX<temp)
              MAX=temp;
          end
       end
end
Rank=A(i,i)+MAX;
end
