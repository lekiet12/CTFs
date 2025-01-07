def main_evaluate_polynomial(flag,array,base):
    for i in range(2):
        x = 1
        for j in range(i+1):
            x = x*array[i]
        flag+=base*(x)
    return flag 

import struct
replica_1 = open("replica_1_challenge.bin",'rb').read()
replica_2 = open("replica_2_challenge.bin",'rb').read()
replica_3 = open("replica_3_challenge.bin",'rb').read()

# replica_1 = open("replica_1_file",'rb').read()
# replica_2 = open("replica_2_file",'rb').read()
# replica_3 = open("replica_3_file",'rb').read()
array_1 = []
array_2 = []
array_3 = []
for i in range(0,len(replica_1),8):
    array_1.append(struct.unpack('<Q', replica_1[i:i+8])[0])
    array_2.append(struct.unpack('<Q', replica_2[i:i+8])[0])
    array_3.append(struct.unpack('<Q', replica_3[i:i+8])[0])


result = [0]*len(array_1)
from z3 import *
for index in range(len(array_1)):
    flag = [BitVec(f"x{i}",32) for i in range(3)]
    s=Solver()

    for i in range(3):
        s.add(flag[i]>=0)
        s.add(flag[i]<=0xff)

    s.add(array_1[index] == main_evaluate_polynomial(flag[0],[flag[1],flag[2]],1))
    s.add(array_2[index] == main_evaluate_polynomial(flag[0],[flag[1],flag[2]],2))
    s.add(array_3[index] == main_evaluate_polynomial(flag[0],[flag[1],flag[2]],3))

    if s.check() == sat:
        m = s.model()
        value = [m.eval(flag[i]).as_long() for i in range(3)]
        print((value[0]),end=" ")
        result[index] = value[0]
with open("flag_bin",'wb') as f:
    f.write(bytearray(result))

# gctf{7h15_f1l3_w45_5h4m1r’s_5ecr375h4r3d}