function [Count] = Uploadusercount(Usernum,Servernum,Channel)
%UPLOADUSERCOUNT �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
Count=0;
for i=1:Usernum
    for j=1:Servernum
        if Channel(i,j)==1
            Count=Count+1;
        end
    end
end
end

