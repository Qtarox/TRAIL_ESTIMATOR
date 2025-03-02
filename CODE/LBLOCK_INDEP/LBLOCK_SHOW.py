import config.config as config
import numpy as np
from TOOL.Visual import show_Lblock_equ
from RES_CONS import *
file_pth=config.file_path
round_num=config.round_num
# RESDC2=[[107, 117], [61, 71, 95, 97],  [62, 64, 88, 98], [28, 38, 44, 54, 276]]
RESDC0=[[173, 183], [172, 182]]
RESDC1=[[9, 19, 26, 36, 44, 45, 54, 55, 90, 101, 108], [46, 48], [29, 39], [28, 38]]
res2=[[121, 127, 133, 135, 142, 143, 148, 149, 262, 263, 269, 271], [122, 128, 137, 151, 152, 158, 164, 166, 257, 270]]
RESDC3=[[12, 22, 28, 38, 76]]
RESDC33=[[12, 22, 28, 38, 76], [12, 22, 28, 38, 76], [68], [77], [79], [84], [85], [86], [89], [92], [94]]
def show_cons_set(gmat,lst):
    mat=gmat[lst,:]
    show_Lblock_equ(mat)
if __name__=="__main__":
    gmat=np.load(file_pth+"GLOBAL_MAT.npy")
    print(np.shape(gmat))
    print("round_num: ",round_num)
    cnt=0
    for i in RES_DC2_SOL:
        lst=[] 
               
        for r in i:
            if(r>64*round_num):
                pass
            else:
                lst.append(r)
        print("the "+str(cnt)+" equation set is:")
        show_cons_set(gmat,lst)
        cnt=cnt+1