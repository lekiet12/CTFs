


data = list(open("flag.txt.enc",'rb').read())
cipher = b''
val = []
for i in range(0,len(data),20):
    val.append(data[i+3]<<24 | data[i+2] << 16 | data[i+1] << 8 | data[i])
    cipher+=bytearray(data[i+4:i+20])
filename = list(b"flag.txt")
number = []
for index in range(4):
  for num in range(0xff):
      x = num
      x += 0x1505
      for i in range(len(filename)):
        x *=0x21
        x &=0xffffffff
        x +=filename[i]   
      if x == val[index]:
         number.append(num)
print(hex(number[3] << 24 | number[2] << 16 | number[1] << 8 | number[0]))
# 0x55755212



iv=[ 0x50, 0x36, 0x51, 0x77, 0x67, 0x6B, 0x78, 0x65, 0x48, 0x4B, 
  0x59, 0x7A, 0x62, 0x3A, 0x47, 0x6B]
key=[ 0x55, 0x6E, 0x6B, 0x5D, 0x6E, 0x38, 0x26, 0x6F, 0x37, 0x3E, 
  0x41, 0x5A, 0x46, 0x4E, 0x79, 0x4E]
from Crypto.Cipher import AES
p = AES.new(bytearray(key[0:16]),AES.MODE_CBC,bytearray(iv))
plaintext = p.decrypt(cipher)
print(plaintext)
# b'gctf{i_h0p3_y0u_used_th3_c0rrect_r4nd0m_funct10n_s0lv1Ng_th1s!!}'