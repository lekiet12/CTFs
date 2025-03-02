#include <iostream>
#include <cstring>
#include <cstdint>

uint64_t seed = 0;

uint64_t my_random() {
    seed = 0x5851F42D4C957F2D * seed + 1;
    return (seed >> 33); 
}

void srandom(uint32_t s) {
    seed = s - 1;
}

void decrypt(unsigned char encrypted[], unsigned int seed) {
    unsigned char flag[39]; 
    memcpy(flag, encrypted, 39); 
    srandom(seed);
    for(int i = 0; i < 39; i++) {
        int x = my_random();
        flag[i] ^= (unsigned int) (x % 127);
    }
    if (flag[0] == 80 && flag[1] == 87 && flag[2] == 78 && flag[3] == 77 && flag[4] == 69 && flag[5] == 123){
        printf("Seed: %d\n", seed);
        for (int i = 0; i < 39; i++) {
            printf("%c", flag[i]);
        }
        exit(0);
    }
}

int main() {
    unsigned char encrypted[39] = {32, 52, 12, 29, 47, 45, 13, 75, 59, 111, 24, 21, 93, 108, 47, 22, 66, 87, 102, 27, 22, 120, 7, 52, 28, 43, 108, 102, 123, 37, 65, 81, 85, 58, 77, 93, 95, 37, 107};
    for (unsigned int i = 0; i < 0xffffffff; i++) {
        decrypt(encrypted, i);
        if (i % 0x10000000 == 0){
            printf("Progress: %d%%\n", i / 0x10000000);
        }
    }
}

// PWNME{4baf3723f62a15f22e86d57130bc40c3}