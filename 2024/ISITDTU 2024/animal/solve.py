from z3 import *

flag=[BitVec(f"X{i}",8) for i in range(36)]
flag_ext=[ZeroExt(24, flag[i]) for i in range(36)]

s=Solver()
for i in range(36):
    s.add(flag[i]>32)
    s.add(flag[i]<126)
s.add(flag[0]==ord('I'))
s.add(flag[1]==ord('S'))
s.add(flag[2]==ord('I'))
s.add(flag[3]==ord('T'))
s.add(flag[4]==ord('D'))
s.add(flag[5]==ord('T'))
s.add(flag[6]==ord('U'))
s.add(flag[7]==ord('{'))
s.add(flag[35]==ord('}'))
s.add(flag[8]==ord('a'))
s.add(flag[17]==ord('c'))
s.add(flag[18]==ord('a'))
s.add(flag[19]==ord('t'))

s.add(flag_ext[8] * flag_ext[1] + flag_ext[32] * flag_ext[27] * flag_ext[25] - flag_ext[29] == 538738)
s.add(flag_ext[7] + flag_ext[20] * flag_ext[10] * flag_ext[4] - flag_ext[6] - flag_ext[11] == 665370)
s.add(flag_ext[14] + (flag_ext[16] - 1) * flag_ext[31] - flag_ext[30] * flag_ext[22] == -2945)
s.add(flag_ext[33] + flag_ext[3] - flag_ext[9] - flag_ext[18] - flag_ext[11] - flag_ext[4] == -191)
s.add(flag_ext[1] + flag_ext[30] + flag_ext[18] + flag_ext[25] * flag_ext[29] - flag_ext[8] == 4853)
s.add(flag_ext[13] + flag_ext[5] - flag_ext[7] * flag_ext[14] * flag_ext[23] * flag_ext[2] == -86153321)
s.add(flag_ext[13] + flag_ext[9] * flag_ext[5] * flag_ext[12] + flag_ext[27] * flag_ext[10] == 873682)
s.add(flag_ext[22] + flag_ext[3] + flag_ext[18] * (flag_ext[9] * flag_ext[21]) - flag_ext[6] == 451644)
s.add(flag_ext[21] + flag_ext[34] + flag_ext[24] + flag_ext[32] * flag_ext[23] - flag_ext[4] == 9350)
s.add(flag_ext[24] + flag_ext[35] + flag_ext[17] - flag_ext[19] - flag_ext[26] - flag_ext[6] == 27)
s.add(flag_ext[14] + flag_ext[13] + flag_ext[15] + flag_ext[23] * flag_ext[19] - flag_ext[3] == 11247)
s.add(flag_ext[2] + flag_ext[17] + (flag_ext[7] * flag_ext[12]) - flag_ext[15] - flag_ext[21] == 13297)
s.add(flag_ext[8] + flag_ext[35] + flag_ext[26] + flag_ext[28] - flag_ext[0] - flag_ext[20] == 266)
s.add(flag_ext[2] + flag_ext[17] + flag_ext[0] + flag_ext[12] * flag_ext[28] - flag_ext[1] == 10422)
s.add(flag_ext[22] + flag_ext[15] + flag_ext[5] * flag_ext[19] - flag_ext[34] - flag_ext[11] == 9883)
s.add(flag_ext[10] * flag_ext[33] + flag_ext[16] * (1 - flag_ext[20]) - flag_ext[0] == -5604)

print(s.check())
while s.check() == sat:
    m = s.model()
    val = [m.eval(flag[i]).as_long() for i in range(36)]
    print(bytearray(val))
    s.add(Or( [(flag[i] != s.model()[flag[i]]) for i in range(36)] ))
# bytearray(b'ISITDTU{a_g0lden_cat_1n_y0ur_area!!}')