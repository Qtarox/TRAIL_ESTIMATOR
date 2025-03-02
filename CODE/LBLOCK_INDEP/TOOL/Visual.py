import numpy as np
import config.config as config
from TOOL.BASIC_OP import *
round_num=config.round_num
def show_Lblock_equ(lmat):
    for i in range(np.shape(lmat)[0]):
        if((lmat[i].sum())==2):# is nonlinear
            l_tmp=""
            for j in range(24*(round_num+1)):
                rn=j//24
                ind=j%24
                if(lmat[i][j]==1 and is_active(j)):
                    if(ind<16):
                        l_tmp=l_tmp+" + S([x^"+str(int(rn))+"_"+str(ind)+"])"
                    else:
                        l_tmp=l_tmp+" + [y^"+str(int(rn))+"_"+str((ind-16))+ "]"
                elif(lmat[i][j]==1):
                    if(ind<16):
                        l_tmp=l_tmp+" + S(x^"+str(int(rn))+"_"+str(ind)+")"
                    else:
                        l_tmp=l_tmp+" + y^"+str(int(rn))+"_"+str((ind-16))+""
            l_tmp=l_tmp+'= 0 '
            print(l_tmp[2:])
        else:
            l_tmp=""
            for j in range(24*(round_num+1)):
                rn=j//24
                ind=j%24
                if(lmat[i][j]==1 and is_active(j)):
                    if(ind<16):
                        l_tmp=l_tmp+" + [x^"+str(int(rn))+"_"+str(ind)+"]"
                    else:
                        l_tmp=l_tmp+" + [y^"+str(int(rn))+"_"+str((ind-16))+ "]"
                elif(lmat[i][j]==1):
                    if(ind<16):
                        l_tmp=l_tmp+" + x^"+str(int(rn))+"_"+str(ind)+""
                    else:
                        l_tmp=l_tmp+" + y^"+str(int(rn))+"_"+str((ind-16))+""
            for j in range(24*(round_num+1),32*(round_num+1)):
                if(lmat[i][j]==1):
                    key_num=j-24*(round_num+1)
                    k_r=key_num//8
                    k_ind=key_num%8
                    l_tmp+=" + k_"+str(k_r)+"_"+str(k_ind)

            l_tmp=l_tmp+'= 0 '
            print(l_tmp[2:])

def show_Lblock_equ1(mat):
    #the column size is 32*(round_num+1)
    for i in range(np.shape(mat)[0]):
        l_str=""
        for j in range(24*(round_num+1)):
            if(mat[i][j]==1):
                r=j//24
                ind=j%24
                if(is_active(j)):
                    if(ind<16):# is x
                        l_str+=" + [x_"+str(r)+"_"+str(ind)+"]"
                    else:
                        l_str+=" + [y_"+str(r)+"_"+str(ind-16)+"]"
                else:
                    if(ind<16):# is x
                        l_str+=" + x_"+str(r)+"_"+str(ind)
                    else:
                        l_str+=" + y_"+str(r)+"_"+str(ind-16)

        for j in range(24*(round_num+1),32*(round_num+1)):
            if(mat[i][j]==1):
                key_num=j-24*(round_num+1)
                k_r=key_num//8
                k_ind=key_num%8
                l_str+=" + k_"+str(k_r)+"_"+str(k_ind)
        l_str+=" = 0"
        print(l_str)

def show_cons_set(gmat,lst):
    mat=gmat[lst,:]
    show_Lblock_equ(mat)