function [flag] = equal(Channellast,Channel,Usernum,Servernum)
%EQUAL �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
flag=1;
for k=1:Usernum
    for p=1:Servernum
        if Channellast(k,p)~=Channel(k,p)
            flag=0;
            break;
        end
    end
end
end

