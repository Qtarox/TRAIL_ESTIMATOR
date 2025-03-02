# This is the code for linear layer of the Lblock
#we start from the input of Sbox

from TOOL.Visual import show_Lblock_equ
import numpy as np
import config.config as config
Pt=[1,3,0,2,5,7,4,6,10,11,12,13,14,15,8,9]
round_num=config.round_num
file_path=config.file_path
L_equ=[[1,14],[3,15],[0,8],[2,9],[5,10],[7,11],[4,12],[6,13]]
def gen_linear_mat(round_num):
    # size of mat 64*round_num+1
    # for each round, we begin from the input of Sbox
    # for each round, we have 16 x_i, 8 y_i and 8 keys k_i, the first 24*round is for x and y only
    # each round have 16 equations
    lmat=np.zeros((16*round_num,32*(round_num+1)),dtype=int)
    for i in range(np.shape(lmat)[0]):
        r=i//16
        equ_ind=i%16
        if(equ_ind<8):#the left to right part
            x_r=L_equ[equ_ind][1]+24*(r)
            x_r1=equ_ind+24*(r+1)
            y_r=L_equ[equ_ind][0]+24*r+16
            k=24*(round_num+1)+r*8+equ_ind
            lmat[i][x_r]=1
            lmat[i][x_r1]=1
            lmat[i][y_r]=1
            lmat[i][k]=1
        else:
            x_r1=equ_ind+24*(r+1)
            x_r=equ_ind-8+24*r
            k=equ_ind-8+24*(round_num+1)+r*8
            lmat[i][x_r1]=1
            lmat[i][x_r]=1
            lmat[i][k]=1

    return lmat

def  gen_nl_mat(round_num):
    n_mat=np.zeros((8*round_num,32*(round_num+1)),dtype=int)
    for i in range(np.shape(n_mat)[0]):
        r=i//8
        equ_ind=i%8
        x_r=equ_ind+24*r
        y_r=equ_ind+24*r+16
        n_mat[i][x_r]=1
        n_mat[i][y_r]=1
    return n_mat

def assemble_ln_mat(l_mat,n_mat):
    result = np.vstack((l_mat,n_mat))
    return result

def GEN_L_MAT(round_num):
    L_M=gen_linear_mat(round_num)
    N_M=gen_nl_mat(round_num)
    res=assemble_ln_mat(L_M,N_M)
    np.save(file_path+"GLOBAL_MAT.npy",res)
    return res
if __name__=="__main__":
    Mat=GEN_L_MAT(round_num)
    # show_Lblock_equ(Mat)


