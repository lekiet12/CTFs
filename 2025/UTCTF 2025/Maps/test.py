import subprocess
import string
char = string.ascii_letters + string.digits + string.punctuation
cipher = "4934849349493674935749360493664940249346493534935849348493574936549351493644937449348493464936449365493744935349360493464935449364493574935749374493494935349358493594935449404"
cipher = [int(cipher[i:i+5]) for i in range(0, len(cipher), 5)]
flag = ""
for i in range(len(cipher)):
    for ch in char:
        temp = flag
        temp += ch
        p = subprocess.Popen("./chall", stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        out, err = p.communicate(input=temp)
        out = out.strip().split(" ")[-1].strip()
        out = [int(out[i:i+5]) for i in range(0, len(out), 5)]
        if out[i] == cipher[i]:
            flag += ch
            print(flag)
            break
print(flag)