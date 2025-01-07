from z3 import *
def rol(a, b):
    return ((a << b) | ((a >> (32 - b))) & ((1 << b) - 1)) & 0xffffffff
cipher = [0x22, 0xe, 0xed, 0xcb, 0x22, 0x4, 0x82, 0x9, 0x33, 0x82, 0x75, 0xc1, 0xf0, 0x40, 0x72, 0x34, 0x3d, 0x4, 0xae, 0xa9, 0x87, 0x3, 0xc2, 0x1e, 0x67, 0xd8, 0x79, 0x2f, 0xa3, 0xf6, 0x48, 0x7, 0x8e, 0xb8, 0x1d, 0x8b, 0xb0, 0x10, 0xc9, 0x87, 0x64, 0x2e, 0xa1, 0xf6, 0x3f, 0xbd, 0x15, 0xa3]
array = []
for i in range(0,len(cipher),4):
    array.append(cipher[i+3]<<24|cipher[i+2]<<16|cipher[i+1]<<8|cipher[i])
cipher = array.copy()
key = [0x00000058, 0x00000038, 0x000003C0, 0x000000D0, 0x00000120, 0x00000014, 0x00000060, 0x0000002C, 0x00000380,
       0x000000F0, 0x000001A0, 0x00000012]

v33=len(key)-1

while v33>=0:
    s = Solver()
    flag = [BitVec(f"flag[{i}]", 32) for i in range(12)]
    v2 = flag[8]
    v3 = flag[0]
    v4 = flag[1]
    v5 = flag[5]
    v6 = flag[9]
    v7 = flag[2]
    v35 = flag[0]
    v8 = flag[4]
    v9 = flag[6]
    v10 = flag[3]
    v37 = flag[4]
    v11 = flag[10]
    v12 = flag[7]
    v34 = flag[10]
    v36 = flag[11]


    v13 = flag[7] ^ flag[3]
    v14 = rol(flag[4] ^ flag[8] ^ flag[0], 5) ^ rol(flag[4] ^ flag[8] ^ flag[0], 14)
    v15 = flag[9] ^ flag[5] ^ flag[1]
    v16 = v14 ^ flag[1]
    v17 = v14 ^ flag[5]
    v18 = rol(v15, 5) ^ rol(v15, 14)
    v19 = flag[6] ^ flag[2]
    v20 = v18 ^ flag[2]
    v21 = rol(flag[10] ^ v19, 5) ^ rol(flag[10] ^ v19, 14)
    v22 = v21 ^ flag[3]
    v23 = v21 ^ flag[7]
    v24 = rol(flag[11] ^ v13, 5) ^ rol(flag[11] ^ v13, 14)
    v25 = v24 ^ flag[4]
    v26 = v18 ^ flag[6]
    v27 = v24 ^ key[v33] ^ flag[0]
    v28 = rol(flag[8] ^ v24, 11)
    v29 = rol(flag[9] ^ v14, 11)
    v30 = rol(flag[10] ^ v18, 11)
    v31 = rol(flag[11] ^ v21, 11)

    v33 -= 1

    s.add(cipher[10] == rol(v28 ^ v23 & ~v27, 8))
    s.add(cipher[11] == rol(v29 ^ v25 & ~v16, 8))
    s.add(cipher[4] == rol(v23 ^ v27 & ~v28, 1))
    s.add(cipher[0] == v27 ^ v28 & ~v23)
    s.add(cipher[9] == rol(v31 ^ v26 & ~v22, 8))
    s.add(cipher[8] == rol(v30 ^ v17 & ~v20, 8))
    s.add(cipher[6] == rol(v17 ^ v20 & ~v30, 1))
    s.add(cipher[5] == rol(v25 ^ v16 & ~v29, 1))
    s.add(cipher[2] == v30 & ~v17 ^ v20)
    s.add(cipher[1] == v29 & ~v25 ^ v16)
    s.add(cipher[7] == rol(v26 ^ v22 & ~v31, 1))
    s.add(cipher[3] == v31 & ~v26 ^ v22)

    if s.check() == sat:
        mol = s.model()
        flag1 = [mol.eval(i).as_long() for i in flag]
        cipher = flag1.copy()
        for i in flag1:
            print(hex(i),end=', ')
        print()
    else:
        break

print(cipher)
from Crypto.Util.number import *
res = b""
for i in range(2,len(cipher)):
    res+=long_to_bytes(cipher[i])
print(res)
# ISITDTU{2s_with0ut_y0u's_l1ke_2m0nths_that2much}