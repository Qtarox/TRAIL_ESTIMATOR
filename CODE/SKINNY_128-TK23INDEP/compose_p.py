# c1={'112': 256, '96': 3072, '80': 1792, '64': 4608, '48': 1792, '32': 3072, '128': 768, '16': 256}
# c2={'2': 232, '4': 48, '6': 8, '3': 32, '1': 224}
# c3={'2':4, '1':8}
c1={'1': 192, '2': 32}
c2= {'6': 64, '1': 128}
c3= {'6': 64, '1': 128}
c4= {'2': 32, '1': 192}
c5= {'1': 112, '2': 8}
c6= {'6': 64, '1': 128} 
c7={'1': 2, '2': 1}

res={}
for k1 in c1:
    for k2 in c2:
        for k3 in c3:
            for k4 in c4:
                for k5 in c5:
                    for k6 in c6:
                        for k7 in c7:
                            K=int(k1)*int(k2)*int(k3)*int(k4)*int(k5)*int(k6)*int(k7) 
                            num=c1[k1]*c2[k2]*c3[k3]*c4[k4]*c5[k5]*c6[k6]*c7[k7]
                            if(str(K) in res):
                                res[str(K)]+=num
                            else:
                                res[str(K)]=num

print(res)
sum=0
for k in res:
    sum+=res[k]
print(sum)
R={}
for k in res:
    R[(int(int(k)/1))]=res[k]/sum*100
sorted_dict = {key: R[key] for key in sorted(R)}
print(sorted_dict)
s=0
# for key in sorted_dict:
#     if(key<2 and key>=1):
#         s+=sorted_dict[key]

# print(s)

# print(R)