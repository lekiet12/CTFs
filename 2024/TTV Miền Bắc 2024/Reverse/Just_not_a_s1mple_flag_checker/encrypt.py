flag="KCSC{3V3rY_r3v3R53_En91n33r_kN0w_H0W_TH3_5t4ck_w0Rkk}"
flag=[ord(i) for i in flag]
# print(bytearray(flag))
flag=[bin(i)[2:].zfill(8) for i in flag]
flag="".join(flag)
flag=[int(i,10) for i in flag]
data = open("data.bin",'rb').read()
data=[i for i in data]
index=0
for k in range(423,-1,-1):
    if data[4*k]!=1:
        print("a",end="")
    data[4*k]^=flag[index]
    index+=1
array=[]
for i in range(0,424,2):
    array.append(data[4*i+4])
    array.append(data[4*i])
array=array[::-1]
value = []
for i in range(0,len(array),8):
    v2 = 0
    for j in range(8):
        v4 = array[i]
        v2 = v2+v4*pow(2,8-j-1)
        v2 &=0xff
        i+=1
    value.append(v2)
array=[]
for i in range(len(value)):
    x = value[i]
    for j in range(8):
        array.append(x % 8)
        x = x // 8
array = array[::-1]
value = []
for i in range(0,len(array),8):
    v2 = 0
    for j in range(8):
        v4 = array[i]
        v2 = v2+v4*pow(10,8-j-1)
        v2 &=0xff
        i+=1
    value.append(v2)
enc=[36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 125, 103, 97, 108, 102, 32, 101, 107, 97, 102, 32, 97, 32, 116, 111, 110, 32, 116, 115, 117, 106, 32, 101, 114, 101, 104, 32, 103, 110, 105, 104, 116, 32, 116, 111, 110, 123, 67, 83, 67, 75]
key=[194, 61, 41, 207, 52, 222, 56, 16, 204, 117, 61, 84, 242, 71, 27, 181, 135, 24, 182, 167, 4, 1, 4, 52, 4, 40, 89, 240, 24, 247, 25, 67, 13, 0, 225, 140, 173, 98, 83, 235, 229, 218, 160, 216, 76, 104, 92, 160, 52, 200, 62, 102, 80]
for i in range(len(enc)):
    value[i]^=key[i]
value=value[::-1]
for i in range(len(value)):
    if value[i]!=enc[i]:
        print("Positive: "+str(i))