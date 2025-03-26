# key = list(b'abcdef7890123456')
# from z3 import *
# import string
# char = 'abcdef7890123456'
# key = [BitVec(f'key_{i}', 32) for i in range(16)]
# solver = Solver()
# for i in range(16):
#     solver.add(Or([key[i] == ord(c) for c in char]))
# start = 0x811c9dc5
# imul = 0x0000000001000193
# key_xor = 0
# cipher = [0]*16
# tmp = []
# for i in range(len(key)):
#     key_xor = (start * imul) & 0xffffffff
#     tmp.append(key_xor)
#     cipher[i] = key[i] ^ key_xor
#     start = cipher[i]
# cipher = cipher[::-1]
# key_cmp = [0x000000007586CBD1]
# solver.add(cipher[0] == key_cmp[0])
# n = 10
# while solver.check() == sat:
#     model = solver.model()
#     flag = [model[key[i]].as_long() for i in range(16)]
#     print(bytes(flag))
#     solver.add(Or([key[i] != model[key[i]] for i in range(16)]))
#     n += 1
#     if n == 20:
#         break

# base = 0x0007FF6D5EE1000
# breakpoint_list = [
#     0x00007FF6D5EEE7DC, 0x00007FF6D5EEEDF8, 0x00007FF6D5EEE8E2,
#     0x00007FF6D5EEE94B, 0x00007FF6D5EEE9F7, 0x00007FF6D5EEEB31,
#     0x00007FF6D5EEEBE0, 0x00007FF6D5EEEC96, 0x00007FF6D5EEED59,
#     0x00007FF6D5EEEDF1, 0x00007FF6D5EEEE96, 0x00007FF6D5EEEF39,
#     0x00007FF6D5EEF036, 0x00007FF6D5EEF0F4, 0x00007FF6D5EEF93D,
#     0x00007FF6D5EEF9F1, 0x00007FF6D5EEFACB, 0x00007FF6D5EEFB82
# ]
# base_new = 0x0007FF68D3F1000
# for i in range(len(breakpoint_list)):
#     breakpoint_list[i] =breakpoint_list[i] -  base
# print(breakpoint_list)


# key = list(b'1'*16)
# start = 0x811c9dc5
# imul = 0x0000000001000193
# key_xor = 0
# cipher = [0]*16
# tmp = []
# for i in range(len(key)):
#     key_xor = (start * imul) & 0xffffffff
#     tmp.append(key_xor)
#     cipher[i] = key[i] ^ key_xor
#     start = cipher[i]
# print(cipher)
# print(start)

# # list_key = [b'ddx6n7tYy_2WBg0N'
# # b'fFl7DGlplEVtqaBo'
# # b'vkpkvuwR_N865NRp'
# # b'aKwen4rm4cl8zpMG'
# # b'BPX1n0HAHFKi0_Cx'
# # b'87PuS7Hcajq3uv9d'
# # b'SbmwHn6T9B6iV0wJ'
# # b'_TU5XlQ6kgcTNtRU'
# # b'Wgm1cixI1_tk8RYW'
# # b'R25loCCWcS4bh8uL']

# # HTB_CA2K25_f0r_l0rd_m4l4k4r!


def ror(val, r_bits, max_bits):
    return ((val & ((1 << max_bits) - 1)) >> r_bits % max_bits) | (val << (max_bits - (r_bits % max_bits)) & ((1 << max_bits) - 1))

key = b'R25loCCWcS4bh8uL'
key = [(i) for i in key]
print(key)
