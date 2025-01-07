#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
void encrypt(unsigned char *v13,int v4){
    uint32_t v16 = 0, v17 = 0, v18 = 0, v19 = 0, v20 = 0, v21 = 0, v22 = 0, v23 = 0, v24 = 0, v25 = 0,
             v26 = 0, v27 = 0, v28 = 0, v29 = 0, v30 = 0, v31 = 0, v32 = 0, v33 = 0, v34 = 0, v35 = 0,
             v36 = 0, v37 = 0, v38 = 0, v39 = 0, v40 = 0, v41 = 0, v42 = 0, v43 = 0, v44 = 0, v45 = 0,
             v46 = 0, v47 = 0, v48 = 0, v49 = 0, v50 = 0, v51 = 0, v52 = 0, v53 = 0, v54 = 0, v55 = 0,
             v56 = 0, v57 = 0, v58 = 0, v59 = 0, v60 = 0, v61 = 0, v62 = 0, v63 = 0, v64 = 0, v65 = 0,
             v66 = 0;
    uint32_t v15, v14;
    v15 = 0;
    v16 = 0;
    do
    {
        v63 = *v13;
        v64 = 654321 * (unsigned char)v16;
        v17 = v13[1] | (*v13 << 7);
        v65 = v64 + 2 * ((v64 + 3 + (unsigned char)v16 * (123456 * (unsigned char)v16 + 1)) ^ (7041841 * (v64 + 3))) + 5570716;
        v66 = ((v64 + 3 + (unsigned char)v16 * (123456 * (unsigned char)v16 + 1)) ^ (unsigned int)(7041841 * (v64 + 3))) / 0x12;
        if ( (((unsigned char)v65 - (unsigned char)v66 - ((v65 - v66 != -1) - 1)) & 1) != 0 ){
            v17 ^= 0x55u;
            v18 = 6;
            v19 = 2;
        }
        else{
            v18 = 4;
            v19 = 0;
        }
        v20 = (unsigned char)(v15 + 1) ^ 0x31;
        v13[1] = -19 - (v17 ^ 1);
        v21 = v13[2] | ((unsigned char)(v63 >> 1) << 7);
        v22 = 654321 * v20;
        v23 = v22 + 2 * ((v22 + 3 + v20 * (123456 * v20 + 1)) ^ (7041841 * (v22 + 3))) + 5570716;
        v24 = ((v22 + 3 + v20 * (123456 * v20 + 1)) ^ (unsigned int)(7041841 * (v22 + 3))) / 0x12;
        if ( (((unsigned char)v23 - (unsigned char)v24 - ((v23 - v24 != -1) - 1)) & 1) != 0 ){
            v21 ^= 0x55u;
            v19 = v18;
        }
        v25 = (unsigned char)(v15 + 2) ^ 0x31;
        v13[2] = -19 - (v21 ^ 2);
        v26 = 654321 * v25;
        v27 = v13[3] | ((unsigned char)(v63 >> 2) << 7);
        v28 = v26 + 2 * ((v26 + 3 + v25 * (123456 * v25 + 1)) ^ (7041841 * (v26 + 3))) + 5570716;
        v29 = ((v26 + 3 + v25 * (123456 * v25 + 1)) ^ (unsigned int)(7041841 * (v26 + 3))) / 0x12;
        if ( (((unsigned char)v28 - (unsigned char)v29 - ((v28 - v29 != -1) - 1)) & 1) != 0 ){
            v19 |= 8u;
            v27 ^= 0x55u;
        }
        v30 = (unsigned char)(v15 + 3) ^ 0x31;
        v13[3] = -19 - (v27 ^ 3);
        v31 = 654321 * v30;
        v32 = v13[4] | ((unsigned char)(v63 >> 3) << 7);
        v33 = v31 + 2 * ((v31 + 3 + v30 * (123456 * v30 + 1)) ^ (7041841 * (v31 + 3))) + 5570716;
        v34 = ((v31 + 3 + v30 * (123456 * v30 + 1)) ^ (unsigned int)(7041841 * (v31 + 3))) / 0x12;
        if ( (((unsigned char)v33 - (unsigned char)v34 - ((v33 - v34 != -1) - 1)) & 1) != 0 ){
            v19 |= 0x10u;
            v32 ^= 0x55u;
        }
        v35 = (unsigned char)(v15 + 4) ^ 0x31;
        v13[4] = -19 - (v32 ^ 4);
        v36 = 654321 * v35;
        v37 = v13[5] | ((unsigned char)(v63 >> 4) << 7);
        v38 = v36 + 2 * ((v36 + 3 + v35 * (123456 * v35 + 1)) ^ (7041841 * (v36 + 3))) + 5570716;
        v39 = ((v36 + 3 + v35 * (123456 * v35 + 1)) ^ (unsigned int)(7041841 * (v36 + 3))) / 0x12;
        if ( (((unsigned char)v38 - (unsigned char)v39 - ((v38 - v39 != -1) - 1)) & 1) != 0 ){
            v19 |= 0x20u;
            v37 ^= 0x55u;
        }
        v40 = (unsigned char)(v15 + 5) ^ 0x31;
        v13[5] = -19 - (v37 ^ 5);
        v41 = 654321 * v40;
        v42 = v13[6] | ((unsigned char)(v63 >> 5) << 7);
        v43 = v41 + 2 * ((v41 + 3 + v40 * (123456 * v40 + 1)) ^ (7041841 * (v41 + 3))) + 5570716;
        v44 = ((v41 + 3 + v40 * (123456 * v40 + 1)) ^ (unsigned int)(7041841 * (v41 + 3))) / 0x12;
        if ( (((unsigned char)v43 - (unsigned char)v44 - ((v43 - v44 != -1) - 1)) & 1) != 0 ){
            v19 |= 0x40u;
            v42 ^= 0x55u;
        }
        v45 = (unsigned char)(v15 + 6) ^ 0x31;
        v13[6] = -19 - (v42 ^ 6);
        v46 = 654321 * v45;
        v47 = v13[7] | ((unsigned char)(v63 >> 6) << 7);
        v48 = v46 + 2 * ((v46 + 3 + v45 * (123456 * v45 + 1)) ^ (0x6B7331 * (v46 + 3))) + 0x55009C;
        v49 = ((v46 + 3 + v45 * (123456 * v45 + 1)) ^ (unsigned int)(0x6B7331 * (v46 + 3))) / 0x12;
        if ( (((unsigned char)v48 - (unsigned char)v49 - ((v48 - v49 != -1) - 1)) & 1) != 0 ){
            (v19) = v19 | 0x80;
            v47 ^= 0x55u;
        }
        v50 = (unsigned char)(v15 + 7) ^ 0x31;
        v13[7] = -19 - (v47 ^ 7);
        v51 = 654321 * v50;
        v52 = v13[8] | ((unsigned char)(v63 >> 7) << 7);
        v53 = v51 + 2 * ((v51 + 3 + v50 * (123456 * v50 + 1)) ^ (7041841 * (v51 + 3))) + 5570716;
        v54 = ((v51 + 3 + v50 * (123456 * v50 + 1)) ^ (unsigned int)(7041841 * (v51 + 3))) / 0x12;
        if ( (((unsigned char)v53 - (unsigned char)v54 - ((v53 - v54 != -1) - 1)) & 1) != 0 ){
            v19 |= 0x100u;
            v52 ^= 0x55u;
        }
        v55 = (unsigned char)(v15 + 8) ^ 0x31;
        v56 = v63 >> 8 << 7;
        (v56) = v13[9] | v56;
        v13[8] = -19 - (v52 ^ 8);
        v57 = v15 + 9;
        v58 = 654321 * v55;
        v59 = v58 + 2 * ((v58 + 3 + v55 * (123456 * v55 + 1)) ^ (7041841 * (v58 + 3))) + 5570716;
        v60 = ((v58 + 3 + v55 * (123456 * v55 + 1)) ^ (unsigned int)(7041841 * (v58 + 3))) / 0x12;
        if ( (((unsigned char)v59 - (unsigned char)v60 - ((v59 - v60 != -1) - 1)) & 1) != 0 )
            v61 = v56 ^ 0x5C;
        else
            v61 = v56 ^ 9;
        v62 = v19 ^ 0xFFFFFF99;
        v15 += 10LL;
        v16 = v57 ^ 0x31;
        *v13 = v62;
        v13 += 10;
        *(v13 - 1) = -19 - v61;
    }
    while ( v15 < v4 );
}

void decrypt(unsigned char *cipher, int size, uint32_t v15, uint32_t &v16){
    uint32_t v17 = 0, v18 = 0, v19 = 0, v20 = 0, v21 = 0, v22 = 0, v23 = 0, v24 = 0, v25 = 0,
             v26 = 0, v27 = 0, v28 = 0, v29 = 0, v30 = 0, v31 = 0, v32 = 0, v33 = 0, v34 = 0, v35 = 0,
             v36 = 0, v37 = 0, v38 = 0, v39 = 0, v40 = 0, v41 = 0, v42 = 0, v43 = 0, v44 = 0, v45 = 0,
             v46 = 0, v47 = 0, v48 = 0, v49 = 0, v50 = 0, v51 = 0, v52 = 0, v53 = 0, v54 = 0, v55 = 0,
             v56 = 0, v57 = 0, v58 = 0, v59 = 0, v60 = 0, v61 = 0, v62 = 0, v63 = 0, v64 = 0, v65 = 0,
             v66 = 0;
    uint32_t v14;
    uint8_t enc0,enc1,enc2,enc3,enc4,enc5,enc6,enc7,enc8,enc9;
    for (int ch0 = 0; ch0 < 127 ;ch0++){
        for (int ch1 = 0; ch1< 127 ;ch1++){
            v63 = ch0;
            v64 = 654321 * (unsigned char)v16;
            v17 = ch1 | (ch0 << 7);
            v65 = v64 + 2 * ((v64 + 3 + (unsigned char)v16 * (123456 * (unsigned char)v16 + 1)) ^ (7041841 * (v64 + 3))) + 5570716;
            v66 = ((v64 + 3 + (unsigned char)v16 * (123456 * (unsigned char)v16 + 1)) ^ (unsigned int)(7041841 * (v64 + 3))) / 0x12;
            if ( (((unsigned char)v65 - (unsigned char)v66 - ((v65 - v66 != -1) - 1)) & 1) != 0 ){
                v17 ^= 0x55u;
                v18 = 6;
                v19 = 2;
            }
            else{
                v18 = 4;
                v19 = 0;
            }
            v20 = (unsigned char)(v15 + 1) ^ 0x31;
            enc0 = -19 - (v17 ^ 1);
            enc0 &= 0xff;
            if (enc0 == cipher[1]){
                for (int ch2 = 0; ch2 < 127 ; ch2++){
                    v21 = ch2 | ((unsigned char)(v63 >> 1) << 7);
                    v22 = 654321 * v20;
                    v23 = v22 + 2 * ((v22 + 3 + v20 * (123456 * v20 + 1)) ^ (7041841 * (v22 + 3))) + 5570716;
                    v24 = ((v22 + 3 + v20 * (123456 * v20 + 1)) ^ (unsigned int)(7041841 * (v22 + 3))) / 0x12;
                    if ( (((unsigned char)v23 - (unsigned char)v24 - ((v23 - v24 != -1) - 1)) & 1) != 0 ){
                        v21 ^= 0x55u;
                        v19 = v18;
                    }
                    v25 = (unsigned char)(v15 + 2) ^ 0x31;
                    enc1 = -19 - (v21 ^ 2);
                    enc1 &= 0xff;
                    if (enc1 == cipher[2]){
                        for (int ch3 = 0; ch3 < 127 ;ch3++){
                            v26 = 654321 * v25;
                            v27 = ch3 | ((unsigned char)(v63 >> 2) << 7);
                            v28 = v26 + 2 * ((v26 + 3 + v25 * (123456 * v25 + 1)) ^ (7041841 * (v26 + 3))) + 5570716;
                            v29 = ((v26 + 3 + v25 * (123456 * v25 + 1)) ^ (unsigned int)(7041841 * (v26 + 3))) / 0x12;
                            if ( (((unsigned char)v28 - (unsigned char)v29 - ((v28 - v29 != -1) - 1)) & 1) != 0 ){
                                v19 |= 8u;
                                v27 ^= 0x55u;
                            }
                            v30 = (unsigned char)(v15 + 3) ^ 0x31;
                            enc2 = -19 - (v27 ^ 3);
                            enc2 &= 0xff;
                            if (enc2 == cipher[3]){
                                for (int ch4 = 0; ch4 < 127; ch4++){
                                    v31 = 654321 * v30;
                                    v32 = ch4 | ((unsigned char)(v63 >> 3) << 7);
                                    v33 = v31 + 2 * ((v31 + 3 + v30 * (123456 * v30 + 1)) ^ (7041841 * (v31 + 3))) + 5570716;
                                    v34 = ((v31 + 3 + v30 * (123456 * v30 + 1)) ^ (unsigned int)(7041841 * (v31 + 3))) / 0x12;
                                    if ( (((unsigned char)v33 - (unsigned char)v34 - ((v33 - v34 != -1) - 1)) & 1) != 0 ){
                                        v19 |= 0x10u;
                                        v32 ^= 0x55u;
                                    }
                                    v35 = (unsigned char)(v15 + 4) ^ 0x31;
                                    enc3 = -19 - (v32 ^ 4);
                                    enc3 &= 0xff;
                                    if (enc3 == cipher[4]){
                                        for(int ch5 = 0; ch5 < 127; ch5 ++){
                                            v36 = 654321 * v35;
                                            v37 = ch5 | ((unsigned char)(v63 >> 4) << 7);
                                            v38 = v36 + 2 * ((v36 + 3 + v35 * (123456 * v35 + 1)) ^ (7041841 * (v36 + 3))) + 5570716;
                                            v39 = ((v36 + 3 + v35 * (123456 * v35 + 1)) ^ (unsigned int)(7041841 * (v36 + 3))) / 0x12;
                                            if ( (((unsigned char)v38 - (unsigned char)v39 - ((v38 - v39 != -1) - 1)) & 1) != 0 ){
                                                v19 |= 0x20u;
                                                v37 ^= 0x55u;
                                            }
                                            v40 = (unsigned char)(v15 + 5) ^ 0x31;
                                            enc4 = -19 - (v37 ^ 5);
                                            enc4 &= 0xff;   
                                            if (enc4 == cipher[5]){
                                                for (int ch6 = 0; ch6 < 127 ; ch6 ++){
                                                    v41 = 654321 * v40;
                                                    v42 = ch6 | ((unsigned char)(v63 >> 5) << 7);
                                                    v43 = v41 + 2 * ((v41 + 3 + v40 * (123456 * v40 + 1)) ^ (7041841 * (v41 + 3))) + 5570716;
                                                    v44 = ((v41 + 3 + v40 * (123456 * v40 + 1)) ^ (unsigned int)(7041841 * (v41 + 3))) / 0x12;
                                                    if ( (((unsigned char)v43 - (unsigned char)v44 - ((v43 - v44 != -1) - 1)) & 1) != 0 ){
                                                        v19 |= 0x40u;
                                                        v42 ^= 0x55u;
                                                    }
                                                    v45 = (unsigned char)(v15 + 6) ^ 0x31;
                                                    enc5 = -19 - (v42 ^ 6);
                                                    enc5 &= 0xff;
                                                    if (enc5 == cipher[6]){
                                                        for(int ch7 = 0; ch7 < 127; ch7++){
                                                            v46 = 654321 * v45;
                                                            v47 = ch7 | ((unsigned char)(v63 >> 6) << 7);
                                                            v48 = v46 + 2 * ((v46 + 3 + v45 * (123456 * v45 + 1)) ^ (0x6B7331 * (v46 + 3))) + 0x55009C;
                                                            v49 = ((v46 + 3 + v45 * (123456 * v45 + 1)) ^ (unsigned int)(0x6B7331 * (v46 + 3))) / 0x12;
                                                            if ( (((unsigned char)v48 - (unsigned char)v49 - ((v48 - v49 != -1) - 1)) & 1) != 0 ){
                                                                (v19) = v19 | 0x80;
                                                                v47 ^= 0x55u;
                                                            }
                                                            v50 = (unsigned char)(v15 + 7) ^ 0x31;
                                                            enc6 = -19 - (v47 ^ 7);
                                                            enc6 &= 0xff;
                                                            if (enc6 == cipher[7]){
                                                                for(int ch8 = 0; ch8 < 127;ch8++){
                                                                    v51 = 654321 * v50;
                                                                    v52 = ch8 | ((unsigned char)(v63 >> 7) << 7);
                                                                    v53 = v51 + 2 * ((v51 + 3 + v50 * (123456 * v50 + 1)) ^ (7041841 * (v51 + 3))) + 5570716;
                                                                    v54 = ((v51 + 3 + v50 * (123456 * v50 + 1)) ^ (unsigned int)(7041841 * (v51 + 3))) / 0x12;
                                                                    if ( (((unsigned char)v53 - (unsigned char)v54 - ((v53 - v54 != -1) - 1)) & 1) != 0 ){
                                                                        v19 |= 0x100u;
                                                                        v52 ^= 0x55u;
                                                                    }
                                                                    v55 = (unsigned char)(v15 + 8) ^ 0x31;
                                                                    enc7 = -19 - (v52 ^ 8);
                                                                    enc7 &= 0xff;
                                                                    if (enc7 == cipher[8]){
                                                                        for (int ch9 = 0; ch9 < 127; ch9++){
                                                                            v56 = v63 >> 8 << 7;
                                                                            (v56) = ch9 | v56;
                                                                            v57 = v15 + 9;
                                                                            v58 = 654321 * v55;
                                                                            v59 = v58 + 2 * ((v58 + 3 + v55 * (123456 * v55 + 1)) ^ (7041841 * (v58 + 3))) + 5570716;
                                                                            v60 = ((v58 + 3 + v55 * (123456 * v55 + 1)) ^ (unsigned int)(7041841 * (v58 + 3))) / 0x12;
                                                                            if ( (((unsigned char)v59 - (unsigned char)v60 - ((v59 - v60 != -1) - 1)) & 1) != 0 )
                                                                                v61 = v56 ^ 0x5C;
                                                                            else
                                                                                v61 = v56 ^ 9;
                                                                            v62 = v19 ^ 0xFFFFFF99;
                                                                            enc9 = v62;
                                                                            enc8 = (-19 - v61)&0xff;
                                                                            enc9 &= 0xff;
                                                                            if (enc8 == cipher[9] && enc9 == cipher[0]){
                                                                                v16 = v57 ^ 0x31;
                                                                                v15 += 10LL;
                                                                                printf("%c%c%c%c%c%c%c%c%c%c",ch0,ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9);
                                                                                return;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                
            }
        }
    }
}
int main(){
    unsigned char *cipher;
    FILE *f = fopen("flag.txt.enc","rb");
    fseek(f,0,SEEK_END);
    int size = ftell(f);
    fseek(f,0,SEEK_SET);
    cipher = (unsigned char *)malloc(size); 
    fread(cipher,1,size,f);
    uint32_t v16 = 0;
    for (int i=0;i<size;i+=10){
        decrypt(cipher+i,10,i,v16);
    }
    printf("\n");
    return 0;
}

// 0xL4ugh{r1se_and_r1se_ag@1n_unt1l_l@mbs_b3c0me_l1ons_e099c665_0b}