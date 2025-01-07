
from z3 import *
flag =[BitVec(f"x{i}",8) for i in range(16)]
enc = ['J','D',';','C','C','?','B','=','C','?','J','Q','J','D']
enc = [ord(i) for i in enc]
char = ['t','u','a','n','l','i','n','h']
char = [ord(i) for i in char]
s=Solver()
for i in range(len(flag)):
    s.add(Or([flag[i]==(char[j]) for j in range(len(char))]))
for i in range(0,14):
    s.add((flag[i]+flag[i+1]+flag[i+2])&0xff == enc[i])
if s.check()==sat:
    m = s.model()
    print(m)
    val = [m.eval(flag[i]).as_long() for i in range(16)]
    print(bytearray(val))

# tuanlinhlinhtuan

enc=[0x20,0x1d,0x13,0x01,0x1b,0x36,0x0c,0x09,0x0f,0x02,0x31,0x1c,0x1c,0x10,0x3e,0x00,0x11,0x06,0x15,0x0b,0x08,0x36,0x07,0x0e,0x33,0x27,0x2b,0x3b,0x2b,0x1d,0x00,0x18,0x11,0x2a,0x07,0x1b,0x02,0x07,0x00,0x06,0x33,0x53,0x47]
key = b'tuanlinhlinhtuan'
for i in range(len(enc)):
    enc[i]^=key[i%16]
print(bytearray(enc))
# Throw_back_the_nested_if_NES_have_funnnn_:)
