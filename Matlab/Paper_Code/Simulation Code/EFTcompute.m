function [Finishtime] = EFTcompute(A,schedule,scheduletemp,temp,j,Comstartup,Transdata,Transferrate,Computecost,N,Q,n,Startsearch,Timeslot)
%ESTCOMPUTE �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
%%N��schedule�ĳ��� n������ͼA��������

%temp=6 j=3 n=N2 Q=Q+1 N=2(N1+N2) Startsearch=N1+N2
k=0;
%scheduletemp=schedule(:,1:N,j);
%scheduletemp=sortrows(scheduletemp',1);%�����ܹ����յ�һ�е���˳������
%scheduletemp=scheduletemp';
Starttime=0;
Earlytime=0;
temp2=0;
       for i=1:n
           if A(temp,i)<0 && i~=temp
           for p=1:Q
               if schedule(1,i+Startsearch,p)~=-1
                   k=p;%ǰ������i���䵽�˺�k��ִ��
                   break;
               end
           end
                  if k==j
                      temp2=schedule(2,i+Startsearch,k);
                  else
                      Comcosttemp=Comstartup(1,k)+Transdata(i,temp)/Transferrate(k,j);
                      temp2=schedule(2,i+Startsearch,k)+Comcosttemp;%����temp��ʵ��������Կ�ʼ��ʱ��
                  end
            end
            if Earlytime<temp2
                Earlytime=temp2;
            end
       end
       Earlytime=max(Earlytime,Timeslot);
                  Start=1;
                   End=N;
                   k=ceil((Start+End)/2);                               
                     while Start~=End
                       if scheduletemp(2,k)>Earlytime
                           End=k-1;
                       else
                           Start=k;
                       end
                       k=ceil((Start+End)/2);
                     end
                     if scheduletemp(1,k)==-1|| scheduletemp(2,1)>Earlytime 
                         k=-1;
                     end
                   
                   
         %         index=-1;
          %        for q=1:N
           %            if scheduletemp(1,q)~=-1 && scheduletemp(2,q)<=Earlytime
            %               index=q; %k�������ʱ���temp2С�����һ�����
                     %      break;
             %          end
              %    end
               %   if index~=k
                %      index
                %      k
                 % end
                   
                   
                   
                   if k==-1 
                       if scheduletemp(2,N)==-1
                       Starttime=max(Earlytime,scheduletemp(2,N));
                       else
                          Start=1;
                          End=N;
                          q=floor((Start+End)/2);                               
                     while Start~=End
                       if scheduletemp(2,q)==-1
                           Start=q+1;
                       else
                           End=q;
                       end
                       q=floor((Start+End)/2);
                     end
                           if scheduletemp(1,q)-Earlytime>=Computecost(temp,j)
                               Starttime=Earlytime;
                           else
                               k=1;
                           end
                        end
                   end
                   if k~=-1
                       Starttime=Earlytime;
                       for q=(k+1):(N+1)                          
                           if q==N+1
                               Starttime=max(scheduletemp(2,N),Earlytime);
                               break;
                           end
                           if scheduletemp(1,q)>Earlytime && scheduletemp(1,q)>=max(Earlytime,scheduletemp(2,q-1))+Computecost(temp,j)
                               Starttime=max(Earlytime,scheduletemp(2,q-1));
                               break;
                           end
                       end
                   end
                   Finishtime=Starttime+Computecost(temp,j);
                 
end
                           
                  


