function [Comstartuptemp] = Comstartupart(Comstartup,Servernum,User)
%COMSTARTUPDETACH �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
 Comstartuptemp=zeros(1,Servernum+1);
 Comstartuptemp(1,1:Servernum)=Comstartup(1,1:Servernum);
 Comstartuptemp(1,Servernum+1)=Comstartup(1,Servernum+User);
end

