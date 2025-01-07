import subprocess
import string
character =string.digits+string.ascii_letters+string.punctuation
flag = []
numbers=[0xa5,0x39,0x24,0x90,0xa8,0xa5,0x88,0x77,0x26,0xe4,0x3c,0x14,0x03,0x1e,0xba,0x3c,0x7d,0xbb,0xdc,0xd6,0xaa,0x90,0x50,0xc9,0x0f,0xaa,0xdd,0x57,0x33,0xe1,0xa4,0xc7]
__flag = ""
for i in range(len(numbers)):
    idx = []
    for char in (character):
        temp = __flag+char
        p = subprocess.Popen("./ai_rnd",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
        output, error = p.communicate(input=temp)
        output = output.split(" ")
        num = [int(output[i],16) for i in range(0,len(output)-1)]
        if num[i]==numbers[i]:
            idx.append(char)
    flag.append(idx)
    __flag +=idx[0]
    print(flag)
# pctf{d33p_le@rnING}