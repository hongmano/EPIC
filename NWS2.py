
      if 'C15' in pat_seq_sp and 'C16' in pat_seq_sp:
         P_RDQS0T='11_'
      elif 'C15' in pat_seq_sp:
         P_RDQS0T='10_'
      elif 'C16' in pat_seq_sp:
         P_RDQS0T='01_'
      else:
         P_RDQS0T='00_'

      # if P_RDQS0T!='00_': print(pat_seq_sp)

      # if 'C17' in pat_seq_sp and 'C18' in pat_seq_sp:
      #    P_RDQS1T='11_'
      # elif 'C17' in pat_seq_sp:
      #    P_RDQS1T='10_'
      # elif 'C18' in pat_seq_sp:
      #    P_RDQS1T='01_'
      # else:
      #    P_RDQS1T='00_'


      if 'C19' in pat_seq_sp and 'C20' in pat_seq_sp:
         P_DMI0='11_'
      elif 'C19' in pat_seq_sp:
         P_DMI0='10_'
      elif 'C20' in pat_seq_sp:
         P_DMI0='01_'
      else:
         P_DMI0='00_'

      if 'C21' in pat_seq_sp and 'C22' in pat_seq_sp:
         P_DMI1='11_'
      elif 'C21' in pat_seq_sp:
         P_DMI1='10_'
      elif 'C22' in pat_seq_sp:
         P_DMI1='01_'
      else:
         P_DMI1='00_'




      # print('%3s %3s %3s %3s %3s %3s %3s %3s %3s %3s %4s %4s %4s'%(P_CKT,P_R0_CS,P_R1_CS,P_CA[0],P_CA[1],P_CA[2],P_CA[3],P_CA[4],P_CA[5],P_CA[6],P_WCKT,P_RDQS0T,P_RDQS1T),end=" ")
      # patline_f0[i]=patline_f0[i]+format('%1s %1s %1s %1s%1s%1s%1s%1s%1s%1s_ %2s %2s %2s '%(P_CKT,P_R0_CS,P_R1_CS,P_CA[0],P_CA[1],P_CA[2],P_CA[3],P_CA[4],P_CA[5],P_CA[6],P_WCKT,P_RDQS0T,P_RDQS1T))
      # patline_f0[i]=patline_f0[i]+format('%1s %1s %1s %1s%1s%1s%1s%1s%1s%1s_ %2s %2s %2s %2s %2s '%(P_CKT,P_R0_CS,P_R1_CS,P_CA[6],P_CA[5],P_CA[4],P_CA[3],P_CA[2],P_CA[1],P_CA[0],P_WCKT,P_RDQS0T,P_RDQS1T,P_DMI0,P_DMI1))
      patline_f0[i]=patline_f0[i]+format('%1s %1s %1s %1s%1s%1s%1s%1s%1s%1s_ %2s %2s %2s %2s '%(P_CKT,P_R0_CS,P_R1_CS,P_CA[0],P_CA[1],P_CA[2],P_CA[3],P_CA[4],P_CA[5],P_CA[6],P_WCKT,P_RDQS0T,P_DMI0,P_DMI1))
      # if P_CA[6]=="": print(patline_f0[i],P_CA,PinFm_CA)
      # patline_f0[i]=patline_f0[i]+format(' (%20s_%20s) '%(xbinary,ybinary))
      # patline_f0[i]=patline_f0[i]+format(' (%7x_%7x) '%(x_val,y_val))

      # tp data register


      # if (patline_seq[i].find("YC_3<")>1): print("-----",patline_seq[i],pat_seq_sp)
      for ixy in range(len(pat_seq_sp)):
         xy_val=0
         if pat_seq_sp[ixy].find("B<")==0:
            # pat_seq_sp[ixy]="B_1<"+pat_seq_sp[ixy][2:]
            pat_seq_sp_="B_1<"+pat_seq_sp[ixy][2:]
            pat_seq_sp[ixy]=pat_seq_sp_
            # print(xy_sp,pat_seq_sp[ixy],pat_seq_sp_)
         if pat_seq_sp[ixy].find("N<")==0:
            # pat_seq_sp[ixy]="B_1<"+pat_seq_sp[ixy][2:]
            pat_seq_sp_="N_1<"+pat_seq_sp[ixy][2:]
            pat_seq_sp[ixy]=pat_seq_sp_
            # print(xy_sp,pat_seq_sp[ixy],pat_seq_sp_)
            

         if pat_seq_sp[ixy].find("<")>1:
            # if (pat_seq_sp[ixy].find("TP_4<")>-1): 
            #    print("  ~~~  ",pat_seq_sp[ixy],end= ' : ')            
            #    print('[%8X %8X %8X %8X] [%8X %8X %8X %8X] '%(tp1_[1],tp1_[2],tp1_[3],tp1_[4],tp2_[1],tp2_[2],tp2_[3],tp2_[4]))
            # if (pat_seq_sp[ixy].find("TP1_1+D5")>-1): print("~~~  ",pat_seq_sp[ixy],end= '')
            # if (pat_seq_sp[ixy].find("_4")>-1): print("~~~  ",pat_seq_sp[ixy])
            # if (pat_seq_sp[ixy].find("YC_3<")>-1): print("~~~  ",pat_seq_sp[ixy])
            xy_sp=pat_seq_sp[ixy].split('<')
            # print(xy_sp,end="  - ")
            # if pat_seq_sp[ixy].find("<B")>-1:
            #    print(xy_sp,pat_seq_sp)
            if xy_sp[0]=='XT':
               xy_sp[0]='XT1'
            elif xy_sp[0]=='YT':
               xy_sp[0]='YT1'
            elif xy_sp[0]=='TP':
               xy_sp[0]='TP1_1'
            elif xy_sp[0][:3]=='TP_':
               xy_sp[0]="TP1_"+xy_sp[0][3]
               # print(xy_sp)
            elif xy_sp[0]=='TP1' or xy_sp[0]=='TP2':
               xy_sp[0]=xy_sp[0]+"_1"
            elif xy_sp[0]=='TPH':
               xy_sp[0]='TPH1A_1'
            elif xy_sp[0]=='TPH1' or xy_sp[0]=='TPH2':
               xy_sp[0]=xy_sp[0]+"A_1"
            elif xy_sp[0]=='D1' or xy_sp[0]=='D2':
               xy_sp[0]=xy_sp[0]+"A_1" 
            elif xy_sp[0]=='D1_2' or xy_sp[0]=='D2_2' or xy_sp[0]=='D1_3' or xy_sp[0]=='D2_3' or xy_sp[0]=='D1_4' or xy_sp[0]=='D2_4':
               xy_sp[0]=xy_sp[0][:2]+"A"+xy_sp[0][2:]
               # print(xy_sp)
            elif xy_sp[0]=='D5' or xy_sp[0]=='D6':
               xy_sp[0]=xy_sp[0]+"_1" 
            elif xy_sp[0].find('_')==-1 and xy_sp[0][1]!='T':   # non XT% YT%
               xy_sp[0]=xy_sp[0]+"_1"
            elif xy_sp[0]=='TPH_1' or xy_sp[0]=='TPH_2' or xy_sp[0]=='TPH_3' or xy_sp[0]=='TPH_4':
               xy_sp[0]=xy_sp[0][:3]+"1A_"+xy_sp[0][len(xy_sp[0])-1]
            elif xy_sp[0]=='TPH2_1' or xy_sp[0]=='TPH2_2' or xy_sp[0]=='TPH2_3' or xy_sp[0]=='TPH2_4':
               xy_sp[0]=xy_sp[0][:4]+"A_"+xy_sp[0][len(xy_sp[0])-1]


            # A < #00
            if xy_sp[1].find("#")>-1:
               # xy_sp[1]=int('0x'+xy_sp[1][xy_sp[1].find('#')+1:],16)
               xy_val=int('0x'+xy_sp[1][xy_sp[1].find('#')+1:],16)
               # print(xy_sp[0],'%5X'%(xy_val))

            # A < B op C
            elif xy_sp[1].find('+')>-1 or xy_sp[1].find('-')>-1 or xy_sp[1].find('"')>-1 or xy_sp[1].find('*')>-1:
               # print(xy_sp)
               op_1=0
               op_2=0
               # if xy_sp[1].find('"')>-1:print(xy_sp)
               if xy_sp[1].find('+')>-1:
                  xy_sp_tmp=xy_sp[1].split('+')
               elif xy_sp[1].find('-')>-1:
                  xy_sp_tmp=xy_sp[1].split('-')
               elif xy_sp[1].find('"')>-1:
                  xy_sp_tmp=xy_sp[1].split('"')
               elif xy_sp[1].find('*')>-1:
                  xy_sp_tmp=xy_sp[1].split('*')
                  print(xy_sp,"-",xy_sp_tmp)

               # print(xy_sp,"-",xy_sp[1].find('*'))

               if xy_sp_tmp[0].find('_')==-1:
                  xy_sp_tmp[0]=xy_sp_tmp[0]+"_1"
                  
               


               for iixy in range(len(xyreg_name)):
                  if xy_sp_tmp[0]==xyreg_name[iixy]:
                     op_1=xyreg_[iixy]
                     # if xy_sp[1].find('"')>-1:print(xy_sp_tmp[0],xy_sp_tmp[1],"%8X"%(op_1))

               for iit in range(len(tpreg_name)):
                  if xy_sp_tmp[0]==tpreg_name[iit]:
                     op_1=tpreg_[iit]
               if xy_sp_tmp[0] in ['TP','TP2','TP_1','TP_2','TP_3','TP_4','TP1_1','TP1_2','TP1_3','TP1_4','TP2_1','TP2_2','TP2_3','TP2_4']:
                  # if (pat_seq_sp[ixy].find("TP1_1+D5")>-1): print(" : ",xy_sp_tmp,end=" ^ ")
                  if xy_sp_tmp[0]=='TP' or xy_sp_tmp[0]=='TP_1':
                     xy_sp_tmp[0]='TP1_1' 
                  elif xy_sp_tmp[0]=='TP2':
                     xy_sp_tmp[0]='TP2_1' 
                  elif xy_sp_tmp[0]=='TP_2':
                     xy_sp_tmp[0]='TP1_2' 
                  elif xy_sp_tmp[0]=='TP_3':
                     xy_sp_tmp[0]='TP1_3' 
                  elif xy_sp_tmp[0]=='TP_4':
                     xy_sp_tmp[0]='TP1_4' 

                  tp_idx=int(xy_sp_tmp[0][4])
                  if xy_sp_tmp[0][:3]=='TP1':
                     op_1=tp1_[tp_idx]
                  elif xy_sp_tmp[0][:3]=='TP2':
                     op_1=tp2_[tp_idx]
                  else:
                     op_1=tp1_[tp_idx+10]

               if xy_sp_tmp[1]=='1':
                  op_2=int(xy_sp_tmp[1])
               elif xy_sp_tmp[1][0]=='D':
                  # if (xy_sp_tmp[0].find("YC_3")>-1): print("~~~  ",xy_sp_tmp)
                  if xy_sp_tmp[1].find('_')==-1:
                     if xy_sp_tmp[1]=='D1' or xy_sp_tmp[1]=='D2':
                        xy_sp_tmp[1]=xy_sp_tmp[1]+"A_1"
                     else:
                        xy_sp_tmp[1]=xy_sp_tmp[1]+"_1"
                  elif xy_sp_tmp[1].find('D1_')==0 or xy_sp_tmp[1].find('D2_')==0:
                     xy_sp_tmp[1]=xy_sp_tmp[1][:2]+"A_"+xy_sp_tmp[1][3]
                     # print("~~~  ",xy_sp_tmp)
                     # xy_sp_tmp[1]=xy_sp_tmp[1]+"A_1"

                  for idr in range(len(dreg_name)):
                     if xy_sp_tmp[1]==dreg_name[idr]:
                        op_2=dreg_[idr]

               if xy_sp[1].find('+')>-1:
                  xy_val=op_1+op_2
                  # if (pat_seq_sp[ixy].find("TP1_1+D5")>-1): 
                  #    print('%X %X %X'%(xy_val,op_1,op_2),xy_sp_tmp[1],end='>')
                  #    print('[%8X %8X %8X %8X] [%8X %8X %8X %8X] '%(tp1_[1],tp1_[2],tp1_[3],tp1_[4],tp2_[1],tp2_[2],tp2_[3],tp2_[4]))
                  # print(xy_sp,op_1,op_2,xy_val)
               elif xy_sp[1].find('-')>-1:
                  xy_val=op_1-op_2
               elif xy_sp[1].find('"')>-1:
                  # print(xy_val,op_1,op_2,xy_sp_tmp[1])
                  xy_val=op_1^op_2
                  # print('%X %X %X'%(xy_val,op_1,op_2),xy_sp_tmp[1])
               elif xy_sp[1].find('*')>-1:
                  # print(xy_val,op_1,op_2,xy_sp_tmp[1])
                  # print(xy_sp,op_1,op_2,xy_val)
                  xy_val=op_1*op_2
               
               # print(xy_sp)
               # print(xy_sp,xy_sp_tmp,"%x"%(xy_val))
              
                  # print(dreg_)
               # print('%X %X %X'%(xy_val,op_1,op_2))
   #        A < B
            elif xy_sp[1][0]=='D':
               # print(xy_sp)
               if xy_sp[1]=='D1' or xy_sp[1]=='D2':
                  xy_sp[1]=xy_sp[1]+'A_1'
                  # print(xy_sp)
               elif xy_sp[1]=='D1_2' or xy_sp[1]=='D2_2':
                  xy_sp[1]=xy_sp[1][:2]+'A_2'
                  # print(xy_sp)
               elif xy_sp[1]=='D1_3' or xy_sp[1]=='D2_3':
                  xy_sp[1]=xy_sp[1][:2]+'A_3'
               elif xy_sp[1]=='D1_4' or xy_sp[1]=='D2_4':
                  xy_sp[1]=xy_sp[1][:2]+'A_4'
               elif xy_sp[1].find('_')==-1:
                  xy_sp[1]=xy_sp[1]+"_1"

               for idr in range(len(dreg_name)):
                  if xy_sp[1]==dreg_name[idr]:
                     xy_val=dreg_[idr]
                     # print(xy_sp," %5X "%(xy_val))
            elif xy_sp[1][0:3]=='TPH':
               if xy_sp[1]=='TP':
                  xy_sp[1]='TP1_1'
               if xy_sp[1]=='TP1' or xy_sp[1]=='TP2':
                  xy_sp[1]=xy_sp[1]+"_1"
               elif xy_sp[1]=='TPH':
                  xy_sp[1]='TPH1A_1'
               elif xy_sp[1]=='TPH1' or xy_sp[1]=='TPH2':
                  xy_sp[1]=xy_sp[1]+"A_1"
               elif xy_sp[1]=='TPH1_2' or xy_sp[1]=='TPH2_2':
                  xy_sp[1]=xy_sp[1][:4]+"A_2"
               elif xy_sp[1]=='TPH1_3' or xy_sp[1]=='TPH2_3':
                  xy_sp[1]=xy_sp[1][:4]+"A_3"
               elif xy_sp[1]=='TPH1_4' or xy_sp[1]=='TPH2_4':
                  xy_sp[1]=xy_sp[1][:4]+"A_4"
               elif xy_sp[1]=='TPH_1' or xy_sp[1]=='TPH_2' or xy_sp[1]=='TPH_3' or xy_sp[1]=='TPH_4':
                  xy_sp[1]=xy_sp[1][:3]+"1A_"+xy_sp[1][len(xy_sp[1])-1]


               # print(xy_sp)
                  # print(patline_seq[i])


               # xy_val=dreg_[0]   
               # if xy_sp[1].find("TPH")>-1:
               for itp in range(len(tpreg_name)):
                  if xy_sp[1]==tpreg_name[itp]:
                     xy_val=tpreg_[itp]

                     # print(xy_sp,xy_val)
               # print(xy_sp,xy_val,tpreg_)

            elif xy_sp[1][0]=='B':
               # print(xy_sp,pat_seq_sp)
               for ib in range(len(breg_name)):
                  if xy_sp[1].split('_')[0]==breg_name[ib]:
                     b_val_[int(xy_sp[0][len(xy_sp[0])-1])]=breg_[bn_cnt][ib]
                     b_val=breg_[bn_cnt][ib]
                     # print(bn_cnt,b_val_,b_val,xy_sp)
            elif xy_sp[1][0]=='N':
               for ib in range(len(nreg_name)):
                  if xy_sp[1].split('_')[0]==nreg_name[ib]:
                     n_val_[int(xy_sp[0][len(xy_sp[0])-1])]=nreg_[bn_cnt][ib]
                     n_val=nreg_[bn_cnt][ib]
            elif xy_sp[1][0]=='Y' or xy_sp[1][0]=='X':
               if len(xy_sp[1])==2: xy_sp[1]=xy_sp[1]+'_1'
               for iixy in range(len(xyreg_name)):
                  if xy_sp[1]==xyreg_name[iixy]:
                     xy_val=xyreg_[iixy]
            else:
               # print(xy_sp)
               xy_val=int(xy_sp[1])

            for iixy in range(len(xyreg_name)):
               if xy_sp[0]==xyreg_name[iixy]:
                  # if xy_sp[0]=="XC_1": print("---",xy_sp," %5X "%(xy_val))
                  xyreg_[iixy]=xy_val
            for idr in range(len(dreg_name)):
               if xy_sp[0]==dreg_name[idr]:                  
                  dreg_[idr]=xy_val
                  # print(xy_sp)
            for iit in range(len(tpreg_name)):
               if xy_sp[0]==tpreg_name[iit]:
                  tpreg_[iit]=xy_val

            if xy_sp[0] in ['TP1_1','TP1_2','TP1_3','TP1_4','TP2_1','TP2_2','TP2_3','TP2_4']:
               tp_idx=int(xy_sp[0][4])
               # print(xy_sp,tp_idx,xy_val)
               if  pat_seq_sp[ixy].find('TP<TP*2')>-1:
                  # print("%6x"%(tp1_[1]))
                  tp1_[1]=tp1_[1]*2
                  # print("%6x"%(tp1_[1]))
               elif  pat_seq_sp[ixy].find('TP2<TP2*2')>-1:
                  tp2_[1]=tp2_[1]*2
               elif  pat_seq_sp[ixy].find('TP1_2<TP1_2*2')>-1:
                  tp1_[2]=tp1_[2]*2
               elif  pat_seq_sp[ixy].find('TP2_2<TP2_2*2')>-1:
                  tp2_[2]=tp2_[2]*2
               elif  pat_seq_sp[ixy].find('TP1_3<TP1_3*2')>-1:
                  tp1_[3]=tp1_[3]*2
               elif  pat_seq_sp[ixy].find('TP2_3<TP2_3*2')>-1:
                  tp2_[3]=tp2_[3]*2
               elif  pat_seq_sp[ixy].find('TP1_4<TP1_4*2')>-1:
                  tp1_[4]=tp1_[4]*2
               elif  pat_seq_sp[ixy].find('TP2_4<TP2_4*2')>-1:
                  tp2_[4]=tp2_[4]*2

               elif  pat_seq_sp[ixy]=='TP<TP':
                  tp1_[1]=tp1_[1]
               elif  pat_seq_sp[ixy]=='TP2<TP2':
                  tp2_[1]=tp2_[1]
               elif  pat_seq_sp[ixy]=='TP1_2<TP1_2':
                  tp1_[2]=tp1_[2]
               elif  pat_seq_sp[ixy]=='TP2_2<TP2_2':
                  tp2_[2]=tp2_[2]
               elif  pat_seq_sp[ixy]=='TP1_3<TP1_3':
                  tp1_[3]=tp1_[3]
               elif  pat_seq_sp[ixy]=='TP2_3<TP2_3':
                  tp2_[3]=tp2_[3]
               elif  pat_seq_sp[ixy]=='TP1_4<TP1_4':
                  tp1_[4]=tp1_[4]
               elif  pat_seq_sp[ixy]=='TP2_4<TP2_4':
                  tp2_[4]=tp2_[4]

               elif  pat_seq_sp[ixy].find('TP</TP')>-1:
                  tp1_[1]=tp1_[1]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP2</TP2')>-1:
                  tp2_[1]=tp2_[1]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP1_2</TP1_2')>-1:
                  tp1_[2]=tp1_[2]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP2_2</TP2_2')>-1:
                  tp2_[2]=tp2_[2]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP1_3</TP1_3')>-1:
                  tp1_[3]=tp1_[3]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP2_3</TP2_3')>-1:
                  tp2_[3]=tp2_[3]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP1_4</TP1_4')>-1:
                  tp1_[4]=tp1_[4]^(0xffff)
               elif  pat_seq_sp[ixy].find('TP2_4</TP2_4')>-1:
                  tp2_[4]=tp2_[4]^(0xffff)



               elif xy_sp[0][:3]=='TP1':
                  tp1_[tp_idx]=xy_val
               elif xy_sp[0][:3]=='TP2':
                  tp2_[tp_idx]=xy_val
               else:
                  tp1_[tp_idx+10]=xy_val



               # print(xy_sp[0],end=" : ")
               # print('[%8X %8X %8X %8X] [%8X %8X %8X %8X] '%(tp1_[1],tp1_[2],tp1_[3],tp1_[4],tp2_[1],tp2_[2],tp2_[3],tp2_[4]))
               # print(tp1_,tp2_)
            # print(xy_sp,xreg_,yreg_,xy_val)
            # if xy_sp[0]=='YC_3': print(dreg_)

            # if (pat_seq_sp[ixy].find("TP_4<")>-1): 
            #    print("  ~~~  ",pat_seq_sp[ixy],end= ' : ')            
            #    print('[%8X %8X %8X %8X] [%8X %8X %8X %8X] '%(tp1_[1],tp1_[2],tp1_[3],tp1_[4],tp2_[1],tp2_[2],tp2_[3],tp2_[4]))



      for ixy in range(len(xyreg_name)):
         

         if x_tmp==xyreg_name[ixy]:
            x_addr=xyreg_[ixy]
         if y_tmp==xyreg_name[ixy]:
            y_addr=xyreg_[ixy]
            # if y_tmp=="YS_2":
            #    print(y_addr,y_tmp)





      tp1f=0
      tp2f=0
      if 'W' in pat_seq_sp or 'R' in pat_seq_sp:
         tp1f=tp1
         tp2f=tp2
         if '/D2' in pat_seq_sp:
            tp2f=tp2^65535
         if '/D' in pat_seq_sp:
            tp1f=tp1^65535
         # print(pat_seq_sp)

         # print('%5s %5s %5X %5X %4X %4X'%(x_tmp,y_tmp,x_addr,y_addr,tp1f,tp2f),end='')  #~~
      # else:
         # print('%5s %5s %5X %5X %4X %4X'%(x_tmp,y_tmp,x_addr,y_addr,0,0),end='') #~~

         # print('%5s %5s %5X %5X %4X %4X'%(x_tmp,y_tmp,x_addr,y_addr,0,0),xyreg_,dreg_,end='')

   # print('%5d %5d %5X %10s %2d '%(i,icnt_seq[i],pccnt_seq[i],label_seq[i],lineway_seq[i]),end=' : ')
   #    print('%100s'%(patline_seq[i]),end=' : ')

      # print('%3s %3s %3s %3s %3s %3s %3s %3s %3s %3s %4s %4s %4s'%(P_CKT,P_R0_CS,P_R1_CS,P_CA[0],P_CA[1],P_CA[2],P_CA[3],P_CA[4],P_CA[5],P_CA[6],P_WCKT,P_RDQS0T,P_RDQS1T),end=" ")


      if dinv==1 and 'R' in pat_seq_sp:
         # print(bin(tp1f & 0xffff),bin(tp1f & 0xffff))
         tp1f_tmp=bin(tp1f & 0xffff)
         tp2f_tmp=bin(tp2f & 0xffff)
         dmi0_=''
         dmi1_=''

         if len(tp1f_tmp)<10:
            tp1f_tmp_b1='0'*8
            tp1f_tmp_b0='0'*(10-len(tp1f_tmp))+tp1f_tmp[2:]
         elif len(tp1f_tmp)<20:
            tp1f_tmp_b1='0'*(8-len(tp1f_tmp[2:len(tp1f_tmp)-8]))+tp1f_tmp[2:len(tp1f_tmp)-8]
            tp1f_tmp_b0=tp1f_tmp[len(tp1f_tmp)-8:]

         if len(tp2f_tmp)<10:
            tp2f_tmp_b1='0'*8
            tp2f_tmp_b0='0'*(10-len(tp2f_tmp))+tp2f_tmp[2:]
         elif len(tp2f_tmp)<20:
            tp2f_tmp_b1='0'*(8-len(tp2f_tmp[2:len(tp2f_tmp)-8]))+tp2f_tmp[2:len(tp2f_tmp)-8]
            tp2f_tmp_b0=tp2f_tmp[len(tp2f_tmp)-8:]

         if tp1f_tmp_b0.count('1')>4:
            tp_tmp_=''
            for ii in range(8):
               if tp1f_tmp_b0[ii]=='1':   tp_tmp_=tp_tmp_+'0'
               elif tp1f_tmp_b0[ii]=='0': tp_tmp_=tp_tmp_+'1'
            tp1f_tmp_b0=tp_tmp_
            dmi0_=dmi0_+"1"
         else:
            dmi0_=dmi0_+"0"
         if tp1f_tmp_b1.count('1')>4:
            tp_tmp_=''
            for ii in range(8):
               if tp1f_tmp_b1[ii]=='1':   tp_tmp_=tp_tmp_+'0'
               elif tp1f_tmp_b1[ii]=='0': tp_tmp_=tp_tmp_+'1'
            tp1f_tmp_b1=tp_tmp_
            dmi1_=dmi1_+"1"
         else:
            dmi1_=dmi1_+"0"

         if tp2f_tmp_b0.count('1')>4:
            tp_tmp_=''
            for ii in range(8):
               if tp2f_tmp_b0[ii]=='1':   tp_tmp_=tp_tmp_+'0'
               elif tp2f_tmp_b0[ii]=='0': tp_tmp_=tp_tmp_+'1'
            tp2f_tmp_b0=tp_tmp_
            dmi0_=dmi0_+"1_"
         else:
            dmi0_=dmi0_+"0_"
         if tp2f_tmp_b1.count('1')>4:
            tp_tmp_=''
            for ii in range(8):
               if tp2f_tmp_b1[ii]=='1':   tp_tmp_=tp_tmp_+'0'
               elif tp2f_tmp_b1[ii]=='0': tp_tmp_=tp_tmp_+'1'
            tp2f_tmp_b1=tp_tmp_
            dmi1_=dmi1_+"1_"
         else:
            dmi1_=dmi1_+"0_"

         tp1f_=int(tp1f_tmp_b0,2)+int(tp1f_tmp_b1,2)*0x100
         tp2f_=int(tp2f_tmp_b0,2)+int(tp2f_tmp_b1,2)*0x100


         # print('0x%04X 0x%04X - 0x%04X 0x%04X'%(tp1f_tmp_b0 & 0xffff,tp1f_tmp_b1 & 0xffff,tp2f_tmp_b0 & 0xffff,tp2f_tmp_b1 & 0xffff))
         # print(tp1f_tmp_b1,tp1f_tmp_b0,tp2f_tmp_b1,tp2f_tmp_b0,' 0x%04X 0x%04X'%(tp1f_ & 0xffff,tp2f_ & 0xffff))


				# if tp1f_tmp.count('1')>4:
         patline_f0[i]=patline_f0[i][:len(patline_f0[i])-8]+format('%s %s 0x%04X 0x%04X'%(dmi0_,dmi1_,tp1f_ & 0xffff,tp2f_ & 0xffff))


         # if i<20:
         #    print(patline_f0[i])
            # print(pat_seq_sp)
      else:
         patline_f0[i]=patline_f0[i]+format('0x%04X 0x%04X'%(tp1f & 0xffff,tp2f & 0xffff))
      patline_f0.append([''])
      # print('')

   pf_cnt=i

   hsc_f_name=''
   if compile_opt1=='A': hsc_f_name='E'
   elif compile_opt1=='B': hsc_f_name='O'

   hsc_f_name=hsc_f_name+compile_opt2

   fwr1 = open(patn_lst[10].strip('"')+hsc_f_name+'_t5511.txt',"w")
   fwr1.write('IDX   LABEL PC UI CLKT  CS0   CS1   CA WCKT  RDQST DMI0  DMI1  DATAe DATAo \n')
   for i in range(pf_cnt):
      # print(patline_f0[i])
      fwr1.write(patline_f0[i])
      fwr1.write('\n')
   fwr1.close

