key=b'0h_g0d_sup3r_k3y_is_here_gsirjcu'
from Crypto.Cipher import AES
import base64
cipher = "CXHoq5mV1jMA+63Sa7+IwhmhZWUXDL69B+wSB01uEQc63QWB0ZIeOiZtheLJpD0s2sC3s2+9FiWyRA+c1Y+vYw=="
cipher = base64.b64decode(cipher.encode())
iv = b'16_bytes_key_len'
p = AES.new(key,AES.MODE_CBC,iv)

plain = p.decrypt(cipher)

print(plain)
# b'wwf{R3m1nD_fuNNy_5tori3s_1s_s0_3a5Y_51796E6B6C6565}\r\r\r\r\r\r\r\r\r\r\r\r\r'