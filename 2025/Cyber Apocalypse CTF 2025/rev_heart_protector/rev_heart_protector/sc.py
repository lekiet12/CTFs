import idaapi
import ida_dbg
import time
def get_all_registers():
    """Get all register values for x64 architecture after ensuring debugger is synchronized."""
    ida_dbg.refresh_debugger_memory()  
    # time.sleep(0.1) 
    
    register_names = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp",
                      "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "rip"]
    registers = {}

    for reg in register_names:
        value = idaapi.get_reg_val(reg)
        registers[reg] = value if value is not None else "N/A"

    return registers


class VMDebugHook(ida_dbg.DBG_Hooks):
    def __init__(self, breakpoint_list):
        super().__init__()
        self.count = 0
        self.log_file = open("log.txt", "w")
        self.breakpoint_list = breakpoint_list

    def dbg_process_start(self, pid, tid, ea, name, base, size):
        print(f"Process started: PID={pid}, TID={tid}, EA={hex(ea)}")
        self.continue_execution()
        return 0

    def dbg_process_exit(self, pid, tid, ea, code):
        print(f"Process exited with code {code}. Unhooking...")
        self.log_file.close()
        self.unhook()
        return 0

    def dbg_run_to(self, tid, ea):
        print(f"Running to {hex(ea)}")
        self.continue_execution()
        return 0

    def dbg_bpt(self, tid, ea):
        """Handle breakpoint hits and log detailed VM operations."""
        print(f"Breakpoint hit at {hex(ea)}, TID={tid}")
        post_registers = get_all_registers()
        registers = post_registers

        breakpoint_ops = {
            0: f"vm->stack[{registers['rax']}] = vm->memory[{registers['rdi']}] = {registers['rcx'] & 0xff}\n",
            1: f"vm->memory[{registers['rdi']}] = {registers['rax']}\n",
            2: f"++vm->memory[{registers['rdi']}]\n",
            3: f"--vm->memory[{registers['rdi']}]\n",
            4: f"vm->memory[{registers['rdi']}] += vm->memory[{registers['rbp']}] = {registers['rax']}\n",
            5: f"vm->memory[{registers['rdi']}] += {registers['r14']}\n",
            6: f"vm->memory[{registers['rdi']}] -= {registers['r14']}\n",
            7: f"vm->memory[{registers['rdi']}] = __ROR4__(vm->memory[{registers['rdi']}], 32 - ({registers['rbp']} & 0x1F)); | ror = {idaapi.get_dword(registers['rbx'] + registers['rdi']*4 + 0x90)} >> {registers['rcx'] & 0xff}\n",
            8: f"vm->memory[{registers['rdi']}] = __ROR4__(vm->memory[{registers['rdi']}], {registers['r12']}); | ror = {idaapi.get_dword(registers['rbx'] + registers['rdi']*4 + 0x90)} >> {registers['rcx'] & 0xff}\n",
            9: f"v15 = vm->memory[{registers['rbp']}]\n",
            10: f"vm->memory[{registers['rdi']}] = {registers['r12']}\n",
            11: f"vm->memory[{registers['r14']}] == {registers['r12']} | {idaapi.get_dword(registers['rbx'] + registers['r14']*4 + 0x90)} == {registers['r12']}\n",
            12: f"vm->memory[{registers['rbp']}] == vm->memory[{registers['r13']}] | {idaapi.get_dword(registers['rbx'] + registers['rbp']*4 + 0x90)} == {registers['rax']}\n",
            13: f"vm->regs[0] = vm->memory[{registers['rdi']}] == 0\n",
            14: f"mov key to stack\n",
            15: f"vm->memory[{registers['rdi']}] *= {registers['rbp']} | x = {(registers['rbp'] & 0xffffffff)} * {idaapi.get_dword(registers['rbx'] + registers['rdi']*4 + 0x90)}\n",
            16: f"v141 = vm->memory[{registers['rbp']}] * *((_DWORD *)&vm->size + v140) * {registers['rax']} | x = {(registers['rax'] & 0xffffffff)} * {idaapi.get_dword(registers['rbx'] + registers['rbp']*4 + 0x90)}\n",
            17: f"v141 = vm->memory[{registers['rbp']}] ^ *((_DWORD *)&vm->size + v140) ^ {registers['rax']} | x = {(registers['rax'] & 0xffffffff)} ^ {idaapi.get_dword(registers['rbx'] + registers['rbp']*4 + 0x90)}\n"
        }

        if ea in self.breakpoint_list:
            op_index = self.breakpoint_list.index(ea)
            op_str = breakpoint_ops[op_index]
            self.log_file.write(f"Operation: {op_str}")
            if 'rdi' in op_str and registers['rdi'] != 'N/A' and registers['rbx'] != 'N/A':
                mem_addr = registers['rbx'] + registers['rdi'] * 4 + 0x90
                mem_val = idaapi.get_dword(mem_addr)
                self.log_file.write(f"Memory at {hex(mem_addr)}: {hex(mem_val)}\n")
            self.log_file.flush()

        self.continue_execution()
        return 0

    def continue_execution(self):
        """Continue process execution."""
        idaapi.continue_process()
        self.count += 1
        print(f"Continued execution #{self.count}")

# Setup breakpoints
offset = [55260, 56824, 55522, 55627, 55799, 56113, 56288, 56470, 56665, 56817, 
          56982, 57145, 57398, 57588, 59709, 59889, 60107, 60290]
base = 0x00007FF607701000
breakpoint_list = [base + i for i in offset]

for addr in breakpoint_list:
    if idaapi.add_bpt(addr, 0, idaapi.BPT_SOFT):
        print(f"Breakpoint set at {hex(addr)}")
    else:
        print(f"Failed to set breakpoint at {hex(addr)}")

try:
    debug_hook = VMDebugHook(breakpoint_list)
    if debug_hook.hook():
        print("Debugger hook installed successfully.")
    else:
        print("Failed to install debugger hook.")
    idaapi.continue_process()
except Exception as e:
    print(f"Error during setup: {str(e)}")