#include<windows.h>
#include<stdio.h>
int main() {
    unsigned int flag[64] = {0};
    unsigned enc[64] = {
  0x72, 0xBB, 0xB2, 0xCD, 0x58, 0xB2, 0x81, 0x0E, 0xA4, 0xB1, 
  0xED, 0xDB, 0x84, 0xB2, 0xC0, 0xAA, 0x60, 0xD0, 0xE8, 0xE8, 
  0xB0, 0x12, 0x81, 0x1E, 0xED, 0xD0, 0xF3, 0x05, 0xB0, 0xB1, 
  0x04, 0x04, 0x7D, 0xF3, 0xC0, 0xE8, 0xED, 0x12, 0xF3, 0xC2, 
  0x7D, 0x0E, 0x0E, 0x0E, 0x7D, 0x04, 0xC0, 0xBB, 0xED, 0xB1, 
  0x81, 0xED, 0xA4, 0xCF, 0xC0, 0x68, 0x84, 0xD0, 0xE2, 0x1B, 
  0xC2, 0x58, 0x30, 0x30
};
    unsigned int option[64] = {
        0xc0000094, 0xc0000005, 0xc0000096, 0xc0000005, 0xc0000094, 0xc0000096, 0xc000001d, 0xc0000094, 0xc0000094, 0xc000001d, 0xc0000094, 0xc000001d, 0xc0000096, 0xc0000096, 0xc0000094, 0x80000003, 0xc0000094, 0xc0000096, 0xc0000096, 0xc0000096, 0xc000001d, 0xc0000094, 0xc000001d, 0x80000003, 0xc0000005, 0xc0000096, 0xc0000094, 0xc0000005, 0xc000001d, 0xc000001d, 0x80000003, 0xc0000005, 0xc000001d, 0xc0000094, 0xc0000094, 0xc0000096, 0xc0000005, 0xc0000094, 0xc0000094, 0xc0000096, 0xc000001d, 0xc0000094, 0xc000001d, 0xc000001d, 0xc000001d, 0x80000003, 0xc0000094, 0xc0000005, 0xc0000005, 0xc000001d, 0xc000001d, 0xc0000094, 0xc0000094, 0xc0000005, 0xc0000094, 0xc000001d, 0xc0000096, 0xc0000096, 0xc0000005, 0x80000003, 0xc0000096, 0xc0000094, 0xc0000096, 0xc0000096
};
    int i,j,k,n,m;
    for (int index = 0; index < 64; ++index) {
        INT32 v3 = option[index];

        for (int num = 10; num < 128; ++num) {
            flag[index] = num;
            unsigned int v0 = flag[index];
            switch (option[index]) {
                case 0x80000003:
                    for (i = 0; i < 10; i = i + 1) {
                        flag[index] = ((flag[index] + 0x45) ^ (i + 0x33)) + (v0 ^ (byte)i) * 7;
                        flag[index] &=0xff;
                    }
                    break;
                case 0xC0000005:
                    for (j = 0; j < 10; j = j + 1) {
                        flag[index] = (flag[index] + 85 + j) ^ 7;
                        flag[index] &=0xff;
                    }
                    break;
                case 0xC000001D:
                    for (k = 0; k < 10; k = k + 1) {
                        byte bVar3 = (byte)k;
                        byte bVar2 = (byte)(k >> 0x1f);
                        flag[index] = (v0 >> ((bVar3 & 1 ^ bVar2) - bVar2 & 0x1f)) +
                                        bVar3 + (flag[index] ^ v0 + bVar3) * 91 ^
                                        (flag[index] << ((k % 3) & 0x1f)) & 0x4f;
                        flag[index] &=0xff;
                    }
                    break;
                case 0xC0000094:
                        for (m = 0; m < 10; m = m + 1) {
                            byte bVar2 = (byte)m;
                            flag[index] = (flag[index] + bVar2 * 5 + v0 * 3 ^ v0 + bVar2) * 93 + (v0 ^ bVar2);
                            flag[index] &=0xff;
                        }
                    break;
                case 0xC0000096:
                    for (n = 0; n < 10; n = n + 1) {
                        flag[index] = (char)((long long)
                               ((int)(char)v0 +
                               n + ((char)flag[index] + 0x2d +
                                    ((int)(char)v0 << ((byte)((long long)n % 3) & 0x1f)) ^ n * 7) *
                                   0x4d) % 0xff);
                        flag[index] &=0xff;
                    }
                    break;
            }
            if (flag[index] == enc[index]) {
                printf("%c", num);
                // break;
            }
        }
        printf("\n");
    }
    return 0;
}
//  S01BQ1RGe2hvd19tYW55X3RpbWVzX2FyZV95b3VfZGllZF90b2RheT9odWg/fQ==  
//  KMACTF{how_many_times_are_you_died_today?huh?}