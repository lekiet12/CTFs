from Crypto.Cipher import AES
def create_inv_s_box(s_box):
    inv_s_box = [0] * 256  
    for i in range(256):
        inv_s_box[s_box[i]] = i
    return inv_s_box

key = [0x3A, 0x69, 0xFF, 0x6B, 0x00, 0x00, 0x00, 0x00, 0x8C, 0x5E, 
  0x2D, 0x63, 0x00, 0x00, 0x00, 0x00]
plaintext = open('flag.txt', 'rb').read()
print(list(plaintext))
p = AES.new(bytes(key), AES.MODE_ECB)
ciphertext = p.encrypt(plaintext)
print(ciphertext)
sbox = open("./enc.enc","rb").read()
print(list(sbox[256:]))
inv_s_box = create_inv_s_box(sbox[0:256])  
# print(inv_s_box)