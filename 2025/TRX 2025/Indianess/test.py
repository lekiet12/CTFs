import gdb
import string
gdb.execute("start")
gdb.execute("b*0x000055555555A7FF")
gdb.execute("")
flag = "012345678901234567890123456789"
char = string.ascii_letters+string.digits+"{_!?}"+string.punctuation
for i in range(0,len(flag)):
    for j in char:
        temp = flag[:i]+j+flag[i+1:]
        gdb.execute("r bytecode {flag}".format(flag=temp))
        for j in range(0,i):
            gdb.execute("c")
        dl = gdb.execute("x/s $dl", to_string=True)
        al = gdb.execute("x/s $al", to_string=True)
        if dl == al:
            flag = temp
            print(flag)
            break
# TRX{RC4_1s_4_r3al_m4st3rp13c3}