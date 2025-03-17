# from capstone import *
# from capstone.x86 import *

# shell = [  0xD4, 0x4D, 0x91, 0xFD, 0x7C, 0xB9, 0x28, 0x18, 0x18, 0x18, 
#   0x93, 0x58, 0x14, 0x93, 0x58, 0x0C, 0x93, 0x18, 0x93, 0x58, 
#   0x08, 0x45, 0xDB]
# md = Cs(CS_ARCH_X86, CS_MODE_32)
# md.detail = True
# for key in range(0, 256):
#     temp = shell[:]
#     for i in range(len(temp)):
#         temp[i] ^= key
#     print("Key: %d" % key)
#     for i in md.disasm(bytes(temp), 0x1000):
#         print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))

# # Key: 24
# # Key: 10

# # import frida
# # import sys
# # base = 0xbc0000
# # argv = ["sneaky_veh.exe","1c342e1e","b33390b","dc08050","3ef5b765"]
# # device = frida.get_local_device()
# # pid = device.spawn(argv)
# # session = device.attach(pid)
# # script = session.create_script("""
# # Interceptor.attach(ptr('0x00BC12A0'), { 
# #     onEnter: function(args) {
# #         var a1 = args[0]; 
# #         var z = Memory.readU64(a1.add(0));
# #         var x = Memory.readU32(a1.add(0));  
# #         var y = Memory.readU32(a1.add(4));  
# #         console.log("[+] x = 0x" + x.toString(16));
# #         console.log("[+] y = 0x" + y.toString(16));
# #         console.log("[+] z = 0x" + z.toString(16));
# #     }
# # });
# # """)

# # def on_message(message, data):
# #     print(message)

# # script.on('message', on_message)
# # script.load()

# # device.resume(pid)
# # sys.stdin.read()

# # [+] x = 0x43534341
# # [+] y=  0x34323032
# # [+] z = 0x3432303243534341

data = open("./sneaky_veh.exe",'rb').read()
with open("./sneaky_veh_copy.exe",'wb') as f:
    f.write(data)