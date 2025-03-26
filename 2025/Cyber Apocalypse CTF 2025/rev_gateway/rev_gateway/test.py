def cal(a1):
    return  ((((a1) >> 1) & 0x55)) | (((2 * (a1)) & 0xaa))
def shr(value, shift, bits=64):
    return (value & (2**bits - 1)) >> shift

flag ='12345678901234561234567890123456'
flag = [ord(i) for i in flag]
flag = [cal(i) for i in flag]
tran_flag = flag
# print(bytes(tran_flag).decode())
index = [20, 18, 27, 8, 24, 4, 16, 5, 21, 10, 16, 28, 26, 13, 23, 27, 3, 19, 28, 31, 20, 26, 0, 31, 31, 0, 24, 2, 24, 23, 28, 21]
for i in range(32):
    tran_flag[index[i]], tran_flag[i] = tran_flag[i], tran_flag[index[i]]
# print(bytes(tran_flag).decode())

import string 
character = string.printable
cipher = [3056211200, 492570721, 1282371112, 1125303727, 1020619446, 510309723, 1020619446, 3228338623, 3980337024, 3136348648, 3215664806, 1020619446, 3017814043, 3136348648, 3789941608, 2957471604, 3017814043, 1020619446, 3215664806, 3898923214, 1282371112, 1125303727, 3017814043, 2635397451, 4002955503, 1020619446, 3215664806, 3215664806, 2635397451, 3136348648, 350043079, 2536674690]
enc = [0]*32
flag = [0]*32
for i in range(32):
    for char in range(0xff):
        x = (-1) & 0xffffffffffffffff
        x ^= char
        for j in range(8):
            if (x & 1) == 0:
                x = shr(x, 1)
            else:
                x = shr(x, 1)
                x ^= 0xc96c5795d7870f42
        x = (~x) & 0xffffffffffffffff
        enc[i] = x & 0xffffffff
        if enc[i] == cipher[i]:
            flag[i] = char
            break
# print(flag)
for i in range(31,-1,-1):
    flag[index[i]], flag[i] = flag[i], flag[index[i]]

res = [0]*32
for i in range(32):
    for char in range(0x20, 0x80):
        x = cal(char)
        if x == flag[i]:
            res[i] = char
            break
print(bytes(res).decode())

# HTB{r3tf@r_t0_tH3_h3@V3n5g@t3!!}