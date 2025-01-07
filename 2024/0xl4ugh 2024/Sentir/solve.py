import base64
xor_key=[  0x0A, 0xBA, 0xDC, 0x0D, 0xEB, 0xAD, 0xF0, 0x0D, 0xCA, 0xFE, 
  0xBA, 0xBE, 0xC0, 0x00, 0xFF, 0xEE]
cipher = b"ScjoW9rDt1K+tonhhzC7ij73slKtwcRq6w=="
enc = base64.b64decode(cipher)
flag = ""
for i in range(len(enc)):
    flag += chr(enc[i] ^ xor_key[i % len(xor_key)])
print(flag)
# Cr4V1nG_tH3_G0Dd4Mn_Fl4g!
# 0xL4ugh{R3v3r$!Ng_N@t1vE_D0t_N3t_Pr0gR@m$_C4N_b3_CRu3L}