import string

char = string.ascii_letters + string.digits
enc = [16641, 3364, 29584, 1849, 34225, 784, 30976, 441, 15625, 529, 23409, 225, 36864, 1764, 17689, 3969, 37249, 784, 16900, 225, 19321, 361, 14884, 225, 27556, 676, 11449, 2401, 22500, 4, 12996, 2209, 46225, 9, 45369, 2500, 27225, 484, 25921, 400, 24025, 81, 48841, 144, 44521, 1, 52900, 1444, 28561, 169, 22500, 1521, 42849, 100, 52900, 1600, 34596, 36, 29241, 36, 17956, 9, 18225, 1]

key = [0] * 64  
key[0] = ord('P')  


addr = 0x10000
v26 = ~addr
v3 = addr + 1

def solve(key, index, addr, v3):
    if index == len(key)-1:
        print(bytearray(key).decode()) 
        return
    for ch in char:
        v5 = key[index]
        v2 = ord(ch)
        v6 = 2 * v2
        v7 = v2 * v2
        if (v3 + addr) & 1 != 0:
            v8 = v5 + v6
        else:
            v8 = v5 - v6
        v8 &= 0xffffffff
        x = (v7 + v5 * v8) & 0xffffffff
        if x == enc[index]:
            key[index+1] = ord(ch)
            solve(key, index + 1, addr, v3 + 1)
solve(key, 0, addr, v3)
# P1kAlMiG2Kb7FzP5tM1QBI6DSS92c31Apgjk9lVK7dmpdonxRWd2YvlzRhbICCFA
# P1kAlMiG2Kb7FzP5tM1QBI6DSS92c31Apgjk9lVK7dmpdonxRWd2YvlzRhbIO74S
# P1kAlMiG2Kb7FzP5tM1QBI6DSS92c31Apgjk9lVK7dmpdopvPYf0WxnxPjdGAEBE
# P1kAlMiG2Kb7FzP5tM1QBI6DSS92c31Apgjk9lVK7dmpdopvPYf0WxnxPjdGM96Q