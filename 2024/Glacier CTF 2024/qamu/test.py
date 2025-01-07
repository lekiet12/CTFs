vm_enc = open("vm_enc.bin","rb").read()
opcode = b''
from Crypto.Cipher import ARC4
from capstone import *
for k in range(0,len(vm_enc),0x1000):
    key = [0x00, 0x50, 0x00, 0x70, 0x00, 0x00, 0x00, 0x00, 0x25, 0xFA, 
    0x5B, 0xC3, 0x52, 0xA7, 0x88, 0xD5, 0x5C, 0x15, 0xFF, 0x16, 
    0xE0, 0xAC, 0x36, 0x2A, 0xE0, 0xD1, 0x37, 0x40, 0x59, 0x83, 
    0x7D, 0x55]
    key[0] = k & 0xff
    key[1] = (k >> 8) & 0xff
    key[2] = (k >> 16) & 0xff
    p = ARC4.new(bytearray(key))

    code_asm = p.decrypt(vm_enc[k:k+0x1000])
    opcode+=code_asm
    index = 0
    for i in range(0,len(code_asm)-2):
        if code_asm[i] == 0xff and code_asm[i+1] == 0xe7:
            index = i+1
            break
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for insn in md.disasm(code_asm[0:index + 1], 0x1000):
        # if "jmp" in insn.mnemonic:
        #     continue
        print(f"{insn.mnemonic} {insn.op_str}")
with open("shellcode",'wb') as f:
    f.write(opcode)