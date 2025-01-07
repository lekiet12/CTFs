full_box = [30, 38, 13, 50, 61, 19, 11, 8, 2, 51, 35, 58, 18, 63, 48, 3, 14, 33, 34, 23, 17, 49, 66, 6, 16, 70, 1, 41, 68, 52, 12, 10, 67, 60, 53, 5, 21, 24, 32, 15, 69, 55, 31, 65, 64, 26, 43, 9, 0, 25, 39, 71, 44, 59, 47, 22, 36, 27, 7, 28, 57, 4, 54, 62, 46, 20, 42, 37, 72, 40, 45, 29, 56]
def encrypted(flag):
    box = full_box[len(full_box)-len(flag):]
    flag = [pow(flag[i], -1, 257) for i in range(len(flag))]
    for i in range(len(flag)):
        flag[i]^=box[i]
    bit_one = [bin(i).count('1') for i in box]
    bit_length = [box[i].bit_length() for i in range(len(box))]    
    lshift = [(bit_one[i] << bit_length[i]) %256  for i in range(len(box))]
    added = [bit_length[i]+bit_one[i]+lshift[i] for i in range(len(box))]
    for i in range(len(flag)):
        flag[i]^=added[i]
    pow_number = []
    for i in range(len(flag)):
        pow_number.append(pow(256,i))
    res = 0
    for i in range(len(flag)):
        flag[i] *=pow_number[i]
        res |=flag[i]
    val = res.to_bytes(len(flag),'little')
    return val
target = b"\x00\x00\x00\x00\x00-\xea\x12Xe\xfeP\xfe\xd7\xf2)&U\x08,#\x82b\xd8\x85b\xe8\xf7_\x1c\xf8P\\2\xec\x9b\x9c\xfai\xc3q\x12\xad#\x8a<\xab\x8e'c\xd5+6\x92\xaee\x18c\xb0\x0e\x87\x06\xab4E\x98\xda\x8a\xd3"
target = target[::-1]
flag = 'a'*64
flag=[ord(i) for i in flag]
import string 
character = string.printable
for i in range(64):
    for char in character:
        flag[i]=ord(char)
        result = encrypted(flag)
        if target[:i+1] == result[:i+1]:
            print(bytearray(flag).decode())
            break