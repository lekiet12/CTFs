#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#include <iostream>
using namespace std;
#pragma comment(lib, "ntdll.lib")

unsigned int random() {
    return ((rand() ^ 0x123456) - 2023396976) & 0xffffffff;
}

int function(uint16_t *buf, uint8_t *opcode, int64_t *array,uint16_t *tmp_input_buffer,uint32_t pbBuffer) {  
    int index = 0;
    int v19 = 0;
    if (*buf) {
        uint16_t *v20 = buf;
        do {
            ++v19;
            ++v20;
        } while (*v20);
    }
    memcpy(tmp_input_buffer, buf, v19 * sizeof(uint16_t));
    srand(0x12345678);
    int v22 = index;
    
    if ((unsigned int)index < 0x1619) {
        int8_t *input_buffer =(int8_t*)tmp_input_buffer;
        while (1) {
            pbBuffer = 0;
            switch (opcode[v22]) {
                case 0x80: {
                    int v24 = v22 + 2;
                    int v25 = opcode[v22 + 1] >> 4;
                    int v26 = opcode[v24] >> 4;
                    int v27 = opcode[v22 + 1] & 0xF;
                    int v28 = opcode[v24] & 0xF;

                    if (v28 == 10) {
                        v28 = *(int *)&opcode[v22 + 3];
                        v22 += 7;
                    } else {
                        v22 += 3;
                    }
                    index = v22;
                    
                    int64_t *v30; 
                    int64_t *v31;

                    if (v25){
                        if (v25 !=1){
                            v31 = &array[v26];
                            v30 = (int64_t*)&input_buffer[*v31];
                        }
                    }
                    else{
                        v30 = &array[v26];
                        v31 = v30;
                    }
                    uint8_t v32,v33;

                    if (v27){
                        if (v27 == 1){
                            v32 = (uint8_t) input_buffer[*v31];
                        }
                        else{
                            if (v28 == -1){
                                v33 = random();
                                input_buffer =(int8_t*)tmp_input_buffer;
                                v32 = v33;
                                v22 = index;
                            }
                            else{
                                v32 = v28;
                            }
                        }
                    }else{
                        v32 = array[v28];
                    }
                    if (v25) {
                        *(BYTE *)v30 = v32;
                    } else {
                        *v30 = v32;
                    }
                    break;
                }
                case 0x90: {
                    int v34 = v22 + 2;
                    int v35 = opcode[v22 + 1] >> 4;
                    int v36 = opcode[v34] >> 4;
                    int v37 = opcode[v22 + 1] & 0xF;
                    int v38 = opcode[v34] & 0xF;

                    if (v38 == 10) {
                        v38 = *(int *)&opcode[v22 + 3];
                        v22 += 7;
                    } else {
                        v22 += 3;
                    }
                    index = v22;
                    
                    int64_t *v40;
                    int64_t *v41;
                    if (v35){
                        v41 = &array[v36];
                        v40 = (int64_t*)&input_buffer[*v41];
                    }
                    else{
                        v40 = &array[v36];
                        v41 = v40;
                    }
                    uint8_t v42,v43;
                    if (v37){
                        if ( v37 == 1 ){
                            v42 = (unsigned __int8)input_buffer[*v41];
                        }
                        else{
                            if ( v38 == -1 ){
                                v43 = rand();
                                input_buffer = (int8_t *)tmp_input_buffer;
                                v42 = v43;
                                v22 = index;
                            }
                            else
                            {
                                v42 = v38;
                            }
                        }
                    }
                    else{
                        v42 = array[v38];
                    }
                    if (v35) {
                        *(BYTE *)v40 &= v42;
                    } else {
                        *v40 &= v42;
                    }
                    break;
                }
                case 0xA0:
                    int v44 = v22 + 2;
                    int v45 = opcode[v22 + 1] >> 4;
                    int v46 = opcode[v44] >> 4;
                    int v47 = opcode[v22 + 1] & 0xF;
                    int v48 = opcode[v44] & 0xF;
                    if ( v48 == 10 ){
                        v22 += 7;
                        v48 = *(int *)&opcode[v22+3];
                    }
                    else{
                        v22+=3;
                    }
                    index = v22;
                    int64_t *v51;
                    int64_t *v50;
                    if (v45){
                        v51 = &array[v46];
                        v50 = (int64_t *)&input_buffer[*v51];
                    }
                    else{
                        v50 = &array[v46];
                        v51 = v50;
                    }
                    uint8_t v52,v53;
                    if (v47){
                        if (v47 == 1){
                            v52 = (uint8_t)input_buffer[*v51];
                        }
                        else{
                            if (v48 == -1){
                                v53 = random();
                                input_buffer = (int8_t*)tmp_input_buffer;
                                v52 = v53;
                                v22 = index;
                            }
                            else{
                                v52 = v48;
                            }
                        }
                    }
                    else{
                        v52 = array[v48];
                    }
                    if ( v45 )
                        *(BYTE *)v50 += v52;
                    else
                        *v50 += v52;
                
                case 0xB0:
                    int v54 = v22 + 2;
                    int v55 = opcode[v22 + 1] >> 4;
                    int v56 = opcode[v54] >> 4;
                    int v57 = opcode[v22 + 1] & 0xF;
                    int v58 = opcode[v54] & 0xF;
                    if ( v58 == 10 ){
                        v22 += 7;
                        v58 = *(int *)&opcode[v22 + 3];
                    }
                    else{
                        v22 +=3;
                    }
                    index = v22;
                    if (v52)
                // Các trường hợp khác tương tự
                case 0xE0:
                    // send(v18, &input_buffer[array[0]], 64, 0);
                    for (int i = array[0]; i < array[0] + 64; i++) {
                        printf("%02x ", input_buffer[i]);
                    }
                    return 1;
                    break;
                case 0xF0: {
                    uint8_t v74;
                    uint8_t flag[64] = {0};
                    size_t byteRead;
                    FILE *file2 = fopen("flag.txt", "rb");
                    if (file2) {
                        v74 = opcode[v22 + 1];
                        byteRead = fread(flag, sizeof(uint8_t), sizeof(flag), file2);
                        fclose(file2);
                        for (int i = 0; i < 64; i++) {
                            flag[i] ^= 0x37;
                            flag[i] -= 0x13;
                            input_buffer[0x200 + i] = flag[i];
                        }
                    }
                    input_buffer = (int8_t *)tmp_input_buffer;
                    v22 = index + 2;
                    index += 2;
                    break;
                }
                default:
                    return 1;
            }
        }
    }
    return 0;
}

int main() {
    UINT16 buffer[]={0x5c,0x3f,0x3f,0x5c,0x44,0x3a,0x5c,0x43,0x54,0x46,0x5c,0x41,0x53,0x43,0x49,0x53,0x5c,0x45,0x7a,0x52,0x65,0x76,0x5c,0x66,0x6c,0x61,0x67,0x2e,0x74,0x78,0x74,0,0,0x14,0x06,0x34,0x29,0x3d,0x31,0x1d,0x07,0x3a,0x3c,0x2c,0x32,0x2f,0x1f,0x1b,0x3e,0x10,0x13,0x24,0x15,0x2b,0x25,0x39,0x1c,0x01,0x17,0x3b,0x20,0x0d,0x30,0x1a,0x3f,0x27,0x1e,0x33,0x22,0x35,0x16,0x05,0x09,0x36,0x2a,0x0b,0x12,0x0a,0x2e,0x37,0x38,0x08,0x03,0x02,0x19,0x26,0x04,0x23,0x18,0x11,0x28,0x0f,0x0e,0x2d,0x21,0x0c};
    int64_t array[16]={0};
    uint8_t opcode[5660]={0};
    FILE *file1 = fopen("out.bin", "rb");
    if (file1) {
        size_t byteread = fread(opcode, sizeof(uint8_t), sizeof(opcode), file1);
        fclose(file1);   
    }
    uint16_t tmp_input_buffer[0x400]={};
    function((uint16_t*)buffer,(uint8_t*)opcode,(int64_t*)array,(uint16_t*)tmp_input_buffer,0);
    return 0;
}