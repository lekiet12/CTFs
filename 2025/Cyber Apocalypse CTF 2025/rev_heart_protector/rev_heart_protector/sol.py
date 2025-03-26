import struct
def ror(a, r):
    return 0xffffffff & ((a >> r) | (a << (32-r)))

def rol(a, r):
	return ror(a, 32-r)

def fnv1(data):
    val = 0x811c9dc5
    for c in data:
        val = ((0x1000193 * val) ^ c) & 0xffffffff
    return val

def add_ror13(data):
	val = 0
	for i in data:
		val += i
		val = ror(val, 0xd)
	return val
def add_mul(data):
    val = 0
    for i in range(len(data)):
        val = val + data[i] * (211 ** i)
    val -= 1869
    return val ^ 9944768

key = b'a9060b622a6d95eb'
key = [i for i in key]

sum_key1 = fnv1(key)
sum_key2 = fnv1([key[5], key[6], key[7]])
sum_key3 = fnv1([key[10], key[12], key[14]])
sum_key4 = key[4] ^ 137
sum_key_5 = add_mul(key[0:4])
sum_key_6 = add_ror13([key[11], key[13], key[15]])

# print(hex(sum_key1), hex(sum_key2), hex(sum_key3), hex(sum_key4), hex(sum_key_5), hex(sum_key_6))
# print(sum_key1, sum_key2 & 0xff, sum_key3 & 0xff, sum_key4 & 0xff, sum_key_5 & 0xff, sum_key_6 & 0xff)

check_sum = [0x7586cbd1]
data = open("./code.bin","rb").read()
data = data[-20:]
for i in range(0, len(data), 4):
    check_sum.append(struct.unpack("<I", data[i:i+4])[0])

assert check_sum[0] == sum_key1
assert check_sum[3] == sum_key2 
assert check_sum[1] == sum_key3 
assert check_sum[4] == sum_key4 
assert check_sum[2] == sum_key_5
assert check_sum[5] == sum_key_6 


# a9060b622a6d95eb




from Crypto.Cipher import AES
key = b'a9060b622a6d95eb'
cipher = open("./heart.png.malakar","rb").read()
iv = cipher[:10]
cipher = cipher[10:]
p = AES.new(key, AES.MODE_GCM, iv)
plaintext = p.decrypt(cipher)
png = b'\x89PNG' + plaintext[5:]
with open("heart.png", "wb") as f:
    f.write(plaintext)