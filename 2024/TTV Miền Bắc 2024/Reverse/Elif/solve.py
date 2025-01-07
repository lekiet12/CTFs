from z3 import *
inp=[BitVec(f"x{i}",32) for i in range(49)]
s=Solver()
s.add(inp[0]==ord('K'))
s.add(inp[1]==ord('C'))
s.add(inp[2]==ord('S'))
s.add(inp[3]==ord('C'))
s.add(inp[4]==ord('{'))
s.add(inp[48]==ord('}'))
for i in range(len(inp)):
    s.add(inp[i]>32)
    s.add(inp[i]<126)
s.add(inp[30] + inp[44] + inp[16] + inp[38] + inp[47] + inp[7] == 398)

s.add(inp[41] + inp[22] + inp[38] + inp[33] + inp[28] + inp[20] == 451)

s.add(inp[10] + inp[3] + inp[39] + inp[14] + inp[4] + inp[47] == 440)

s.add(inp[2] + inp[12] + inp[45] + inp[4] + inp[42] + inp[30] == 581)

s.add(inp[36] + inp[36] + inp[26] + inp[43] + inp[21] + inp[1] == 587)

s.add(inp[16] + inp[3] + inp[16] + inp[20] + inp[38] + inp[39] == 274)

s.add(inp[28] + inp[39] + inp[18] + inp[38] + inp[47] + inp[8] == 372)

s.add(inp[25] + inp[19] + inp[36] + inp[19] + inp[20] + inp[31] == 470)

s.add(inp[44] + inp[27] + inp[5] + inp[41] + inp[16] + inp[42] == 565)

s.add(inp[46] + inp[35] + inp[8] + inp[1] + inp[4] + inp[47] == 447)

s.add(inp[41] + inp[20] + inp[42] + inp[40] + inp[3] + inp[43] == 503)

s.add(inp[36] + inp[4] + inp[21] + inp[46] + inp[34] + inp[38] == 532)

s.add(inp[43] + inp[45] + inp[3] + inp[45] + inp[3] + inp[17] == 382)

s.add(inp[24] + inp[2] + inp[6] + inp[2] + inp[25] + inp[1] == 490)

s.add(inp[38] + inp[41] + inp[33] + inp[34] + inp[21] + inp[42] == 569)

s.add(inp[17] + inp[38] + inp[1] + inp[15] + inp[46] + inp[35] == 364)

s.add(inp[40] + inp[17] + inp[34] + inp[33] + inp[39] + inp[19] == 398)

s.add(inp[18] + inp[21] + inp[4] + inp[27] + inp[19] + inp[29] == 541)

s.add(inp[30] + inp[34] + inp[42] + inp[26] + inp[18] + inp[47] == 588)

s.add(inp[23] + inp[24] + inp[30] + inp[1] + inp[13] + inp[7] == 471)

s.add(inp[17] + inp[16] + inp[32] + inp[16] + inp[15] + inp[14] == 343)

s.add(inp[30] + inp[10] + inp[24] + inp[3] + inp[40] + inp[3] == 519)

s.add(inp[10] + inp[34] + inp[27] + inp[38] + inp[46] + inp[40] == 480)

s.add(inp[6] + inp[6] + inp[46] + inp[35] + inp[5] + inp[13] == 357)

s.add(inp[18] + inp[16] + inp[5] + inp[6] + inp[12] + inp[32] == 411)

s.add(inp[1] + inp[3] + inp[37] + inp[4] + inp[22] + inp[44] == 514)

s.add(inp[26] + inp[11] + inp[12] + inp[47] + inp[22] + inp[2] == 541)

s.add(inp[32] + inp[32] + inp[18] + inp[34] + inp[31] + inp[37] == 454)

s.add(inp[38] + inp[25] + inp[1] + inp[23] + inp[28] + inp[27] == 403)

s.add(inp[37] + inp[11] + inp[2] + inp[24] + inp[39] + inp[21] == 457)

s.add(inp[21] + inp[4] + inp[3] + inp[11] + inp[42] + inp[2] == 588)

s.add(inp[11] + inp[36] + inp[27] + inp[1] + inp[18] + inp[19] == 549)

s.add(inp[16] + inp[18] + inp[37] + inp[41] + inp[25] + inp[45] == 446)

s.add(inp[19] + inp[19] + inp[18] + inp[8] + inp[25] + inp[14] == 453)

s.add(inp[19] + inp[2] + inp[40] + inp[34] + inp[27] + inp[5] == 461)

s.add(inp[48] + inp[41] + inp[33] + inp[41] + inp[23] + inp[37] == 533)

s.add(inp[45] + inp[9] + inp[8] + inp[32] + inp[4] + inp[26] == 531)

s.add(inp[47] + inp[27] + inp[2] + inp[32] + inp[3] + inp[38] == 393)

s.add(inp[32] + inp[27] + inp[2] + inp[34] + inp[27] + inp[14] == 506)

s.add(inp[24] + inp[14] + inp[39] + inp[20] + inp[3] + inp[17] == 365)

s.add(inp[10] + inp[17] + inp[43] + inp[28] + inp[48] + inp[48] == 565)

s.add(inp[35] + inp[47] + inp[27] + inp[42] + inp[35] + inp[37] == 415)

s.add(inp[10] + inp[37] + inp[37] + inp[44] + inp[21] + inp[15] == 502)

s.add(inp[9] + inp[44] + inp[9] + inp[48] + inp[38] + inp[15] == 600)

s.add(inp[16] + inp[47] + inp[12] + inp[27] + inp[39] + inp[16] == 386)

s.add(inp[2] + inp[37] + inp[32] + inp[41] + inp[9] + inp[13] == 485)

s.add(inp[25] + inp[18] + inp[25] + inp[41] + inp[40] + inp[11] == 566)

s.add(inp[36] + inp[37] + inp[4] + inp[12] + inp[35] + inp[42] == 546)

s.add(inp[45] + inp[32] + inp[12] + inp[19] + inp[16] + inp[3] == 371)

if s.check()==sat:
    m = s.model()
    flag=[m.eval(inp[i]).as_long() for i in range(49)]
    print(bytearray(flag))
# bytearray(b'KCSC{700_much_1f-3l53_f0r_fl46ch3ck3r!!!7ry_z3<3}')