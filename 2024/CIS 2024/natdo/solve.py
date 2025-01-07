cipher=[0xDD, 0x50, 0x1C, 0x44, 0xC1, 0x3D, 0x78, 0x55, 0x4B, 0x68, 
  0xEB, 0x36, 0x6F, 0x17, 0x87, 0x02, 0x88, 0x17, 0x41, 0x5A, 
  0x59, 0xA9, 0x35, 0x51, 0x4E, 0x35, 0x97, 0x61, 0x4B, 0xB0, 
  0xF5, 0xEB]
from Crypto.Cipher import AES 
import hashlib
import binascii

salt = "the co lam duoc khong"
password = "tin chuan chua"
password_bytes = password.encode('utf-8')
salt_bytes = salt.encode('utf-8')
iterations = 10000
dklen = 48  
derived_key = hashlib.pbkdf2_hmac('sha512', password_bytes, salt_bytes, iterations, dklen)
derived_key_hex = binascii.hexlify(derived_key).decode('utf-8')
key = bytes.fromhex(derived_key_hex)
p = AES.new(key[0:32],AES.MODE_CBC,key[32:48])
plain = p.decrypt(bytearray(cipher))
print(plain)
