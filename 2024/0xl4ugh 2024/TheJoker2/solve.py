
import zlib
import png
# data = list(open("Exfiltrated_data.zip",'rb').read())
# key = [0x64, 0xD6, 0x69, 0x39]
# for i in range(len(data)):
#    data[i] = data[i] ^ key[i % 4]
# header = (bytes(data[0:4]))
# checksum = [0x64, 0xD6, 0x69, 0x39, 0x00, 0x00, 0x00, 0x00, 0x0B, 0xA2, 
#   0x06, 0x00]
# checksum = zlib.crc32(bytes(checksum))

# reader = png.Reader(filename="./lose.png")
reader = png.Reader(filename="./Would you lose.png")
width, height, pixels, metadata = reader.read()
pixel_data = []
for row in pixels:
    for pixel in zip(*[iter(row)]*4):
        pixel_data.extend(pixel)
print(bytes(pixel_data[0:24]).hex())
key_xor = pixel_data[4:8]
size_zip = len(pixel_data) - 16 
original_data = pixel_data[16:]
for i in range(len(original_data)):
    original_data[i] = original_data[i] ^ key_xor[i % 4]
with open("origin.zip",'wb') as f:
   f.write(bytes(original_data))