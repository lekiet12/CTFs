import pefile
from Crypto.Cipher import ChaCha20
iv = [ 0xd0, 0, 0, 0, 0, 0, 0, 0]
key = [ 0x51, 0x5A, 0xEE, 0xF6, 0x31, 0x60, 0x65, 0x39, 0x9A, 0xE2, 
  0x6D, 0xAA, 0x8F, 0x22, 0x37, 0x6D,0xAE, 0x0B, 0x15, 0x70, 0xFA, 0x65, 0x1B, 0x88, 0x81, 0xDA, 
  0x6F, 0x64, 0x26, 0x79, 0x0B, 0x03]

pe = pefile.PE('molly.exe')

section_text = None
for section in pe.sections:
    if b'.text' in section.Name:
        section_text = section
        break
pages = section_text.SizeOfRawData // 0x1000 + 1
data = section_text.get_data()

for i in range(pages):
    offset = i * 0x1000
    data_page = data[offset:offset + 0x1000]
    cipher = ChaCha20.new(key=bytes(key), nonce=bytes(iv))
    decrypted = cipher.decrypt(data_page)
    data = data[:offset] + decrypted + data[offset + 0x1000:]
    print(f'Page {i} decrypted')
pe.set_bytes_at_offset(section_text.PointerToRawData, data)
pe.write('molly_dec.exe')