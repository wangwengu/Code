function [Channel] = UpdateChannel(Channel,User,server,Servernum,Local)
%UPDATECOM �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
     for k=1:Servernum
         if Channel(User,k)==1
             Channel(User,k)=0; %k����Userԭ��ռ�õĺ� ����Ҫ�ͷ�
            % [Transferrate]=Recomputecom(k,Channel,Transferrate1,Transferrate2,Transferrate3,Transferrate1ini,Transferrate2ini,Transferrate3ini,Num,Q);
             break;
         end
     end
        if server~=Local
       Channel(User,server)=1;
       %[Transferrate]=Recomputecom(server,Channel,Transferrate,Transferrateini,Usernum,Servernum);
        end

