function [Bool] = Isin(j,In,len)
%ISEXCEPT �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Bool=0;  
for i=1:len
      if j==In(1,i)
          Bool=1;
          break;
      end
end
end

