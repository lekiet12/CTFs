#include<iostream>
unsigned char s_box[256]={0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 
  0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 
  0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 
  0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 
  0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7, 
  0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 
  0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 
  0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 
  0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 
  0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA, 0xFB, 
  0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 
  0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 
  0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 
  0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 
  0x64, 0x5D, 0x19, 0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 
  0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB, 
  0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 
  0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D, 
  0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 
  0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 
  0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 
  0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 
  0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 
  0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF, 
  0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 
  0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16};
__int64 __fastcall func(unsigned __int8 a1)
{
  unsigned __int64 v1; // rdx
  unsigned __int64 v2; // rcx
  unsigned __int64 v3; // rcx
  unsigned __int64 v4; // rcx
  unsigned __int64 v5; // rcx
  unsigned __int64 v6; // rcx
  unsigned __int64 v7; // rcx
  unsigned __int64 v8; // rcx
  unsigned __int64 v9; // rcx
  unsigned __int64 v10; // rcx
  unsigned __int64 v11; // rcx
  unsigned __int64 v12; // rcx
  unsigned __int64 v13; // rcx
  unsigned __int64 v14; // rcx
  unsigned __int64 v15; // rcx
  unsigned __int64 v16; // rcx
  unsigned __int64 v17; // rcx
  unsigned __int64 v18; // rcx
  unsigned __int64 v19; // rcx
  unsigned __int64 v20; // rcx
  unsigned __int64 v21; // rcx

  v1 = ((unsigned __int8)(4 * a1) | ((unsigned __int64)a1 >> 6)) ^ 0x2B;
  v2 = s_box[((unsigned __int8)(4 * s_box[v1]) | ((unsigned __int64)s_box[v1] >> 6)) ^ 0x2B];
  v3 = s_box[((unsigned __int8)(4 * v2) | (v2 >> 6)) ^ 0x2B];
  v4 = s_box[((unsigned __int8)(4 * v3) | (v3 >> 6)) ^ 0x2B];
  v5 = s_box[((unsigned __int8)(4 * v4) | (v4 >> 6)) ^ 0x2B];
  v6 = s_box[((unsigned __int8)(4 * v5) | (v5 >> 6)) ^ 0x2B];
  v7 = s_box[((unsigned __int8)(4 * v6) | (v6 >> 6)) ^ 0x2B];
  v8 = s_box[((unsigned __int8)(4 * v7) | (v7 >> 6)) ^ 0x2B];
  v9 = s_box[((unsigned __int8)(4 * v8) | (v8 >> 6)) ^ 0x2B];
  v10 = s_box[((unsigned __int8)(4 * v9) | (v9 >> 6)) ^ 0x2B];
  v11 = s_box[((unsigned __int8)(4 * s_box[((unsigned __int8)(4 * v10) | (v10 >> 6)) ^ 0x2B]) | ((unsigned __int64)s_box[((unsigned __int8)(4 * v10) | (v10 >> 6)) ^ 0x2B] >> 6)) ^ 0x2B];
  v12 = s_box[((unsigned __int8)(4 * v11) | (v11 >> 6)) ^ 0x2B];
  v13 = s_box[((unsigned __int8)(4 * v12) | (v12 >> 6)) ^ 0x2B];
  v14 = s_box[((unsigned __int8)(4 * v13) | (v13 >> 6)) ^ 0x2B];
  v15 = s_box[((unsigned __int8)(4 * v14) | (v14 >> 6)) ^ 0x2B];
  v16 = s_box[((unsigned __int8)(4 * v15) | (v15 >> 6)) ^ 0x2B];
  v17 = s_box[((unsigned __int8)(4 * v16) | (v16 >> 6)) ^ 0x2B];
  v18 = s_box[((unsigned __int8)(4 * v17) | (v17 >> 6)) ^ 0x2B];
  v19 = s_box[((unsigned __int8)(4 * v18) | (v18 >> 6)) ^ 0x2B];
  v20 = s_box[((unsigned __int8)(4 * v19) | (v19 >> 6)) ^ 0x2B];
  v21 = s_box[((unsigned __int8)(4 * v20) | (v20 >> 6)) ^ 0x2B];
  return s_box[((unsigned __int8)(4 * v21) | (v21 >> 6)) ^ 0x2B];
}
int main(){
    for(int i=0;i<=0xff;i++){
        unsigned int x = func(i);
        printf("0x%x,",x&0xff);
    }
    return 0;
}