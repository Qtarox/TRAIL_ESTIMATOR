F=[0, 8, 1, 9, 2, 10, 3, 11, 12, 4, 13, 5, 14, 6, 15,7]
def n_bit(x,n):
    return ((x>>n)&1)
# for i in range(15):
    # F.append((n_bit(i,0)^n_bit(i,3))*8+n_bit(i,3)*4+n_bit(i,2)*2+n_bit(i,1))
res=[i for i in range(16)]
for i in range(15):
    for j in range(16):
        res[j]=F[res[j]]
    print("F"+str(i+1)+"=",res)

