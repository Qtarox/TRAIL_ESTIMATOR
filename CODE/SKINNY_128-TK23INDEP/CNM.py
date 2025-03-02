import config.config as config
Sbox=config.Sbox


din=0x32
dout=0x92
res=[]
for i in range(256):
    
    if(Sbox[i]^Sbox[i^din]==dout):
        print(i)
        res.append(i)

print(res)
    