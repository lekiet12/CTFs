from capstone import *
from capstone.x86 import *
from keystone import *
import string
from z3 import *
s=Solver()
cipher = [1721316726, 1003633041, 1610664176, 116415076, 1954822517, 3346781256, 4019955012, 1648684297, 2199015073, 1302825731]
shell = open("shell.bin",'r').read().split("\n")
shell = [bytes.fromhex(x)[::-1] for x in shell]
shellcode = b''
for i in shell:
    shellcode += i 
md = Cs(CS_ARCH_X86, CS_MODE_32)
code = ""
for i in md.disasm(shellcode, 0x0):
    code +=("%s\t%s\n" %(i.mnemonic,i.op_str))
with open("dis.asm",'w') as f:
    f.write(code)
with open("shellcode.bin",'wb') as f:
    f.write(shellcode)

code = open("dis.asm",'r').read().split("\n")
number_mul = []
for i in range(len(code)):
    if "imul" in code[i]:
        x = code[i].split(",")[-1].strip()
        number_mul.append(int(x,16))
number1 = number_mul[0:40]
number2 = number_mul[40:]
flag = [BitVec(f"flag{i}",32) for i in range(40)]
temp = flag[:]
for i in range(len(flag)):
    s.add(flag[i] >= 32, flag[i] <= 127)
for i in range(0,39):
    flag[i] ^= (((number1[i]) * flag[i+1]) & 0xff)
    flag[i] += 53
    flag[i] &= 0xff 
flag[39] +=53
enc = []
for i in range(0,40,4):
    x = flag[i+3] << 24 | flag[i+2] << 16 | flag[i+1] << 8 | flag[i]
    x *= number2[i//4]
    x &=0xffffffff
    enc.append(x)
for i in range(10):
    s.add(enc[i] == cipher[i])
if s.check() == sat:
    m = s.model()
    x = [m.eval(temp[i]).as_long() for i in range(40)]
    print("".join([chr(i) for i in x]))
# Alpaca{Ev3ry7h1ng_3ve2y7h1n9_a11_cccccc}