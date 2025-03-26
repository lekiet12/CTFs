import struct
 
OPCODE_TABLE = {
0x00: {"mnemonic": "PUSH", "operands": ["Rs"], "size": 2},
0x01: {"mnemonic": "MOV", "operands": ["Rd", "[Rs]"], "size": 3},
0x02: {"mnemonic": "INC", "operands": ["Rd"], "size": 2},
0x03: {"mnemonic": "DEC", "operands": ["Rd"], "size": 2},
0x04: {"mnemonic": "ADD", "operands": ["Rd", "Rs"], "size": 3},
0x05: {"mnemonic": "ADD", "operands": ["Rd", "Imm32"], "size": 6},
0x06: {"mnemonic": "ADDZ", "operands": ["Rd", "Imm32"], "size": 6},
0x07: {"mnemonic": "SUB", "operands": ["Rd", "Imm32"], "size": 6},
0x08: {"mnemonic": "ROL", "operands": ["Rd", "Imm32"], "size": 6},
0x09: {"mnemonic": "ROR", "operands": ["Rd", "Imm32"], "size": 6},
0x0A: {"mnemonic": "MOV", "operands": ["Rd", "Rs"], "size": 3},
0x0B: {"mnemonic": "MOV", "operands": ["Rd", "Imm32"], "size": 6},
0x0C: {"mnemonic": "CMP", "operands": ["Rd", "Imm32"], "size": 6},
0x0D: {"mnemonic": "CMP", "operands": ["Rd", "Rs"], "size": 3},
0x0E: {"mnemonic": "TEST", "operands": ["Rd"], "size": 2}, # set ZF true if zero
0x0F: {"mnemonic": "JMP", "operands": ["Imm16"], "size": 3},
0x10: {"mnemonic": "JZ1", "operands": ["Imm16"], "size": 3},
0x11: {"mnemonic": "JBE", "operands": ["Imm16"], "size": 3},
0x12: {"mnemonic": "JAE", "operands": ["Imm16"], "size": 3},
0x13: {"mnemonic": "JNZ1", "operands": ["Imm16"], "size": 3},
0x14: {"mnemonic": "JZ2", "operands": ["Imm16"], "size": 3},
0x15: {"mnemonic": "JNZ2", "operands": ["Imm16"], "size": 3},
0x16: {"mnemonic": "CALL", "operands": ["Imm16"], "size": 3},
0x17: {"mnemonic": "POP_KEY", "operands": [], "size": 1},
0x18: {"mnemonic": "MUL", "operands": ["Rd", "Imm32"], "size": 6},
0x19: {"mnemonic": "MUL", "operands": ["Rd", "Rs"], "size": 3},
0x1A: {"mnemonic": "XOR", "operands": ["Rd", "Rs"], "size": 3},
0x1B: {"mnemonic": "LOAD", "operands": ["Rd", "[Rs]"], "size": 3},
0x1C: {"mnemonic": "RET", "operands": [], "size": 1},
}
 
 
def disassemble(bytecode):
    ip = 5
    output = []
 
    while ip < len(bytecode):
        opcode = bytecode[ip]
 
        if opcode not in OPCODE_TABLE:
            output.append(
                f"{ip:04X}: DB 0x{opcode:02X} ({bytes([opcode])}) (UNKNOWN OPCODE)"
            )
            ip += 1
            continue
 
        entry = OPCODE_TABLE[opcode]
        mnemonic = entry["mnemonic"]
        operands = []
        operand_bytes = bytecode[ip + 1 : ip + entry["size"]]
        op_ptr = 0
 
        for operand_type in entry["operands"]:
            if operand_type == "Rd" or operand_type == "Rs":
                operands.append(f"R{operand_bytes[op_ptr]}")
                op_ptr += 1
            elif "Imm32" in operand_type:
                imm = struct.unpack("<I", operand_bytes[op_ptr : op_ptr + 4])[0]
                operands.append(f"0x{imm:08X}")
                op_ptr += 4
            elif "Imm16" in operand_type:
                imm = struct.unpack("<H", operand_bytes[op_ptr : op_ptr + 2])[0]
                operands.append(f"0x{imm:04X}")
                op_ptr += 2
            elif "Imm8" in operand_type:
                operands.append(f"0x{operand_bytes[op_ptr]:02X}")
                op_ptr += 1
            elif "[" in operand_type:
                # Memory operand
                if "Rs" in operand_type:
                    operands.append(f"[R{operand_bytes[op_ptr]}]")
                    op_ptr += 1
                else:
                    imm = struct.unpack("<I", operand_bytes[op_ptr : op_ptr + 4])[0]
                    operands.append(f"[0x{imm:08X}]")
                    op_ptr += 4
 
        assert op_ptr + 1 == entry["size"], f"{entry['mnemonic']}"
 
        # Format instruction
        operands_str = ", ".join(operands)
        output.append(f"{ip:04X}: {mnemonic:6} {operands_str}")
 
        ip += entry["size"]
 
    return "\n".join(output)
 
 
if __name__ == "__main__":
    with open("code.bin", "rb") as f:
        code = f.read()
 
    print("=== Disassembly Output ===")
    print(disassemble(code))