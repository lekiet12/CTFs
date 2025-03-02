from Crypto.Cipher import AES
import hashlib
from Crypto.Util import Counter

# big endian

p = int(bytes.fromhex("6b152f4845212e15")[::-1].hex(), 16)
# print(p)
g = 2
KA = int.from_bytes(bytes.fromhex("5c4f31a50c2d980c"), byteorder='little')
KB = int.from_bytes(bytes.fromhex("65027c9877d09804"), byteorder='little')
# print(KB)

# p = 1526193905172682091
# A = Mod(907524857249484636, p)
# g = Mod(0x02, p)
# a = discrete_log(A, g)
# show(a)

a = 1330218279148611220
key_shared = pow(KB, a, p).to_bytes(8,'little')
# print(key_shared)

key = hashlib.sha256(key_shared).digest()
ciphers = list(open("./stream.txt","r").read().split("\n"))

# cipher = bytes.fromhex("6877c550aa2cebfc5f899f1847fb5ae6045f8d562277d574bee80647031fb055c7e71efbf9517ccbb0c2446b854dfed44ae867ecbc33dde85258c6f7887180e2d7be7ec4cb76739f39f0e3abb56a1b253594a96f086424c639d4af536ddd57301fcd2a9d35ac43e516d22a042f5c98bd464c0c761cf73514837545c98ff8cffc037af2eec2e55be389")

for cipher in ciphers:
    cipher = bytes.fromhex(cipher)
    nonce = cipher[len(cipher)-16-4:-4]
    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    print(aes.decrypt(cipher[:len(cipher)-16-4]))
# PWNME{Crypt0_&_B4ndwidth_m4k3s_m3_f33l_UN83474813!!!}