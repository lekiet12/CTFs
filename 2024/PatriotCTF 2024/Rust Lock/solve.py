import gdb
gdb.execute("b*0x0000555555567072")
flag=[]
gdb.execute("r <<< 12345678901234567890123456789012 ")
for i in range(0x20):
    eax = gdb.execute("info register rax",to_string=True).split(" ")[-1]
    ecx = gdb.execute("info register rcx",to_string=True).split(" ")[-1]
    flag.append(int(ecx,16))
    gdb.execute(f"set $rax={int(ecx,16)}")
    gdb.execute('c')
print(bytearray(flag))
# bytearray(b'tHe$3cRetunBr3Akab!ep4$$w0rD!1!1')
# ./rustLock
# Enter your password: tHe$3cRetunBr3Akab!ep4$$w0rD!1!1
# correct!: PCTF{Ru$7_r3vEr51ng_Pr0!!_3naGd}