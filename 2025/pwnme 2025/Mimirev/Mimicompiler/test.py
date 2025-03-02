from Crypto.Cipher import AES
import base64

# from z3 import *
# x = BitVec('x', 64)
# y = BitVec('y', 64)
# s=Solver()
# s.add(x <= 0xffffffff)
# s.add(y <= 0xffffffff)
# s.add(x >= 0)
# s.add(y >= 0)
# s.add(x+y == 314159)
# s.add((x * x + y * y * y - x * y) % 0xFFFFD == 0x42B6E)

# if s.check() == sat:
#     print(s.model())
# [y = 190703, x = 123456]
# x = 0x1e240
# y = 0x2e8ef
import hashlib
x = b"123456:190703"
hash_code = hashlib.sha256(x).digest()
print(hash_code)

# PWNME{R3v3rS1ng_Compil0_C4n_B3_good}