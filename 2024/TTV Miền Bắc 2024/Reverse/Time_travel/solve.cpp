#include<stdio.h>
#include<iostream>

int main(){
    unsigned char enc[]={104, 104, 125, 198, 55, 142, 253, 235, 52, 254, 23, 254, 157, 40, 224, 4, 112, 133, 183, 68, 104, 55, 192, 251, 34, 201, 160, 73, 189, 42, 182, 207, 184, 69, 189, 68, 80, 135, 177, 72, 243, 201, 124, 35, 184, 249, 46, 131, 189, 238, 168, 217, 8, 239, 55, 152, 28, 118, 197, 19, 246, 240, 220, 14, 42, 81, 189, 212, 35, 100, 132, 83, 225, 75};
    for (unsigned int seed = 0; seed < INT64_MAX;seed++){
        unsigned char flag[74];
        srand(seed);
        for (int i=0;i<74;i++){
            flag[i]=enc[i]^(rand());
        }
        if (flag[0]=='K' && flag[1]=='C' && flag[2]=='S' && flag[3]=='C' && flag[4]=='{'){
            for (int i=0;i<74;i++){
                printf("%c",flag[i]);
            }
            printf("\nseed: %x",seed);
            exit(0);
        } 
    }
}
// KCSC{0xffffff_is_1970-07-14,I_created_this_challenge_at_"the_end"_of_time}