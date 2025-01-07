cipher = bytes.fromhex(open("./enc",'r').read().strip())
with open('output.txt', 'wb') as file:
    file.write(cipher)

with open('output.txt', 'r') as file:
    output = [ord(char) for char in file.read().strip()]
val_add = output[len(output)//2]

enc = []
for i in range(len(output)):
    if i != len(output)//2:
        enc.append(output[i])
enc1 = enc[:len(enc)//2]
enc2 = enc[len(enc)//2:]

for i in range(len(enc2)):
    enc2[i] = (enc2[i] - val_add) ^ enc1[i]
    enc1[i] = (enc1[i] - val_add) ^ enc2[i]
print(bytes(enc1).decode())
# irisctf{k3lp_1s_4_h34lthy_r3pl4c3m3n7_f0r_ch1p5}