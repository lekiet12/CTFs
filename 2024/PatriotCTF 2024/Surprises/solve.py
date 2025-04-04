from Crypto.Cipher import AES 

cipher = open("flag.txt.enc",'rb').read()
iv = bytearray([0x00 ,0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 
  0x0B, 0x0C, 0x0D, 0x0E, 0x0F])

key = bytearray([0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF, 0x10, 0x32, 
  0x54, 0x76, 0x98, 0xBA, 0xDC, 0xFE, 0xF0, 0xE1, 0xD2, 0xC3, 
  0xB4, 0xA5, 0x96, 0x87, 0x78, 0x69, 0x5A, 0x4B, 0x3C, 0x2D, 
  0x1E, 0x0F])

p = AES.new(key, AES.MODE_CFB, iv, segment_size=128)

plain = p.decrypt(cipher)

print(plain)

# b'PCTF{UPX_15_2_3A$y_t0_uNp4cK}\n'