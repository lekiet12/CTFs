#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

char nlf(int d)
{
    return (979137582 >> d) & 0x1;
}

void keeloq_encrypt(uint64_t *key, uint32_t *plaintext, uint32_t *ciphertext, int nrounds)
{    
    *ciphertext = *plaintext;
    unsigned char out, xor, nlf_input;
    for (int i = 0; i < nrounds; i++)
    {
        nlf_input = (((*ciphertext >> 31) & 0x1) << 4) | (((*ciphertext >> 26) & 0x1) << 3) |
                    (((*ciphertext >> 20) & 0x1) << 2) | (((*ciphertext >> 9) & 0x1) << 1) | ((*ciphertext >> 1) & 0x1);
        out = nlf(nlf_input);
        xor = ((*key >> (i % 64)) & 0x1) ^ ((*ciphertext >> 16) & 0x1) ^ (*ciphertext & 0x1) ^ out;
        *ciphertext = (*ciphertext >> 1) | (xor << 31);
    }    
}

void keeloq_decrypt(uint64_t *key, uint32_t *plaintext, uint32_t *ciphertext, int nrounds)
{
    *plaintext = *ciphertext;    
    char out, xor, nlf_input;
    for (int i = 0; i < nrounds; i++)
    {
        nlf_input = (((*plaintext >> 30) & 0x1) << 4) | (((*plaintext >> 25) & 0x1) << 3) |
                    (((*plaintext >> 19) & 0x1) << 2) | (((*plaintext >> 8) & 0x1) << 1) | (*plaintext & 0x1);
        out = nlf(nlf_input);
        xor = ((*key >> ((15 - i) % 64)) & 0x1) ^ ((*plaintext >> 31) & 0x1) ^ ((*plaintext >> 15) & 0x1) ^ out;
        *plaintext = (*plaintext << 1) | xor;
    }    
}
int main() {
    uint32_t cipher[9] = {0x16E7ECB2, 0xFAB8DCCE, 0x14D27DC1, 0x1D1DE649, 0xE6D8DD1, 
                          0x559D48D5, 0x65E7D793, 0xC36732FA, 0xE9797025};
    uint64_t key = 0x345EE31337F47CBA;
    int rounds = 528; 
    uint32_t plaintext, result;

    for (int i = 0; i < 9; i++) {
        keeloq_decrypt(&key, &plaintext, &cipher[i], rounds);
        for (int j=0;j<4;j++){
          printf("%c",(plaintext >> (8*(3-j))));
        }
    }
    return 0;
}

// ASIS{o0Oo0O0O00o0OO000_iT_Is_KeeLoq}