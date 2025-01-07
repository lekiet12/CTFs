arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
import random
number = 4
num = [3, 2, 4, 5, 0, 1]
x = max(min(number,5),0)
random.seed(number)
random.shuffle(arr)
if num[x] != 0:
    print("https://www.youtube.com/watch?v=3GDr-eyhsSM")
    exit(0)
full_box = arr[::-1]
flag = ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]tt'
flag=[ord(i) for i in flag]
sum_flag = sum(flag) % 512
random.seed(sum_flag % (2 ** 9))
if (random.randint(0,10000) != 7930):
    exit(0)
flag = [pow(i,-1,257) for i in flag]
box = full_box[len(full_box)-len(flag):]
for i in range(len(flag)):
    flag[i]^=box[i]
bit_one = [bin(i).count('1') for i in box]
bit_length = [len(bin(i))-2 for i in box]
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
val = res.to_bytes(len(flag),'big')
print(val)
enc = b"\x00\x00\x00\x00\x00-\xea\x12Xe\xfeP\xfe\xd7\xf2)&U\x08,#\x82b\xd8\x85b\xe8\xf7_\x1c\xf8P\\2\xec\x9b\x9c\xfai\xc3q\x12\xad#\x8a<\xab\x8e'c\xd5+6\x92\xaee\x18c\xb0\x0e\x87\x06\xab4E\x98\xda\x8a\xd3"
if enc == val:
    print("correct")
    