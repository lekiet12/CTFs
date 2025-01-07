#include <stdio.h>
#include <xmmintrin.h>
#include <math.h>
#include <stdint.h>
__m128 function(int base, int a2) {
    int v2 = 0; // Đếm số vòng lặp
    __int128 v3 = 0; // Kết quả trả về
    double v4 = 0.0; // Tích lũy giá trị
    int v7 = base; // Giá trị cơ sở
    double v8; // Biến tạm
    double v9; // Biến tạm
    __int64 v10; // Biến tạm cho vòng lặp
    int v11; // Biến tạm
    __int128 v12; // Biến tạm
    int v13; // Biến tạm

    if (a2 >= 0) {
        do {
            v8 = 1.0;
            v9 = (double)v7;
            if (a2 - v2 > 0) {
                v10 = (unsigned int)(a2 - v2);
                do {
                    v8 = fmod(v8 * 16.0, v9);
                    --v10;
                } while (v10);
            }
            ++v2;
            v7 += 8;
            v4 = fmod(v8 / v9 + v4, 1.0);
        } while (v2 <= a2);
    }

    v11 = base + 8 * (a2 + 1);
    *((__int64 *)&v12 + 1) = 0LL;
    *(double *)&v12 = pow(16.0, -1.0) / (double)v11 + 0.0;
    if (*(double *)&v12 != 0.0) {
        v13 = -1;
        do {
            --v13;
            v3 = v12;
            v11 += 8;
            *(double *)&v12 = *(double *)&v12 + pow(16.0, (double)v13) / (double)v11;
        } while (*(double *)&v3 != *(double *)&v12);
    }
    *(double *)&v3 = *(double *)&v3 + v4;
    return (__m128)v3;
}

int main() {
    int a2 = 0x1bcc; // Giá trị a2
    __m128 result1 = function(4, a2);

    double* v8 = (double*)&result1; // Chuyển đổi kết quả sang double
    // printf("Result for base 4: %llx \n", *(unsigned long long*)&v8[0]); // In ra kết quả


    __m128 result2 = function(1, a2);
    double* v9 = (double*)&result2;
    // printf("Result for base 1: %llx \n", *(unsigned long long*)&v9[0]); // In ra kết quả


    __m128 result3 = function(5, a2);
    double* v10 = (double*)&result3;
    // printf("Result for base 5: %llx \n", *(unsigned long long*)&v10[0]);

    double computedValue = (v9[0]*4.0);
    computedValue -=(v8[0]+v8[0]);
    computedValue -= (v10[0]);
    __m128 result4 = function(6, a2);

    double* v11 = (double*)&result4;

    double v12 = fmod(computedValue - v11[0], 1.0);
    double v13 = pow(16.0, 14.0);
    double v14 = floor(v12 * v13);
    

    int64_t intValue = (int64_t)v14; 

    unsigned char key[8];
    for(int i=0;i<7;i++){
        key[i]=(intValue >> (8*i))&0xff;
    }
    printf("Value of v14 as int: %llx\n", intValue); 

    return 0;
}