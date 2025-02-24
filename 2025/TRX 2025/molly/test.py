import pefile

key = b'forgivemefather'
def convert(v11):
    return ((16 * v11) | (v11 >> 4)) & 0xff
pe = pefile.PE("./molly.exe")

section_text = None

for section in pe.sections:
    if b'.text' in section.Name:
        section_text = section
        break
if section == None:
    exit(0)
data = bytearray(section_text.get_data())
pages = section_text.SizeOfRawData // 0x1000
for i in range(pages):
    offset = i * 0x1000
    for j in range(0x1000):
        data[offset + j] = convert(data[offset + j])
        data[offset + j] = data[offset + j] ^ key[j % len(key)]
pe.set_bytes_at_offset(section_text.PointerToRawData, bytes(data))
pe.write("molly_dec.exe")
pe.close()