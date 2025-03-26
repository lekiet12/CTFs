import numpy as np
A = np.array([[88, -17, 19, -57],
              [45, -9, 10, -29],
              [-56, 11, -12, 36],
              [-40, 8, -9, 26]])

if np.linalg.det(A) == 0:
    print("Ma trận không khả nghịch!")
    exit()
B = np.linalg.inv(A)
B = np.round(B, decimals=0).astype(int)  
flag = [0]*16

for j in range(4):
    for k in range(4):
        flag[j*4+k] = int(B[j][k]) + 65 + k * j

for i in range(0,len(flag),4):
    print(bytes(flag[i:i+4]).decode(), end='-')
# HTB{t00_mUcH_x0R!!}
# BFCF-EJJL-CKKL-BLJQ