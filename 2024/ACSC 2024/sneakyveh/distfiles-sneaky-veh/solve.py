from z3 import *

key = [BitVec('key%d' % i, 32) for i in range(4)]
s = Solver()

cipher = [0x252D0D17, 0x253F1D15, 0xBEA57768, 0xBAA5756E]

for i in range(4):
    if i == 0:
        v7 = key[0]
        v5 = key[1]
    elif i == 1:
        v7 = key[1]
        v5 = key[0]
    elif i == 2:
        v7 = key[2]
        v5 = key[3]
    else:
        v7 = key[3]
        v5 = key[2]
    s.add((v5 ^ ((v7 << 16) | (v7 >> 8) & 0xFF00 | ((v7 >> 0x18)&0xff))) == cipher[i])
enc = [0x18,0xa]
for i in range(2):
    a = (key[i]) & 0xff
    b = (key[i] >> 8) & 0xff
    c = (key[i] >> 16) & 0xff
    d = (key[i] >> 24) & 0xff
    s.add((a ^ b ^ c ^ d) == enc[i])
s.add((key[0] ^ key[1]) == 0x43534341)
s.add((key[2] ^ key[3]) == 0x34323032)
s.add((key[1] ^ 0x43534341)&0xff == 0x99)
s.add((key[3] ^ 0x34323032)&0xff == 0x4f)
if s.check()  == sat:
    m = s.model()
    for i in range(4):
        print(hex(m[key[i]].as_long())[2:], end=' ')
# cfe7a999 8cb4ead8 15d89f4f 21eaaf7d 