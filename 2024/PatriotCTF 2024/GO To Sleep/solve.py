key=[0xd,0x5e,0xa1,0xf9,0x15,0x9a,0xcc]
flag=[ord(i) for i in "aes gcm nonce reuse attack"]
for i in range(len(flag)):
  flag[i]^=key[i%len(key)]
print(flag)
from Crypto.Cipher import AES
key=[ 0xCC, 0xD9, 0xCB, 0xE2, 0xAD, 0xF4, 0x2C, 0xFC, 0x90, 0x51, 
  0xFA, 0xFD, 0x5B, 0x89, 0x77, 0x80, 0xA1, 0xF2, 0xA2, 0x36, 
  0x9D, 0x87, 0x1F, 0x05, 0x7B, 0xBB, 0x2E, 0x49, 0xAF, 0xDA, 
  0xB2, 0x58]
# nonce =[ 0x59, 0xA3, 0x18, 0xB6, 0x51, 0x10, 0x0E, 0x7E, 0x50, 0x41, 
#   0x86, 0x73]
# p = AES.new(bytearray(key[0:32]),AES.MODE_GCM,bytearray(nonce))
# enc=p.encrypt(bytearray(flag))
# print(enc.hex())



enc=bytes.fromhex("8a7e7886aac76f550b3e0bbd59c5f0ea46ed30c858a99423372bbccc960fcf7158a23de05c2788617986affa78ae8b608c6b38386c4715b9e49bcb")
key=[0xd,0x5e,0xa1,0xf9,0x15,0x9a,0xcc]
enc=[i for i in enc]
for i in range(len(enc)):
    enc[i]^=key[i%len(key)]
nonce = enc[0:12]
enc = enc[12:]
key=[ 0xCC, 0xD9, 0xCB, 0xE2, 0xAD, 0xF4, 0x2C, 0xFC, 0x90, 0x51, 
  0xFA, 0xFD, 0x5B, 0x89, 0x77, 0x80, 0xA1, 0xF2, 0xA2, 0x36, 
  0x9D, 0x87, 0x1F, 0x05, 0x7B, 0xBB, 0x2E, 0x49, 0xAF, 0xDA, 
  0xB2, 0x58]
p = AES.new(bytearray(key),AES.MODE_GCM,bytearray(nonce))
flag=p.decrypt(bytearray(enc))

key=[0xd,0x5e,0xa1,0xf9,0x15,0x9a,0xcc]
flag=[i for i in flag]
for i in range(len(flag)):
  flag[i]^=key[i%len(key)]
print(bytearray(flag))

# bytearray(b'PCTF{whY_4rE_y0U_$t1LL_Aw4k3?!}{\xf3\xb1)\xcfD\x03\xd5\xe0\xe7\x8a\xfa\xdeSdn')
