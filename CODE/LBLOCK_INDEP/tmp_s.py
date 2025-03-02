import config.config as config
Sbox=config.Sbox

"""    array[0..15, 1..2] of int: sbox_table0 = 
        array2d(0..15, 1..2, [
            0, 12,  1, 6,  2, 9,  3, 0,
            4, 1,   5, 10, 6, 2,  7, 11,
            8, 3,   9, 8,  10, 5, 11, 13,
            12, 4,  13, 14, 14, 7, 15, 15
        ]);"""
def print_S(i):
    str1="array[0..15, 1..2] of int: sbox_table"+str(i)+" =\n"
    str1+="        array2d(0..15, 1..2, [\n       "
    si = Sbox[i]
    for j in range(15):
        str1+=str(j)+" , "+str(si[j])+" ,  "
    str1+=str(15)+" , "+str(si[15])+"\n"
    str1+="         ]);\n"
    return str1
sss=""
for i in range(8):
    sss+=print_S(i)

print(sss)
