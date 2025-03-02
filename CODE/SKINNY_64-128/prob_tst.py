import config.config as config
S=config.Sbox
Y=[0 for i in range(16)]
for x1 in range(16):
    for x2 in range(16):
        for x3 in range(16):
            for x4 in range(16):
                for x5 in range(16):
                    for x6 in range(16):
                        if(x1^x2^x3^x4^x5^x6==0):
                            Y[S[x1]^S[x2]^S[x3]^S[x4]^S[x5]^S[x6]]+=1
print(Y)