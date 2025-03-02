from pwn import *
import base64
import zlib
from Crypto.Cipher import ARC4
import json
import ctypes
libc = ctypes.CDLL('libc.so.6')
def gen_license(user):
    seed = (zlib.crc32(user.encode()))
    libc.srand(seed)
    x = libc.rand() % 0xffff
    y = libc.rand() % 0xffff
    key = (x * y).to_bytes(4, 'big')
    plaintext = b'PwNmE_c4_message!137'
    cipher = ARC4.new(bytes(key))
    serial = cipher.encrypt(plaintext)
    license = {'user': user, 'serial': serial.hex()}
    return base64.b64encode(json.dumps(license).encode()), key
def decrypt_license(key, license):
    license_json = json.loads(base64.b64decode(license).decode())
    serial =bytes.fromhex(license_json['serial'])
    cipher = ARC4.new(bytes(key))
    decrypted = cipher.decrypt(serial)
    return decrypted

p = remote("c4license-aff71d5b8635d032.deploy.phreaks.fr", 443, ssl=True, sni="c4license-aff71d5b8635d032.deploy.phreaks.fr")
for i in range(100):
    data = p.recvuntil(b"user : ")
    user = (data.split(b"\n")[1].split(b' ')[3]).decode()
    license, key = gen_license(user)
    p.sendline(license)
p.interactive()