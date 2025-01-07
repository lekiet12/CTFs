import gostcrypto
from Crypto.Util.Padding import pad
key = b"1234567890abcedfabcdef1234nhdkfj"
with open("flag.txt", "rb") as f:
    flag = bytearray(f.read())

try:
    plaintext = bytes.fromhex("1234567890abcedf1234567890abcedf") 
    plaintext = pad(plaintext, 16)
    print(len(plaintext))
    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    print(ciphertext.hex())
except:
    print("Eh!")
    exit(0)

# 50712a44c97fa08c1d31b47e591ace0e
# 50712a44c97fa08c1d31b47e591ace0e
# 798c999e3055a7a87e4d63ed8a846a02