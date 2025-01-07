#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include "defs.h"

int size_seed = 6;
unsigned char seed_rand[6] = { 0x59, 0x42, 0x80, 0xE7, 0x12, 0x2C};
unsigned char array[2560]={0};
unsigned char key[16]={0};

void init(){
  int v1; // [rsp+Ch] [rbp-B4h]
  int i; // [rsp+10h] [rbp-B0h]
  int j; // [rsp+14h] [rbp-ACh]
  unsigned int seed; // [rsp+18h] [rbp-A8h]
  __int16 v5; // [rsp+1Ch] [rbp-A4h]
  int v6[38]; // [rsp+20h] [rbp-A0h]
  unsigned __int64 v7; // [rsp+B8h] [rbp-8h]

  v6[0] = 1;
  v6[1] = 3;
  v6[2] = 5;
  v6[3] = 7;
  v6[4] = 11;
  v6[5] = 13;
  v6[6] = 17;
  v6[7] = 19;
  v6[8] = 23;
  v6[9] = 29;
  v6[10] = 31;
  v6[11] = 37;
  v6[12] = 41;
  v6[13] = 43;
  v6[14] = 47;
  v6[15] = 53;
  v6[16] = 59;
  v6[17] = 61;
  v6[18] = 67;
  v6[19] = 71;
  v6[20] = 73;
  v6[21] = 79;
  v6[22] = 83;
  v6[23] = 89;
  v6[24] = 97;
  v6[25] = 101;
  v6[26] = 103;
  v6[27] = 107;
  v6[28] = 109;
  v6[29] = 113;
  v6[30] = 127;
  v6[31] = 131;
  v6[32] = 137;
  v6[33] = 139;
  v6[34] = 149;
  for ( i = 1; i <= (unsigned __int8)size_seed; ++i )
  {
    if ( i == (unsigned __int8)size_seed )
      BYTE1(seed) = seed_rand[0];
    else
      BYTE1(seed) = seed_rand[i];
    LOBYTE(seed) = seed_rand[i - 1];
    // printf("%lx ",seed);
    srand(seed);
    v1 = 0;
    for ( j = 0; j <= 2559; ++j )
    {
      v1 += v6[i];
      if ( v1 > 2559 )
        v1 -= 2560;
      v5 = rand();
      array[v1] = v5;
      if ( v1 == 2558 )
        array[0] = HIBYTE(v5);
      else
        array[v1 + 1] = HIBYTE(v5);
    }
  }
}

void gen_key()
{
  int i; // [rsp+0h] [rbp-10h]
  int j; // [rsp+0h] [rbp-10h]
  int v3; // [rsp+4h] [rbp-Ch]
  _BYTE *v4; // [rsp+8h] [rbp-8h]

  v4 = key;
  v3 = 0;
  for ( i = 0; i <= 15; ++i )
    key[i] = 0;
  for ( j = 0; j <= 2559; ++j )
  {
    *v4++ ^= array[j];
    if ( ++v3 == 16 )
    {
      v3 = 0;
      v4 = key;
    }
  }
}
void encrypt(unsigned char *data, int size){
    for (int i = 0; i < 8; i++){
        unsigned int v6 = 8*(data[i]^key[i]);
        for (int j = 0; j < 8; j++){
            if (i!=j){
                data[j] ^= array[v6+j];
            }
        }
    }
    for (int i = 0; i < 8; i++){
        unsigned int v6 = 8*(data[i]^key[8+i]);
        for (int j = 0; j < 8; j++){
            if (i!=j){
                data[j] ^= array[v6+j];
            }
        }
    }
}
void decrypt(unsigned char *data, int size){
    for (int i = 7; i >= 0; i--){
        unsigned int v6 = 8*(data[i]^key[8+i]);
        for (int j = 7; j >= 0; j--){
            if (i!=j){
                data[j] ^= array[v6+j];
            }
        }
    }
    for (int i = 7; i >= 0; i--){
        unsigned int v6 = 8*(data[i]^key[i]);
        for (int j = 7; j >= 0; j--){
            if (i!=j){
                data[j] ^= array[v6+j];
            }
        }
    }
}
int main() {
    init();
    gen_key();
    unsigned char *cipher;
    FILE *f = fopen("flag.enc", "rb");
    if (!f) {
        perror("Error opening file");
        return -1;
    }

    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);

    cipher = malloc(fsize);
    if (!cipher) {
        perror("Memory allocation failed");
        fclose(f);
        return -1;
    }

    fread(cipher, 1, fsize, f);
    if (ferror(f)) {
        perror("Error reading file");
        free(cipher);
        fclose(f);
        return -1;
    }
    fclose(f);

    for (int i = 0; i < fsize; i += 8) {
        decrypt(cipher + i, 8);
    }
    int valid = 1;
    
    FILE *fw = fopen("./flag.png","wb");
    if (fw == NULL) {
        perror("Error opening file for writing");
        free(cipher);
        return -1;
    }
    fwrite(cipher, 1, fsize, fw);
    fclose(fw);
    free(cipher);
    return 0;
}
