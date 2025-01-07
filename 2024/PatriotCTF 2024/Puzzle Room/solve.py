enc_flag = b"FFxxg1OK5sykNlpDI+YF2cqF/tDem3LuWEZRR1bKmfVwzHsOkm+0O4wDxaM8MGFxUsiR7QOv/p904UiSBgyVkhD126VNlNqc8zNjSxgoOgs="
import base64
import hashlib
from Crypto.Cipher import AES 
import itertools
def decrypt(enc,key):
    key = hashlib.sha256(key.encode()).digest()
    enc = base64.b64decode(enc)
    iv = enc[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return (cipher.decrypt(enc[AES.block_size :]))
grid = [
    [
        "SPHINX",
        "urn",
        "vulture",
        "arch",
        "snake",
        "urn",
        "bug",
        "plant",
        "arch",
        "staff",
        "SPHINX",
    ],
    [
        "plant",
        "foot",
        "bug",
        "plant",
        "vulture",
        "foot",
        "staff",
        "vulture",
        "plant",
        "foot",
        "bug",
    ],
    [
        "arch",
        "staff",
        "urn",
        "Shrine",
        "Shrine",
        "Shrine",
        "plant",
        "bug",
        "staff",
        "urn",
        "arch",
    ],
    [
        "snake",
        "vulture",
        "foot",
        "Shrine",
        "Shrine",
        "Shrine",
        "urn",
        "snake",
        "vulture",
        "foot",
        "vulture",
    ],
    [
        "staff",
        "urn",
        "bug",
        "Shrine",
        "Shrine",
        "Shrine",
        "foot",
        "staff",
        "bug",
        "snake",
        "staff",
    ],
    [
        "snake",
        "plant",
        "bug",
        "urn",
        "foot",
        "vulture",
        "bug",
        "urn",
        "arch",
        "foot",
        "urn",
    ],
    [
        "SPHINX",
        "arch",
        "staff",
        "plant",
        "snake",
        "staff",
        "bug",
        "plant",
        "vulture",
        "snake",
        "SPHINX",
    ],
]

grids = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] not in grids and grid[i][j]!='SPHINX' and grid[i][j]!='vulture' and grid[i][j]!='Shrine':
            grids.append(grid[i][j])
print(grids)

for n in range(1,8):
    for key in itertools.product(grids,repeat=n):
        key="vulture"+"".join(key)+"Shrine"
        plain = decrypt(enc_flag,key)
        if b'pctf' in plain:
            print(key)
            print(plain)
            break