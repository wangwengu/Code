function [Bool] = IsExcept(j,Except,len)
%ISEXCEPT �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Bool=0;  
for i=1:len
      if j==Except(1,i)
          Bool=1;
          break;
      end
end
end



