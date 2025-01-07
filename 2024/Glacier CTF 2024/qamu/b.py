from pwn import *

# p = process("./challenge")
p = remote("challs.glacierctf.com",13381)
p.recvuntil(b"\n")
p.sendline(b'AHMPQ-50007-ACBJW-qmjph:\xd8\x0c\xb4\xba$\xfe\xe3P')
p.interactive()

# gctf{th1s_w4s_4_b4d_1d34_t0_1mpl3ment_with1n_10_hour5}