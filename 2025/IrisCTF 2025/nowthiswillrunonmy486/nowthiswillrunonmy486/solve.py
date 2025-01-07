from Crypto.Util.number import long_to_bytes
key_xor = [0x0BF51B0D7,0x75CC547B,0x4F0FD83A,0x0A2117744,0x0ECD0CEC6,0x2E19F9FA,0x32EA83D9,0x0E5EB61E0]
enc = [0x0CC38C2BE,0xEAA2018,0x1078B74D,0xDB631232,0x98A0A199,0x42789493,0x5685E086,0x98CA4085]
flag = [i^j for i,j in zip(key_xor,enc)]
res = "".join([long_to_bytes(i).decode()[::-1] for i in flag])
print(res)
# irisctf{wow_very_optimal_code!!}