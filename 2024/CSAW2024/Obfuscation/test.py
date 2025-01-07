
# 00005555555851A5 00007FFFFFFFDEA0
# 0x00007FFFFFFFD510 0x00007FFFF7FA2220
import gdb
import string

optimized = string.ascii_letters + string.digits + " "
optimized += "".join(chr(x) for x in range(0x20, 0x7f) if chr(x) not in optimized)

ge = gdb.execute
parse = gdb.parse_and_eval
BASE = 0x555555554000

ge("aslr off")
ge("del 1-40")
ge(f"b*{BASE+0x297AD}")

def print_flag():
    global flag
    print('=' * 50)
    print(f"{flag = }")
    print('=' * 50)

flag = ""
while len(flag) != 34:
    for char in optimized:
        with open("guess.txt", "w") as file:
            file.write(flag + char)
            
        ge(f"r < guess.txt")
        for _ in range(len(flag)):
            ge("c")
        
        eax = int(parse("$eax"))
        ecx = int(parse("$ecx"))

        if eax == ecx:
            flag += char
            print_flag()
            break
    else:
        print("failed to find next char ):")
        print(f"{flag = }")
        exit(1)

print_flag()

# flag = 'wh47 15 7h3 r1ck 457l3y p4r4d0x?'
# csawctf{5h0u70u7_70_@53hn40u1_f0r_7h3_r1ck_457l3y_p4r4d0x}