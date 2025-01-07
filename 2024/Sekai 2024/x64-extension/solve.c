#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
void aes_x86_128_encrypt_block(unsigned char *plaintext, unsigned char *ciphertext, unsigned char *round_keys)
{
	
	asm("movdqu (%0), %%xmm15" :: "r"(plaintext));

	asm("movdqu (%0), %%xmm0" :: "r"(round_keys));
	asm("movdqu (%0), %%xmm1" :: "r"(round_keys + 16));
	asm("movdqu (%0), %%xmm2" :: "r"(round_keys + 32));
	asm("movdqu (%0), %%xmm3" :: "r"(round_keys + 48));
	asm("movdqu (%0), %%xmm4" :: "r"(round_keys + 64));
	asm("movdqu (%0), %%xmm5" :: "r"(round_keys + 80));
	asm("movdqu (%0), %%xmm6" :: "r"(round_keys + 96));
	asm("movdqu (%0), %%xmm7" :: "r"(round_keys + 112));
	asm("movdqu (%0), %%xmm8" :: "r"(round_keys + 128));
	asm("movdqu (%0), %%xmm9" :: "r"(round_keys + 144));
	asm("movdqu (%0), %%xmm10" :: "r"(round_keys + 160));
	asm("movdqu (%0), %%xmm11" :: "r"(round_keys + 160+16));
	asm("movdqu (%0), %%xmm12" :: "r"(round_keys + 160+16*2));
	asm("movdqu (%0), %%xmm13" :: "r"(round_keys + 160+16*3));
	asm("movdqu (%0), %%xmm14" :: "r"(round_keys + 160+16*4));
	
	asm("pxor %xmm0, %xmm15; \
	     aesenc %xmm1, %xmm15;\
	     aesenc %xmm2, %xmm15;\
	     aesenc %xmm3, %xmm15;\
	     aesenc %xmm4, %xmm15;\
	     aesenc %xmm5, %xmm15;\
	     aesenc %xmm6, %xmm15;\
	     aesenc %xmm7, %xmm15;\
	     aesenc %xmm8, %xmm15;\
	     aesenc %xmm9, %xmm15;\
		 aesenc %xmm10, %xmm15;\
		 aesenc %xmm11, %xmm15;\
		 aesenc %xmm12, %xmm15;\
		 aesenc %xmm13, %xmm15;\
	     aesenclast %xmm14, %xmm15;");
	
	asm("movdqu %%xmm15, (%0)" :: "r"(ciphertext));
}
void aes_x86_128_decrypt_block(unsigned char *ciphertext, unsigned char *plaintext, unsigned char *dec_round_keys)
{
	
	asm("movdqu (%0), %%xmm15" :: "r"(ciphertext));
	
	asm("movdqu (%0), %%xmm11" :: "r"(dec_round_keys + 160+16));
	asm("movdqu (%0), %%xmm12" :: "r"(dec_round_keys + 160+16*2));
	asm("movdqu (%0), %%xmm13" :: "r"(dec_round_keys + 160+16*3));
	asm("movdqu (%0), %%xmm14" :: "r"(dec_round_keys + 160+16*4));
	asm("movdqu (%0), %%xmm10" :: "r"(dec_round_keys + 160));
	asm("movdqu (%0), %%xmm9" :: "r"(dec_round_keys + 144));
	asm("movdqu (%0), %%xmm8" :: "r"(dec_round_keys + 128));
	asm("movdqu (%0), %%xmm7" :: "r"(dec_round_keys + 112));
	asm("movdqu (%0), %%xmm6" :: "r"(dec_round_keys + 96));
	asm("movdqu (%0), %%xmm5" :: "r"(dec_round_keys + 80));
	asm("movdqu (%0), %%xmm4" :: "r"(dec_round_keys + 64));
	asm("movdqu (%0), %%xmm3" :: "r"(dec_round_keys + 48));
	asm("movdqu (%0), %%xmm2" :: "r"(dec_round_keys + 32));
	asm("movdqu (%0), %%xmm1" :: "r"(dec_round_keys + 16));
	asm("movdqu (%0), %%xmm0" :: "r"(dec_round_keys));
	/* ...and do the rounds with them */
	asm("pxor %xmm14, %xmm15; \
		aesdec %xmm13, %xmm15;\
		aesdec %xmm12, %xmm15;\
		aesdec %xmm11, %xmm15;\
		aesdec %xmm10, %xmm15;\
	     aesdec %xmm9, %xmm15;\
	     aesdec %xmm8, %xmm15;\
	     aesdec %xmm7, %xmm15;\
	     aesdec %xmm6, %xmm15;\
	     aesdec %xmm5, %xmm15;\
	     aesdec %xmm4, %xmm15;\
	     aesdec %xmm3, %xmm15;\
	     aesdec %xmm2, %xmm15;\
	     aesdec %xmm1, %xmm15;\
	     aesdeclast %xmm0, %xmm15;");
	/* copy the data out of xmm15 */
	asm("movdqu %%xmm15, (%0)" :: "r"(plaintext));
}
void aes_x86_128_key_inv_transform(unsigned char *round_keys, unsigned char *dec_round_keys) {
  /* call the inversion instruction on most of the keys */
  asm(" \
    mov %0, %%rdx;                 \
    mov %1, %%rax;                 \
    movdqu (%%rdx), %%xmm1;        \
    movdqu %%xmm1, (%%rax);        \
    add $0x10, %%rdx;              \
    add $0x10, %%rax;              \
    \
    mov $13, %%ecx;                 \
    repeat:                        \
    movdqu (%%rdx), %%xmm1;    \
    aesimc %%xmm1, %%xmm1;     \
    movdqu %%xmm1, (%%rax);    \
    add $0x10, %%rdx;          \
    add $0x10, %%rax;          \
    loop repeat;                   \
    \
    movdqu (%%rdx), %%xmm1;        \
    movdqu %%xmm1, (%%rax);        \
    " :: "r"(round_keys), "r"(dec_round_keys) : "rdx", "rax");
}
int main() {
  unsigned char plaintext[] = "1111111111111111";
  assert(strlen(plaintext) == 16);
  unsigned char roundkeys[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 183, 115, 194, 159, 179, 118, 196, 152, 187, 127, 206, 147, 183, 114, 192, 156, 185, 81, 168, 205, 173, 68, 190, 218, 181, 93, 164, 193, 169, 64, 186, 222, 141, 135, 223, 76, 62, 241, 27, 212, 133, 142, 213, 71, 50, 252, 21, 219, 154, 225, 241, 116, 55, 165, 79, 174, 130, 248, 235, 111, 43, 184, 81, 177, 214, 86, 23, 189, 232, 167, 12, 105, 109, 41, 217, 46, 95, 213, 204, 245, 85, 226, 186, 146, 98, 71, 245, 60, 224, 191, 30, 83, 203, 7, 79, 226, 169, 210, 143, 162, 65, 117, 131, 203, 44, 92, 90, 229, 115, 137, 150, 16, 218, 69, 42, 88, 184, 2, 223, 100, 88, 189, 193, 55, 147, 186, 142, 213, 135, 203, 140, 126, 198, 190, 15, 181, 234, 226, 85, 80, 153, 107, 195, 64, 52, 58, 4, 81, 140, 56, 219, 53, 212, 133, 26, 2, 71, 63, 148, 215, 167, 233, 130, 222, 97, 87, 141, 107, 139, 181, 216, 59, 18, 222, 27, 123, 253, 39, 171, 112, 113, 31, 112, 69, 165, 154, 106, 71, 226, 165, 254, 144, 199, 82, 226, 70, 166, 5, 111, 45, 45, 176, 183, 22, 63, 110, 172, 109};
  unsigned char ciphertext[]= "aaaaaaaaaaaaaaaa";
  unsigned char dk[180]= {};
  aes_x86_128_encrypt_block(plaintext, ciphertext, roundkeys);
  memset(plaintext, 0, sizeof(plaintext));
  aes_x86_128_key_inv_transform(roundkeys, dk);
  unsigned char cipher[]={21, 42, 56, 130, 205, 138, 54, 51, 84, 77, 34, 102, 92, 229, 138, 234, 28, 178, 93, 178, 89, 100, 122, 126, 109, 112, 33, 42, 221, 36, 107, 142, 56, 17, 69, 163, 96, 61, 202, 143, 18, 182, 236, 156, 15, 96, 217, 38, 233, 44, 131, 159, 97, 112, 15, 220, 120, 146, 89, 57, 72, 193, 231, 194, 107, 92, 186, 28, 67, 194, 134, 128, 24, 98, 21, 210, 30, 11, 107, 158, 23, 44, 20, 199, 65, 16, 196, 53, 254, 120, 111, 180, 252, 221, 212, 170, 186, 221, 170, 21, 2, 183, 247, 119, 101, 67, 243, 120, 204, 238, 20, 202, 83, 66, 223, 58, 236, 237, 166, 49, 74, 129, 77, 255, 190, 78, 198, 239, 23, 104, 208, 157, 177, 115, 255, 78, 36, 191, 236, 187, 85, 245, 175, 125, 125, 107, 223, 159, 154, 59, 35, 152, 179, 164, 180, 28, 38, 95, 122, 13};
  unsigned char iv[]={0xFF, 0xFE, 0xFD, 0xFC, 0xFB, 0xFA, 0xF9, 0xF8, 0xF7, 0xF6, 
  0xF5, 0xF4, 0xF3, 0xF2, 0xF1, 0xF0,
  0x15, 0x2A, 0x38, 0x82, 0xCD, 0x8A, 0x36, 0x33, 0x54, 0x4D, 
  0x22, 0x66, 0x5C, 0xE5, 0x8A, 0xEA,
  0x1C, 0xB2, 0x5D, 0xB2, 0x59, 0x64, 0x7A, 0x7E, 0x6D, 0x70, 
  0x21, 0x2A, 0xDD, 0x24, 0x6B, 0x8E,
   0x38, 0x11, 0x45, 0xA3, 0x60, 0x3D, 0xCA, 0x8F, 0x12, 0xB6, 
  0xEC, 0x9C, 0x0F, 0x60, 0xD9, 0x26,
   0xE9, 0x2C, 0x83, 0x9F, 0x61, 0x70, 0x0F, 0xDC, 0x78, 0x92, 
  0x59, 0x39, 0x48, 0xC1, 0xE7, 0xC2,
   0x6B, 0x5C, 0xBA, 0x1C, 0x43, 0xC2, 0x86, 0x80, 0x18, 0x62, 
  0x15, 0xD2, 0x1E, 0x0B, 0x6B, 0x9E,
   0x17, 0x2C, 0x14, 0xC7, 0x41, 0x10, 0xC4, 0x35, 0xFE, 0x78, 
  0x6F, 0xB4, 0xFC, 0xDD, 0xD4, 0xAA,
    0xBA, 0xDD, 0xAA, 0x15, 0x02, 0xB7, 0xF7, 0x77, 0x65, 0x43, 
  0xF3, 0x78, 0xCC, 0xEE, 0x14, 0xCA,
   0x53, 0x42, 0xDF, 0x3A, 0xEC, 0xED, 0xA6, 0x31, 0x4A, 0x81, 
  0x4D, 0xFF, 0xBE, 0x4E, 0xC6, 0xEF,
     0x17, 0x68, 0xD0, 0x9D, 0xB1, 0x73, 0xFF, 0x4E, 0x24, 0xBF, 
  0xEC, 0xBB, 0x55, 0xF5, 0xAF, 0x7D
  };
  for (int i=0;i<sizeof(cipher);i+=16){
	unsigned char temp[16];
	for(int j=i;j<i+16;j++){
		temp[j-i]=cipher[j];
	}
	aes_x86_128_decrypt_block(temp, plaintext, dk);
	for (int j=i;j<i+16;j++){
		printf("%c",iv[j]^plaintext[j-i]);
	}
  }
  return 0;
}
