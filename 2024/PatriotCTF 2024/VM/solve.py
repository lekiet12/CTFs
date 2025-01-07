import gdb
gdb.execute("b*0x00005555555555B3")
flag=[]
fake=[ord(i) for i in "12345678901234567890123456789012"]
gdb.execute("r vm_program.bin <<< 12345678901234567890123456789012 ")
for i in range(0x20):
    eax = gdb.execute("info register rax",to_string=True).split(" ")[-1]
    flag.append(int(eax,16))
    gdb.execute(f"set $rax={fake[i]}")
    print(bytearray(flag))
    gdb.execute('c')
print(bytearray(flag))
# bytearray(b'pctf{nest3d_vm_s3cr3ts}')