v6 = [0]*32
v6[0] = 67
v6[1] = 164
v6[2] = 65
v6[3] = 174
v6[4] = 66
v6[5] = 252
v6[6] = 115
v6[7] = 176
v6[8] = 111
v6[9] = 114
v6[10] = 94
v6[11] = 168
v6[12] = 101
v6[13] = 242
v6[14] = 81
v6[15] = 206
v6[16] = 32
v6[17] = 188
v6[18] = 96
v6[19] = 164
v6[20] = 109
v6[21] = 70
v6[22] = 33
v6[23] = 64
v6[24] = 32
v6[25] = 90
v6[26] = 44
v6[27] = 82
v6[28] = 45
v6[29] = 94
v6[30] = 45
v6[31] = 196
for i in range(32):
    v6[i] = (v6[i]//(i%2+1))^i 
print(bytearray(v6))
# bytearray(b'CSCTF{u_g0T_it_h0OrAy6778462123}')