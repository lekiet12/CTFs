cipher = "147274ff36e71d07cfad08e75f0352799d0081c6862fd96aebb08566f49ca86f15528c5121940ddc3ee92b816b1147be934d03389ee0cfad5b539ebf35feb969"
cipher = bytes.fromhex(cipher)
cipher = list(cipher)
from pwn import *
import string
character = string.ascii_letters + string.digits + string.punctuation
def get_key(flag):
    try:
        p = process('./chas_elf')
        p.sendline(flag)
        data = p.recv().strip()
        p.close()
        return data.decode()
    except:
        return None
### get key ###
list_key = []
for k in character:
    flag = k 
    flag += '1'*(64-len(flag))
    for ch in character:
        temp = flag + ch 
        data = get_key(temp.encode())
        # print(data)
        if data is None:
            continue
        enc = list(bytes.fromhex(data))
        if enc[0] == cipher[0]:
            # print("Found key:", ch)
            list_key.append(k)
            break
list_flag = []
flag = [1] * 65

for k in list_key:
    flag[64] = ord(k)
    res = ""
    for i in range(64):
        for ch in character:
            flag[i] = ord(ch)
            data = get_key(bytes(flag))
            if data is None:
                continue
            enc = list(bytes.fromhex(data))
            if len(enc) != 64:
                continue
            if enc[i] == cipher[i]:
                res += ch
                break
        if len(res) != i + 1:
            break
    if len(res) == 64:
        list_flag.append(res+k)
for flag in list_flag:
    print(flag)
# C0py_@nd_P4tch?_N0_7hi$_1s_Ch@s_Tr1ck!_W3lc0m3_tO_ChA_W0rld_haha!