import base64
index = [52,45,37,10,40,25,20,18,55,34,20,19,53,43,27,23,56,53,24,17,46,30,28,14,42,21,16,11,43,36,17,10,51,45,32,9,38,30,29,9,31,25,14,8,55,34,28,7,51,47,23,7,56,49,32,15,46,31,21,6,55,8,6,5,44,38,27,5,39,25,19,4,48,37,22,3,44,41,12,3,50,36,29,2,42,28,20,1,49,26,4,0,51,42,25,13,41,35,18,12,54,48,2,0,47,33,17,10,38,32,15,9]

enc =    "anVtcGp1bXBqdW1wQtXNWGp1bXBqdW1wanVtcGp1bXBq"
cipher = "anVtcGp1DXBqdW1wanVtcGp1bXBqdW1wanVtcGp1bXBq"
enc = base64.b64decode(enc)
cipher = base64.b64decode(cipher)
print(enc)
print(cipher)
