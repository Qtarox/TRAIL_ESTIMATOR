# c1={'112': 256, '96': 3072, '80': 1792, '64': 4608, '48': 1792, '32': 3072, '128': 768, '16': 256}
# c2={'2': 232, '4': 48, '6': 8, '3': 32, '1': 224}
# c3={'2':4, '1':8}
c1={'144': 29915, '108': 61389, '72': 96324, '36': 77126, '12': 340553, '18': 226358, '6': 254157, '24': 117366, '30': 16780, '1': 207424, '3': 206690, '4': 112992, '2': 298144, '5': 33440, '93': 1, '13': 1, '28': 1} #16 

c2= {'6848': 32, '6000': 32, '6288': 32, '5440': 32, '5664': 32, '4752': 32, '4464': 32, '3552': 32}#8

res={}
for k1 in c1:
    for k2 in c2:
        K=int(k1)*int(k2)
        num=c1[k1]*c2[k2]
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