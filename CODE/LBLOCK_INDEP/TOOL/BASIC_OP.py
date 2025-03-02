import numpy as np
import json
import sys
import os
import config.config as config
Sbox_set= config.Sbox
round_num=config.round_num

np.set_printoptions(linewidth=400)


def corr_ind(ind_num):
    rn=ind_num//32
    j=ind_num%32
    if(j<16): #is an ind of x
        x_rn=rn+1
        y_rn=x_rn
        y_ind=j+16
        y_num=y_rn*32+y_ind
        return y_num
    else: #ind of y
        y_rn=rn
        x_rn=y_rn
        x_ind=j-16
        x_num=(x_rn-1)*32+x_ind
        return x_num
       
def list_xor(l1,l2):#two possible set xor
    res=[]
    for i in l1:
        for j in l2:
            res.append(i^j)
    dic_tmp={}
    res=sorted(res)
    for i in res:
        if(i in dic_tmp):
            dic_tmp[i]+=1
        else:
            dic_tmp[i]=1
    flg=False
    gcd_t=256
    for i in range(16):
        if(i not in dic_tmp or dic_tmp[i]==0):
            continue
        elif(flg==False):
            gcd_t=dic_tmp[i]
        else:
            gcd_t=np.gcd(gcd_t,dic_tmp[i])
        if(gcd_t==1):
            break
    if(gcd_t==1):
        return res
    res=[]
    for i in range(16):
        if(i not in dic_tmp):
            continue
        t=(dic_tmp[i]//gcd_t)
        for j in range(t):
            res.append(i)
    
    return res

# def X_DDT(xddt):
#     for input in range(16):
#         for output in range(16):
#             cnt=0
#             for x in range(16):
#                 x1=x
#                 x2=x^input
#                 y1=Sbox[x1]
#                 y2=Sbox[x2]
#                 if(y1^y2==output and input!=0):
#                     xddt[input][output][cnt]=x
#                     cnt=cnt+1
#     return xddt

def xddt_list(input,output,Sbox):
    res=[]
    for x in range(16):
        x1=x
        x2=x^input
        y1=Sbox[x1]
        y2=Sbox[x2]
        if(y1^y2==output and input!=0):
            res.append(x)
            #print("XDDT("+str(input)+", "+str(output)+")="+str(tmp))
    return res
    

def yddt_list(input,output,Sbox):
    res=[]
    for x in range(16):
        x1=x
        x2=x^input
        y1=Sbox[x1]
        y2=Sbox[x2]
        if(y1^y2==output and input!=0):
            res.append(y1)
    return res


def corr_ind(ind_num):
    rn=ind_num//24
    j=ind_num%24
    if(j<16): #is an ind of x
        x_rn=rn
        y_rn=x_rn
        y_ind=j+16
        y_num=y_rn*24+y_ind
        return y_num
    else: #ind of y
        y_rn=rn
        x_rn=y_rn
        x_ind=j-16
        x_num=(x_rn)*24+x_ind
        return x_num

def create_folder(pth):
# Create the new folder if it doesn't already exist
    if not os.path.exists(pth):
        os.makedirs(pth)
    # Verify if the folder has been created
    os.path.exists(pth)
def creat_dic(file_path,round):
    x_dic={}
    y_dic={}
    for r in range(len(round)):
        for x_ind in range(8):
            x_index=7-x_ind
            if(round[r][0][x_ind]==0):
                continue
            k_tmp='x_'+str(r)+'_'+str(x_index)
            y_tmp='y_'+str(r)+'_'+str(x_index)
            l_x=xddt_list(round[r][0][x_ind],round[r][1][x_ind],Sbox_set[x_index])
            l_y=yddt_list(round[r][0][x_ind],round[r][1][x_ind],Sbox_set[x_index])
            x_dic[k_tmp]=l_x.copy()
            y_dic[y_tmp]=l_y.copy()
    original_stdout = sys.stdout

    # Specify the file name where you want to save the output
    file_x= file_path+"act_x.json"

        # Open the file in write mode, this will create the file if it doesn't exist
    with open(file_x, 'w') as json_file1:
        # Redirect the standard output to the file
        json.dump(x_dic, json_file1)
    
    file_y= file_path+"act_y.json"

        # Open the file in write mode, this will create the file if it doesn't exist
    with open(file_y, 'w') as json_file2:
        # Redirect the standard output to the file
        json.dump(y_dic, json_file2)

def load_dic(file_path):
    if os.path.exists(file_path):
        f = open(file_path, encoding='utf-8')
        content = f.read()
        user_dic = json.loads(content)
        return user_dic
    
x_dic=load_dic(config.file_path+"act_x.json")
y_dic=load_dic(config.file_path+"act_y.json")
def is_active(num,x_dic=x_dic,y_dic=y_dic):
    if(num>24*(round_num+1)):
        return False
    rn=num//24
    ind=num%24
    if(ind<16):#is x
        x_rn=rn
        if(("x_"+str(x_rn)+"_"+str(ind)) in x_dic):
            # print("x_"+str(x_rn)+"_"+str(ind))
            return True
        else:
            return False
    else:
        y_rn=rn
        y_ind=ind-16
        if(("y_"+str(y_rn)+"_"+str(y_ind)) in y_dic):
            # print("y_"+str(y_rn)+"_"+str(y_ind))
            return True
        else:
            return False
def active_list(num,x_dic=x_dic,y_dic=y_dic):
    rn=num//24
    ind=num%24
    if(ind<16):#is x
        x_rn=rn
        if(("x_"+str(x_rn)+"_"+str(ind)) in x_dic):
            # print("x_"+str(x_rn)+"_"+str(ind))
            return x_dic["x_"+str(x_rn)+"_"+str(ind)]
        else:
            return False
    else:
        y_rn=rn
        y_ind=ind-16
        if(("y_"+str(y_rn)+"_"+str(y_ind)) in y_dic):
            # print("y_"+str(y_rn)+"_"+str(y_ind))
            return y_dic["y_"+str(y_rn)+"_"+str(y_ind)]
        else:
            return False  
def get_inv(S):
    l=len(S)
    lst=[0 for i in range(l)]
    # print(lst)
    for i in range(l):
        lst[S[i]]=i
    return lst.copy()

def get_S(lst,S):
    res=[]
    for i in lst:
        res.append(S[i])
    return res

if __name__=="__main__":
    S4=Sbox_set[4]
    x34=[8,11,12,15]
    x36=[0,2,9,11]
    x33=[11,10,14,15]
    x_04=[9,10,13,14]
    y24=[5,0,1,4]
    x36=[11,14]
    print(list_xor(y24,x36))
    print(list_xor(x_04,x_04))
    Y=get_S(x33,S4)
    print("S(X): ",Y)
    Y=[8,5,7,2]
    x31=[0,3,4,7]

    l2=(list_xor(x31,Y))
    print(l2)