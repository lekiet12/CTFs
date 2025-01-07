enc=[36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 125, 103, 97, 108, 102, 32, 101, 107, 97, 102, 32, 97, 32, 116, 111, 110, 32, 116, 115, 117, 106, 32, 101, 114, 101, 104, 32, 103, 110, 105, 104, 116, 32, 116, 111, 110, 123, 67, 83, 67, 75]
enc=enc[::-1]
key=[194, 61, 41, 207, 308, 222, 312, 272, 204, 117, 317, 340, 242, 71, 283, 181, 135, 280, 182, 167, 260, 1, 260, 308, 4, 296, 345, 240, 24, 247, 25, 67, 269, 0, 225, 140, 173, 354, 339, 235, 229, 218, 160, 216, 76, 104, 92, 160, 52, 200, 62, 102, 336]
flag=[(i^j) for i,j in zip(enc,key)]
possible_values=[]
for k in range(len(flag)):
    value=[]
    for char in range(0xff):
        x = char 
        array=[]
        for j in range(8):
            array.append(x % 8)
            x = x // 8
        array = array[::-1]
        v2 = 0
        i=0
        for j in range(8):
            v4 = array[i]
            v2 = v2+v4*pow(10,8-j-1)
            i+=1
        if (v2) == flag[k]:
            flag[k]=char
            value.append(char)
            # break
    possible_values.append(value)
print(possible_values)
from itertools import product
import sys
import subprocess
n = 1
for combination in product(*possible_values):
    flag=combination
    flag=flag[::-1]
    flag=[bin(i)[2:].zfill(8) for i in flag]
    flag="".join(flag)
    flag=[int(i,10) for i in flag]
    flag=flag[::-1]
    data = open("out.bin",'rb').read()
    data=[i for i in data]
    for i in range(0,424,2):
        flag[i]^=data[i*4+4]
        flag[i+1]^=data[i*4]
        flag[i],flag[i+1]=flag[i+1],flag[i]
    flag=flag[::-1]
    x=("".join(str(i) for i in flag))
    out=""
    for i in range(0,len(x),8):
        y = int(x[i:i+8],2)
        out+=chr(y)
    if "KCSC{" in out:
        print(out)

# KCSC{3V3rY_r3v3R53_En91n33r_kN0w_H0W_TH3_5t4ck_w0Rkk}