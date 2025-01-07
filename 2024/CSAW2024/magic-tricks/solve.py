from pwn import * 
import time
enc=open("./enc.txt",'rb').read()
def send(flag):
    p = process("./chall")
    p.recvuntil(b'Enter data: ')
    p.sendline(flag.encode())
    p.recvuntil(b'Tada! Your file is ready but useless maybe!')
    time.sleep(0.5)
    p.close()

flag=""
import string
character = string.printable
while '}' not in flag:
  for char in character:
    _flag = flag+char 
    send(_flag)
    out = open("output.txt",'rb').read()
    if out[0:len(out)] == enc[0:len(out)]:
      flag+=char
      print(flag)
      break
print(flag)
# csawctf{tHE_runE5_ArE_7H3_k3y_7O_th3_G0ph3r5_mA91C}    