
from idaapi import *
import idc
import ida_dbg

addr_mem1 = 0x0000555556D3F080
addr_mem2 = 0x0000555555684DE0
addr_mem3 = 0x00005555555AF640

arr_mem1 = []
arr_mem2 = []
arr_mem3 = []

for i in range(100):
    addr1 = get_qword(addr_mem1+8*i)
    addr2 = get_qword(addr_mem2+8*i)
    addr3 = get_dword(addr_mem3+8*i)
    for j in range(addr1,addr1+0x3A2E*4*4,4):
        arr_mem1.append(get_dword(i))
    for j in range(addr2,addr2+0x886*4*4,4):
        arr_mem2.append(get_dword(i))
    for j in range(addr3,addr3+0x3A2E*4*4,4):
        arr_mem3.append(get_dword(i))
with open("array.h","w") as f:
    f.write("#include<stdint.h>\n")
    f.write("uint32_t mem1[] = "+str(arr_mem1).replace("[","{").replace("]","}")+";\n")
    f.write("uint32_t mem2[] = "+str(arr_mem2).replace("[","{").replace("]","}")+";\n")
    f.write("uint32_t mem3[] = "+str(arr_mem3).replace("[","{").replace("]","}")+";\n")





# from idaapi import *
# import idc
# import ida_dbg

# BREAKPOINT_ADDRESS = 0x0000555555557973
# array = []
# def monitor():
#     rcx = get_reg_val('rcx')
#     rdx = get_reg_val('rdx')
#     eax = get_reg_val('eax')
#     addr_val = 0x55555ed3f3c4
#     enc = eax - get_dword(addr_val)
#     array.append(enc)

#     idaapi.continue_process()

# ida_dbg.add_bpt(BREAKPOINT_ADDRESS, 0, idaapi.BPT_SOFT)

# class MyHandler(idaapi.DBG_Hooks):
#     def dbg_bpt(self, tid, ea):
#         monitor()
#         with open("array2.txt", "w") as f:
#             f.write(str(array))
#         return 0

# debugger = MyHandler()
# debugger.hook()

# print(f"Breakpoint set at {BREAKPOINT_ADDRESS:X}")
# print("Run the debugger to start monitoring")