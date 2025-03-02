c1={'112': 256, '96': 3072, '80': 1792, '64': 4608, '48': 1792, '32': 3072, '128': 768, '16': 256}
c2={'2': 232, '4': 48, '6': 8, '3': 32, '1': 224}
c3={'2':4, '1':8}
res={}
for k1 in c1:
    for k2 in c2:
        for k3 in c3:
            K=int(k1)*int(k2)*int(k3) 
            num=c1[k1]*c2[k2]*c3[k3]
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
    R[(int(int(k)/16))]=res[k]/sum*100
sorted_dict = {key: R[key] for key in sorted(R)}
print(sorted_dict)
# s=0
# for key in sorted_dict:
#     if(key<2 and key>=1):
#         s+=sorted_dict[key]

# print(s)

# print(R)