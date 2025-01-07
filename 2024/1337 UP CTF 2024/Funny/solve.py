import dis
import marshal

with open('funny.pyc', 'rb') as f:
    f.seek(16)
    code = marshal.load(f)
positions = list(code.co_positions())
rows = [bytearray(b" " * 0x1000) for _ in range(7)]

for i, pos in enumerate(positions):
    # ignore any positional info that is blank or isnt between lines 24-30
    start_lineno, end_lineno, start_pos, end_pos = pos
    if start_lineno is None or not (24 <= start_lineno <= 30):
        continue

    # each instruction in python is 2 bytes with the first byte being the opcode and second one being the operand
    insn = code.co_code[i*2:i*2+2]
    opcode, operand = insn[0], insn[1]

    # we only care about the LOAD_NAME instructions
    if opcode != dis.opmap['LOAD_NAME']:
        continue

    assert start_lineno == end_lineno # should always pass in this case
    idx = start_lineno - 24
    # the operand holds the index of the name in co_names
    src = code.co_names[operand] + ";"
    assert len(src) == end_pos - start_pos + 1
    print(pos)
    rows[idx][start_pos:end_pos] = src.encode()

# dump the key
with open("out_key.txt", "w") as file:
    for row in rows:
        file.write(row.rstrip().decode() + "\n")
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
msg = unpad(AES.new(code.co_consts[12], AES.MODE_CBC, code.co_consts[13]).decrypt(code.co_consts[11]), AES.block_size)
iv_positions = eval(msg.decode().split("\n")[5])

# dump the iv
iv = "".join(chr(rows[y][x]) for x, y in iv_positions)
print(f"{iv = !s}")
key = b'P05IT1ON4L_INF0RM4TION_1S_GR34T_'
cipher = b'\x1fQer\xec\xb6\x05\xee\xc0g/\x82\x0c\xdb\xecZ\x13\xf8\x08\x01\tB:\xe4\xbdkb/r\xba\xf6\xc0\xe9\xe6M\xf7\xa1\x02&\x17p\x7f)\xb4\xe0\xdf\xe8w'
p = AES.new(key,AES.MODE_CBC,iv.encode())
plaintext = p.decrypt(cipher)
print(plaintext)