from Crypto.Util.number import long_to_bytes
enc = [3316489910, 3588225682, 3353127073, 3784025294, 3789333130, 3533568649, 47002]
for i in range(len(enc)):
    enc[i] ^=0xBEEFCAFE
flag = b''
for i in enc:
    flag += long_to_bytes(i, 4)[::-1]
print(flag)
# HTB{l00k_b3y0nd_th3_w0rld}