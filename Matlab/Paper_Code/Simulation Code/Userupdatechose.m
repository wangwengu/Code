function [User,server] = Userupdatechose(Usercurrent,Userlast,Servernum,Usernum)
%USERUPDATECHOSE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
     Improve=zeros(1,Usernum);
      maximprove=-1;
      maxindex=-1;
     for k=1:Usernum
         Improve(1,k)=Userlast(1,k)/min(Usercurrent(:,:,k));
          if maximprove<Improve(1,k)
             maximprove=Improve(1,k);
             maxindex=k;
         end
     end
         User=maxindex;
         minindex=Usercurrent(1,1,User);
         server=1;
         for k=2:Servernum+1
             if minindex>=Usercurrent(1,k,User)
                 minindex=Usercurrent(1,k,User);
                 server=k;
             end
         end
end

