#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Rotate right
uint32_t ror(uint32_t value, int shift) {
    return (value >> shift) | (value << (32 - shift));
}
// rotate left
uint32_t rol(uint32_t value, int shift) {
    return (value << shift) | (value >> (32 - shift));
}
 
int main(){
    uint32_t cipher[8]={878342545, 3703870730, 2329362254, 1611063022, 3027564196, 2518701901, 2142918248, 1170946430};
    uint32_t rounds = 0x24F8896;
    uint32_t key[8]={0xE8D2BFCD,0x009D45CB,0x1867CBC9,0x303251C7,0x47FCD7C5,0x5FC75DC3,0x7791E3C1,0x8F5C69BF};
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j <= rounds; j++) {
            cipher[i] = ror(cipher[i], 3);
        }
    }
    for (int i = 0; i < 8; i++) {
        cipher[i] ^= key[i];
    }
    for (int i = 0; i < 8; i++) {
        printf("%c%c%c%c",
               (cipher[i] & 0xFF), 
               (cipher[i] >> 8) & 0xFF, 
               (cipher[i] >> 16) & 0xFF, 
               (cipher[i] >> 24) & 0xFF);
    }
    printf("\n");
    return 0;
}
// V3r1l0g2Cpp_by_v3r1l4t0r