import gdb

def to_int(gdb_v:gdb.Value):
    return int(gdb_v.cast(gdb.lookup_type('unsigned long long')))

gdb.execute("file vmvm")
gdb.execute("d")

class VMDecoder(gdb.Breakpoint):
    
    def __init__(self, bp, opcode):
        super().__init__(bp)
        self.opcode = opcode
    def stop(self):
        global cpt,tfound,i
        edx = to_int(gdb.parse_and_eval("(uint64_t *)$edx"))
        if edx != 0 and edx != 1:
            return False
        if cpt == (i+1) and edx == 1:
            tfound=True
        cpt += 1
        return False
bp = VMDecoder("*0x55555555525F", 27)
flag = [0x41]*64
flag[0]= ord('C')
flag[1] = ord('S')
flag[2] = ord('C')
flag[3] = ord('C')
flag[4] = ord('T')
flag[5] = ord('F')
flag[6] = ord('{')
flag[-1] = ord('}')
flagx = ''.join(chr(v) for v in flag)
import string
charset = string.printable[0:len(string.printable)-10]

for i in range(64):

    tfound=False
    for char in charset:
        if char == "'":
            continue

        flag[i] = ord(char)
        flagx = ''.join(chr(v) for v in flag)
        print("testing" , flagx)
        cpt=0
        gdb.execute(f"run vmvm.vm <<< '{flagx}'")

        if tfound:
            print("found char : ", char)
            print(flagx)
            break
# CSCTF{i_would_make_gross_hidden_crypto_but_idk_crypto_f5f04dd12}