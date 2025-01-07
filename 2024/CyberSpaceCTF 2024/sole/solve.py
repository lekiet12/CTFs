from z3 import *

flag = [BitVec(f'x_{i}',8) for i in range(26)]

s = Solver()

s.add((flag[4] * (flag[19] * flag[11])) & 0xffffffff == 0x5F76C)
s.add((flag[13] * (flag[22] * flag[8])) & 0xffffffff == 0x8A9A8)
s.add((flag[22] * flag[0] + flag[15]) & 0xffffffff == 0x1308)
s.add((flag[11] + (flag[0] + flag[8])) & 0xffffffff == 199)
s.add((flag[13] - (flag[22] * flag[12])) & 0xffffffff == 0xFFFFF177)
s.add((flag[9] * flag[4] - flag[1]) & 0xffffffff == 8037)
s.add((flag[11] * (flag[9] * flag[16])) & 0xffffffff == 0x429C0)
s.add((flag[15] + (flag[23] * flag[3])) & 0xffffffff == 9792)
s.add((flag[9] - flag[23] - flag[4]) & 0xffffffff == -70)
s.add((flag[5] - flag[21] - flag[8]) & 0xffffffff == -63)
s.add((flag[0] + (flag[24] * flag[3])) & 0xffffffff == 5359)
s.add((flag[17] + (flag[25] * flag[1])) & 0xffffffff == 10483)
s.add((flag[2] * (flag[7] * flag[19])) & 0xffffffff == 0xDA2CE)
s.add((flag[19] + (flag[11] - flag[4])) & 0xffffffff == 93)
s.add((flag[7] + flag[6] - flag[10]) & 0xffffffff == 136)
s.add((flag[10] + (flag[0] + flag[25])) & 0xffffffff == 287)
s.add((flag[12] + flag[5] - flag[22]) & 0xffffffff == 104)
s.add((flag[4] * flag[7] + flag[12]) & 0xffffffff == 8243)
s.add((flag[4] + (flag[1] - flag[22])) & 0xffffffff == 81)
s.add((flag[8] - (flag[19] * flag[11])) & 0xffffffff == -5503)
s.add((flag[8] - flag[10] - flag[7]) & 0xffffffff == -129)
s.add((flag[21] + (flag[20] + flag[22])) & 0xffffffff == 224)
s.add((flag[12] + (flag[24] + flag[23])) & 0xffffffff == 232)
s.add((flag[4] + (flag[15] - flag[9])) & 0xffffffff == 2)
s.add((flag[2] + (flag[9] * flag[15])) & 0xffffffff == 5635)
s.add((flag[16] + (flag[24] + flag[14])) & 0xffffffff == 210)
s.add((flag[1] + flag[10] - flag[12]) & 0xffffffff == 125)
s.add((flag[18] - flag[1] - flag[5]) & 0xffffffff == -111)
s.add(((flag[12] - flag[14]) - flag[7]) & 0xffffffff == -163)
s.add((flag[1] + flag[5] - flag[16]) & 0xffffffff == 158)

if s.check() == sat:
    model = s.model()
    val = [model.eval(flag[i]).as_long() for i in range(26)]
    print(bytearray(val))

# bytearray(b'CSCTF{ruSt_15_c00l_r1gHt?}')