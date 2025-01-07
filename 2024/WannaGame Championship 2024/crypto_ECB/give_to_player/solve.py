import gostcrypto
from Crypto.Util.Padding import pad
import binascii
import string
from pwn import *
key = b"1234567890abcedf1234567890abcedf"  
with open("flag.txt", "rb") as f:
    flag_test = bytearray(f.read())

def encrypt_with_kuznechik(plaintext):
    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
    return cipher.encrypt(plaintext)

# flag = ""
# character = string.ascii_letters+string.digits+"{_}"
# for i in range(16):
#     plaintext = b'a'*(15-i)
#     plaintext = pad(plaintext + flag_test, 16)
#     ciphertext = encrypt_with_kuznechik(plaintext)
#     res = ciphertext
#     for char in character:
#         plaintext = b'a'*(15-i) + flag.encode() + char.encode()
#         plaintext = pad(plaintext + flag_test, 16)
#         ciphertext = encrypt_with_kuznechik(plaintext)
#         if ciphertext[0:16] == res[0:16]:
#             flag += char
#             print(flag)
#             break

def send_server(data):
    p = remote("chall.w1playground.com",24777)
    p.sendlineafter(b"Plaintext (hex): ",data.encode())
    ciphertext = bytes.fromhex(p.recv().decode())
    p.close()
    return ciphertext

flag = ""
character ="{_}"+string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
temp = ""
for i in range(0,48):
    plaintext = b'a'*(47-i)
    res = send_server(plaintext.hex())
    for char in character:
        plaintext = b'a'*(47-i) + flag.encode() + char.encode()
        ciphertext = send_server(plaintext.hex())
        if ciphertext[0:48] == res[0:48]:
            flag += char
            print("FLAG : "+flag)
            if "}" in flag:
                exit(0)
            break
    print(flag)
# FLAG : W1{0Ld_pr0bl3m_BUT_n3W_c1pher}