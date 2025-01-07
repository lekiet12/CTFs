# 08092DE9
# 08092D41
# 0808EF90
# 0808EF72

flag=[' ']*0x13
flag[0xa]='l'
flag[0x11]=chr(0x4e)
flag[0x6]=chr(0x5f)
flag[0x12]='9'
flag[0x3]=chr(0x70)
flag[0xd]=chr(0x31)
flag[0xf]=chr(0x6e)
flag[0xb]='a'
flag[8]='3'
flag[0xc]=chr(0x31)
flag[0]='S'
flag[7]='D'
flag[4]=chr(0x6c)
flag[0x10]='i'
flag[0xe]=chr(0x65)
flag[2]=chr(0x6d)
flag[1]='1'
flag[9]='f'
flag[5]='3'
print("".join(flag))
# S1mpl3_D3fla11eniN9 




# import idaapi
# lst=[]
# for i in range(0x08048060,0x08092E46+1):
#    lst.append(idaapi.get_byte(i))
# with open("out.bin",'wb') as f:
#    f.write(bytearray(lst))
