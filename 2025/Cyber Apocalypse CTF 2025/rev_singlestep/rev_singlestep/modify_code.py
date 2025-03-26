import idaapi
import idc


with open("log.txt", "w") as f:

    start = 0x00000000000043E0
    end = 0x0000000000008FC3
    addr = set()

    current_addr = start
    while current_addr <= end:
        idc.del_items(current_addr, 0, 1)
        idc.create_byte(current_addr)
        current_addr += 1

    current_addr = start
    while current_addr <= end:
        if idc.create_insn(current_addr):
            instruction_size = idc.get_item_size(current_addr)
            mnemonic = idc.print_insn_mnem(current_addr).lower()
            if mnemonic in ("pushfq", "popfq"):
                current_addr += instruction_size
            else:
                current_addr += 1
        else:
            current_addr += 1

    def patch_nop(start, size):
        for i in range(size):
            idc.patch_byte(start + i, 0x90)
    current_addr = start
    checking = False
    pushfq_addr = []
    popfq_addr = []
    index = 0
    while current_addr <= end:
        if current_addr in addr:
            if idc.create_insn(current_addr):
                current_addr += idc.get_item_size(current_addr)
            else:
                current_addr += 1
            continue

        if not idc.create_insn(current_addr):
            current_addr += 1
            continue

        instruction_size = idc.get_item_size(current_addr)
        mnemonic = idc.print_insn_mnem(current_addr).lower()

        if mnemonic == "pushfq":
            pushfq_addr.append(current_addr)
            checking = True
            index += 1
        elif mnemonic == "popfq":
            popfq_addr.append(current_addr)
            checking = False

        if mnemonic in ("pushfq", "popfq"):
            current_addr += instruction_size
            continue

        if index % 2 == 1 and checking and mnemonic == "xor":
            try:
                disasm = idaapi.generate_disasm_line(current_addr, 0).lower()
                if "dword" in disasm and instruction_size == 10:
                    addr_patch = (idc.get_wide_dword(current_addr + 2) + current_addr + instruction_size) & 0xffff
                    if addr_patch not in addr:
                        addr.add(addr_patch)
                        number_xor = idc.get_wide_dword(current_addr + 6)
                        number_patch = idc.get_wide_dword(addr_patch)
                        number_patch ^= number_xor
                        idc.patch_dword(addr_patch, number_patch)
                        f.write(f"Patched DWORD at {hex(addr_patch)}: {hex(number_patch)}\n")
                elif "word" in disasm and instruction_size == 9:
                    addr_patch = (idc.get_wide_word(current_addr + 3) + current_addr + instruction_size) & 0xffff
            
                    if addr_patch not in addr:
                        addr.add(addr_patch)
                        number_xor = idc.get_wide_word(current_addr + 7)
                        number_patch = idc.get_wide_word(addr_patch)
                        number_patch ^= number_xor
                        idc.patch_word(addr_patch, number_patch)
                        f.write(f"Patched WORD at {hex(addr_patch)}: {hex(number_patch)}\n")
                elif "byte" in disasm and instruction_size == 7:
                    addr_patch = (idc.get_wide_dword(current_addr + 2) + current_addr + instruction_size) & 0xffff
                    if addr_patch not in addr:
                        addr.add(addr_patch)
                        number_xor = idc.get_wide_byte(current_addr + 6)
                        number_patch = idc.get_wide_byte(addr_patch)
                        number_patch ^= number_xor
                        idc.patch_byte(addr_patch, number_patch)
                        f.write(f"Patched BYTE at {hex(addr_patch)}: {hex(number_patch)}\n")
            except Exception as e:
                print(f"Error at {hex(current_addr)}: {e}")
                current_addr += instruction_size
                continue
        current_addr += instruction_size
    for i in range(len(pushfq_addr)):
        patch_nop(pushfq_addr[i], popfq_addr[i] - pushfq_addr[i]+1)
    print("Patching complete.")


