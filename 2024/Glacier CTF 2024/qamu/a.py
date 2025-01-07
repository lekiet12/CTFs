from pwn import *
import angr
import claripy

p = angr.Project("/bin/id", auto_load_libs=False)

ADDR = 0x7000000
STACK_ADDR = 0xd0000000
INPUT_ADDR = 0x20000000

state = p.factory.blank_state(addr=ADDR)

sc = open("./shellcode", "rb").read()


x = [claripy.BVS(f"flag{i}", 64) for i in range(0x20)]

flag = claripy.Concat(*x)

state.memory.store(ADDR, sc)
state.memory.store(INPUT_ADDR, flag)


state.regs.rax = 0
state.regs.rbx = 0
state.regs.rcx = 0
state.regs.rdx = 0
state.regs.rdi = INPUT_ADDR
state.regs.rsi = 0
state.regs.r8 = 0
state.regs.r9 = 0
state.regs.r10 = 0
state.regs.r11 = 0
state.regs.r12 = 0
state.regs.r13 = 0x70000000
state.regs.r14 = 0
state.regs.r15 = 0x4018bb
state.regs.rbp = 0
state.regs.rsp = STACK_ADDR

simgr = p.factory.simulation_manager(state)

while len(simgr.active):
    simgr.step()

ret = simgr.unconstrained[0].regs.rax

s = claripy.Solver()

vs = []

s.add(ret != 0)
for v in x:
    vs.append(s.eval(v, 1)[0])

vs = [p64(v)[-1] for v in vs]
print(bytes(vs))