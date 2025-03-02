import hashlib
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

user = 'Owen'
license, key = gen_license('Owen')
print(license)
print(decrypt_license(key, license))