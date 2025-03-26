#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

struct mt {
    uint64_t rows;    
    uint64_t cols;    
    uint64_t *data;  
};

int convert(mt *a1, uint64_t row, uint64_t col, uint64_t value) {
    if (row >= a1->rows)
        return 0;
    if (col >= a1->cols)
        return 0;
    a1->data[row * a1->cols + col] = value;
    return 1;
}

int get_num(mt *a1, uint64_t row, uint64_t col, uint64_t *value) {
    if (row >= a1->rows)
        return 0;
    if (col >= a1->cols)
        return 0;
    *value = a1->data[row * a1->cols + col];
    return 1;
}

int MulMatrix(mt *a1, mt *a2, mt *a3) {
    uint64_t sum;           
    uint64_t val1, val2;    
    mt *v6 = a2;            

    if (a1->cols != a2->rows)
        return 0;
    if (a3->rows != a1->rows || a3->cols != a2->cols)
        return 0;

    for (int i = 0; i < a1->rows; ++i) {
        for (int j = 0; j < v6->cols; ++j) {
            sum = 0;
            for (int k = 0; k < v6->rows; ++k) {
                val1 = 0;
                val2 = 0;
                if (!get_num(a1, i, k, &val1))
                    return 0;
                if (!get_num(v6, k, j, &val2))
                    return 0;
                sum += val1 * val2;
            }
            if (!convert(a3, i, j, sum))
                return 0;
        }
    }
    return 1;
}

mt* create(mt *a1, uint64_t rows, uint64_t cols) {
    a1->rows = rows;
    a1->cols = cols;
    a1->data = (uint64_t *)calloc(rows * cols, sizeof(uint64_t));
    return a1;
}

int main() {
    int j, k, m, n;
    mt v15, v16, v17;           
    uint64_t v14;               
    int v6;                     
    int v3;                     
    uint8_t v19[16] = {1, 5, 2, 5, 4, 8, 7, 8, 2, 8, 6, 5, 1, 8, 3, 7}; 
    create(&v15, 4, 4);
    create(&v16, 4, 4);
    create(&v17, 4, 4);

    convert(&v15, 0, 0, 0x58ULL);
    convert(&v15, 0, 1, 0xFFFFFFFFFFFFFFEFULL);
    convert(&v15, 0, 2, 0x13ULL);
    convert(&v15, 0, 3, 0xFFFFFFFFFFFFFFC7ULL);
    convert(&v15, 1, 0, 0x2DULL);
    convert(&v15, 1, 1, 0xFFFFFFFFFFFFFFF7ULL);
    convert(&v15, 1, 2, 0xAULL);
    convert(&v15, 1, 3, 0xFFFFFFFFFFFFFFE3ULL);
    convert(&v15, 2, 0, 0xFFFFFFFFFFFFFFC8ULL);
    convert(&v15, 2, 1, 0xBULL);
    convert(&v15, 2, 2, 0xFFFFFFFFFFFFFFF4ULL);
    convert(&v15, 2, 3, 0x24ULL);
    convert(&v15, 3, 0, 0xFFFFFFFFFFFFFFD8ULL);
    convert(&v15, 3, 1, 8ULL);
    convert(&v15, 3, 2, 0xFFFFFFFFFFFFFFF7ULL);
    convert(&v15, 3, 3, 0x1AULL);

    for (j = 0; j <= 3; ++j) {
        for (k = 0; k <= 3; ++k) {
            convert(&v16, j, k, v19[4 * j + k]);
        }
    }

    v6 = 1;
    MulMatrix(&v15, &v16, &v17);

    for (m = 0; m <= 3; ++m) {
        for (n = 0; n <= 3; ++n) {
            get_num(&v17, m, n, &v14);
            if (m == n)
                v3 = v6 && v14 == 1;
            else
                v3 = v6 && v14 == 0;
            v6 = v3 != 0;
        }
    }

    if (v6)
        puts("Correct");
    else
        puts("Incorrect");

    free(v15.data);
    free(v16.data);
    free(v17.data);

    return 0;
}