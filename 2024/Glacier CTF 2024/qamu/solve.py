from z3 import *
flag=[]
s=Solver()

rsi = flag[8//8]
rbx = flag[0x70//8]
r11 = flag[0xa0//8]
rbp = flag[0x60 // 8]
r9 = flag[0]
rdi = flag[0x20 // 8]
r12 = flag[0x30 // 8]
r8 = flag[0x38 // 8]
r10 = flag[0xb0 // 8]


s.add(flag[0x28//8] == 0x2d)
s.add(flag[0x58//8]==0x2d)
s.add(flag[0x88//8] == 0x2d)
s.add(flag[0xb8 // 8] == 0x3a)
s.add(flag[0x18//8] == 0x50)
s.add(flag[0] == flag[8//8])
s.add(flag[0x30 // 8] == flag[0x38 // 8])
s.add(flag[0x18//8] == flag[0x20 // 8])
s.add(flag[0] == flag[0x60 // 8])
s.add(flag[0] - 0x41 == 0x19 )
s.add(flag[0x30 // 8]-0x30 == 9)
s.add(flag[0x40 // 8] == 0x48)
s.add(flag[0x90//8] == 0x20 ^ flag[0x20 // 8])

s.add(flag[0] | flag[0xa0//8] == 0x6b)
s.add(flag[8//8] ^ flag[0x80] == 0x1f)
s.add(flag[0x88//8]+flag[0x10 // 8] == 0x7a)
s.add(flag[0x48//8] | flag[0x38 // 8] == 0x30)
s.add(flag[8//8])