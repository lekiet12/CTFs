import ctypes

libc = ctypes.CDLL("libc.so.6")
libc.srand(0x12345678)
def rand():
    return (libc.rand()^ 0x123456) - 0x789A9670
opcode = list(open("out.bin",'rb').read())
array = [0]*16
input_buffer = [0]*0x500
flag = list(open("flag.txt",'rb').read())
flag = [((i+0x13)^0x37)&0xff for i in flag]
index  = 0
while True:
    if opcode[index] == 0xF0:
        v74 = opcode[index+1]
        for i in range(array[v74 & 0xf],array[v74 & 0xf]+64):
            input_buffer[i] = flag[i-array[v74 & 0xf]]
        index +=2
        continue

    if opcode[index] == 0x80:
        v24 = index + 2
        v25 = opcode[index + 1] >> 4
        v26 = opcode[v24] >> 4
        v27 = opcode[index + 1] & 0xF
        v28 = opcode[v24] & 0xF
        
        if v28 == 10:
            v29 = index + 3
            index +=7
            v28 = opcode[v29+3] << 24 | opcode[v29+2] << 16 | opcode[v29+1] << 8 | opcode[v29]
        else:
            index +=3

        if v25 == 1:
            v31 = array[v26]
            v30 = input_buffer[v31]
        else:
            v30 = array[v26]
            v31 = v30 
        if v27:
            if v27 == 1:
                v32 = input_buffer[v31] & 0xff
            else:
                if v28 == 0xFFFFFFFF:
                    v33 = rand()
                    v32 = v33 
                else:
                    v32 = v28
        else:
            v32 = array[v28]
        if v25:
            input_buffer[v31] = v32 & 0xFF  
        else:
            array[v26] = (v32) & 0xff
            array[v26+1] = ((v32) >> 8)&0xff
            array[v26+2] = ((v32) >> 16)&0xff
            array[v26+3] = ((v32) >> 24)&0xff
        # print("mov")
    elif opcode[index] == 0x90:
        v24 = index + 2
        v25 = opcode[index + 1] >> 4
        v26 = opcode[v24] >> 4
        v27 = opcode[index + 1] & 0xF
        v28 = opcode[v24] & 0xF
        
        if v28 == 10:
            v29 = index + 3
            index +=7
            v28 = opcode[v29+3] << 24 | opcode[v29+2] << 16 | opcode[v29+1] << 8 | opcode[v29]
        else:
            index +=3
        if v25 == 1:
            v31 = array[v26]
            v30 = input_buffer[v31+3] << 24 | input_buffer[v31+2] << 16 | input_buffer[v31+1] << 8 | input_buffer[v31]
        else:
            v30 = array[v26]
            v31 = v30 
        if v27:
            if v27 == 1:
                v32 = input_buffer[v31] & 0xff
            else:
                if v28 == 0xFFFFFFFF:
                    v33 = rand()
                    v32 = v33 
                else:
                    v32 = v28
        else:
            v32 = array[v28]
        if v25:
            input_buffer[v31] &= v32 & 0xFF  
        else:
            array[v26] &= (v32) & 0xff
            array[v26+1] &= ((v32) >> 8)&0xff
            array[v26+2] &= ((v32) >> 16)&0xff
            array[v26+3] &= ((v32) >> 24)&0xff
        # print("and")
    elif opcode[index] == 0xA0:
        v24 = index + 2
        v25 = opcode[index + 1] >> 4
        v26 = opcode[v24] >> 4
        v27 = opcode[index + 1] & 0xF
        v28 = opcode[v24] & 0xF
        
        if v28 == 10:
            v29 = index + 3
            index +=7
            v28 = opcode[v29+3] << 24 | opcode[v29+2] << 16 | opcode[v29+1] << 8 | opcode[v29]
        else:
            index +=3
        if v25 == 1:
            v31 = array[v26]
            v30 = input_buffer[v31]
        else:
            v30 = array[v26]
            v31 = v30 
        if v27:
            if v27 == 1:
                v32 = input_buffer[v31] & 0xff
            else:
                if v28 == 0xFFFFFFFF:
                    v33 = rand()
                    v32 = v33 
                else:
                    v32 = v28
        else:
            v32 = array[v28]
        if v25:
            input_buffer[v31] += v32 & 0xFF  
            input_buffer[v31] &=0xff
        else:
            array[v26] += (v32) & 0xff
            array[v26] &=0xff
            array[v26+1] += ((v32) >> 8)&0xff
            array[v26] &=0xff
            array[v26+2] += ((v32) >> 16)&0xff
            array[v26] &=0xff
            array[v26+3] += ((v32) >> 24)&0xff
            array[v26] &=0xff
        # print("add")
    elif opcode[index] == 0xB0:
        v24 = index + 2
        v25 = opcode[index + 1] >> 4
        v26 = opcode[v24] >> 4
        v27 = opcode[index + 1] & 0xF
        v28 = opcode[v24] & 0xF
        
        if v28 == 10:
            v29 = index + 3
            index +=7
            v28 = opcode[v29+3] << 24 | opcode[v29+2] << 16 | opcode[v29+1] << 8 | opcode[v29]
        else:
            index +=3
        if v25 == 1:
            v31 = array[v26]
            v30 = input_buffer[v31]
        else:
            v30 = array[v26]
            v31 = v30 
        if v27:
            if v27 == 1:
                v32 = input_buffer[v31] & 0xff
            else:
                if v28 == 0xFFFFFFFF:
                    v33 = rand()
                    v32 = v33 
                else:
                    v32 = v28
        else:
            v32 = array[v28]
        if v25:
            input_buffer[v31] -= v32 & 0xFF  
            input_buffer[v31] &=0xff
        else:
            array[v26] -= (v32) & 0xff
            array[v26] &=0xff
            array[v26+1] -= ((v32) >> 8)&0xff
            array[v26] &=0xff
            array[v26+2] -= ((v32) >> 16)&0xff
            array[v26] &=0xff
            array[v26+3] -= ((v32) >> 24)&0xff
            array[v26] &=0xff
        # print("sub")
    elif opcode[index] == 0xC0:
        v24 = index + 2
        v25 = opcode[index + 1] >> 4
        v26 = opcode[v24] >> 4
        v27 = opcode[index + 1] & 0xF
        v28 = opcode[v24] & 0xF
        
        if v28 == 10:
            v29 = index + 3
            index +=7
            v28 = opcode[v29+3] << 24 | opcode[v29+2] << 16 | opcode[v29+1] << 8 | opcode[v29]
        else:
            index +=3
        if v25 == 1:
            v31 = array[v26]
            v30 = input_buffer[v31]
        else:
            v30 = array[v26]
            v31 = v30 
        if v27:
            if v27 == 1:
                v32 = input_buffer[v31] & 0xff
            else:
                if v28 == 0xFFFFFFFF:
                    v33 = rand()
                    v32 = v33 
                else:
                    v32 = v28
        else:
            v32 = array[v28]
        if v25:
            input_buffer[v31] ^= v32 & 0xFF 
            input_buffer[v31] &=0xff 
        else:
            array[v26] ^= (v32) & 0xff
            array[v26+1] ^= ((v32) >> 8)&0xff
            array[v26+2] ^= ((v32) >> 16)&0xff
            array[v26+3] ^= ((v32) >> 24)&0xff
        # print("xor")
    elif opcode[index] == 0xE0:
        print(input_buffer[array[0]:array[0]+64])
        print(bytearray(input_buffer[array[0]:array[0]+64]).hex())
        # print("Send")
        break
    