cipher = [2585429724, 899388381, 4007294163, 3309066984, 1194550300, 4079500242, 2336774860, 2269842548, 1082185272, 659220049, 257061793, 1028916883, 3371897701, 1741860709, 2112817587, 3849758243, 4279439379, 3501100340, 4081921180, 793164961, 1471580056, 4044857882, 3132155376, 2813685147, 2891868844, 3633379048, 2442764976]
key = [1634757697, 1632133475, 1867672419, 946105973]
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def encrypt(flag):
    global key
    x = rol(key[0], 5, 32) + ror(key[1], 3, 32)
    x &=0xffffffff
    y = ror(key[2], 3, 32) - rol(key[3], 5, 32)
    y &=0xffffffff
    flag = flag ^ x ^ y

    if flag & 1 == 0:
        key[0] ^= ror(y, 0xd, 32)
        key[1] ^= ror(y, 0xf, 32)
        key[2] ^= rol(x, 0xd, 32)
        key[3] ^= rol(x, 0xb, 32)
    else:
        key[0] ^= rol(y, 0xb, 32)
        key[1] ^= ror(y, 0xd, 32)
        key[2] ^= rol(x, 0xf, 32)
        key[3] ^= ror(x, 0xd, 32)
    for i in range(4):
        print(hex(key[i]),end=" ")
    print()
    return flag

def decrypt(cipher):
    global key
    x = rol(key[0], 5, 32) + ror(key[1], 3, 32)
    x &=0xffffffff
    y = ror(key[2], 3, 32) - rol(key[3], 5, 32)
    y &=0xffffffff
    flag = cipher ^ x ^ y
    if cipher & 1 == 0:
        key[0] ^= ror(y, 0xd, 32)
        key[1] ^= ror(y, 0xf, 32)
        key[2] ^= rol(x, 0xd, 32)
        key[3] ^= rol(x, 0xb, 32)
    else:
        key[0] ^= rol(y, 0xb, 32)
        key[1] ^= rol(y, 0xd, 32)
        key[2] ^= ror(x, 0xf, 32)
        key[3] ^= ror(x, 0xd, 32)
    return flag
flag = [0]*len(cipher)
res = b''
for i in range(len(cipher)):
    flag[i] = decrypt(cipher[i])
    res += (flag[i]).to_bytes(4, 'little')
print(res)
# b'Alpaca{th15_f145_1s_3xc3ssiv3ly_l3ngthy_but_th1s_1s_t0_3nsur3_th4t_1t_c4nn0t_b3_e4s1ly_s01v3d_us1ng_angr}\x00\x00\x00'