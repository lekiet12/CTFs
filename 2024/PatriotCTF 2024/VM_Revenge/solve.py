import gdb
gdb.execute("b*0x0005555555555C7")
flag=[]
fake=[ord(i) for i in "123456789012345678901234567890"[::-1]]
gdb.execute("r <<< 123456789012345678901234567890 ")
for i in range(30):
    eax = gdb.execute("info register rax",to_string=True).split(" ")[-1]
    flag.append(int(eax,16))
    gdb.execute(f"set $rax={fake[i]}")
    print(bytearray(flag[::-1]))
    gdb.execute('c')
print(bytearray(flag[::-1]))
# pctf{th1s_vm_pr0blem_was_e4sy}