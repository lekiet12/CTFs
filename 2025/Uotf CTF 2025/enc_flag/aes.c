/* Basic implementation of AES in C
 *
 * Warning: THIS CODE IS ONLY FOR LEARNING PURPOSES
 *          NOT RECOMMENDED TO USE IT IN ANY PRODUCTS
 */

#include <stdio.h>  // for printf
#include <stdlib.h> // for malloc, free

enum errorCode
{
    SUCCESS = 0,
    ERROR_AES_UNKNOWN_KEYSIZE,
    ERROR_MEMORY_ALLOCATION_FAILED,
};

// Implementation: S-Box

unsigned char sbox[256] = {
    // 0     1    2      3     4    5     6     7      8    9     A      B    C     D     E     F
    117, 147, 8, 226, 253, 254, 14, 191, 255, 23, 31, 89, 111, 175, 19, 160, 102, 173, 133, 47, 43, 104, 156, 59, 95, 177, 186, 20, 35, 159, 195, 204, 83, 75, 139, 215, 53, 84, 164, 40, 194, 30, 50, 51, 25, 150, 221, 122, 171, 222, 91, 11, 15, 68, 148, 236, 245, 4, 52, 158, 196, 197, 48, 179, 32, 109, 130, 123, 131, 161, 146, 67, 27, 124, 178, 180, 183, 55, 13, 38, 7, 71, 143, 172, 63, 193, 207, 60, 217, 18, 103, 105, 155, 37, 9, 116, 163, 176, 187, 66, 62, 79, 24, 208, 5, 125, 41, 45, 85, 127, 129, 113, 90, 10, 76, 3, 118, 39, 87, 28, 99, 107, 115, 26, 119, 135, 93, 151, 97, 17, 33, 153, 88, 157, 12, 162, 140, 56, 167, 108, 166, 192, 86, 199, 70, 81, 73, 182, 29, 200, 72, 201, 46, 61, 82, 128, 65, 80, 64, 112, 142, 100, 69, 134, 202, 22, 174, 181, 0, 126, 44, 184, 185, 189, 190, 138, 203, 209, 210, 211, 98, 110, 120, 121, 137, 132, 54, 213, 218, 206, 168, 219, 220, 58, 57, 223, 154, 224, 225, 227, 42, 229, 230, 114, 49, 231, 6, 92, 136, 106, 170, 233, 144, 235, 78, 238, 239, 205, 240, 36, 74, 2, 77, 234, 241, 243, 21, 169, 149, 244, 101, 198, 94, 165, 141, 216, 232, 237, 242, 16, 246, 214, 34, 212, 145, 247, 248, 249, 250, 1, 228, 96, 251, 188, 252, 152}; // F

unsigned char rsbox[256] =
    {168, 249, 221, 115, 57, 104, 206, 80, 2, 94, 113, 51, 134, 78, 6, 52, 239, 129, 89, 14, 27, 226, 165, 9, 102, 44, 123, 72, 119, 148, 41, 10, 64, 130, 242, 28, 219, 93, 79, 117, 39, 106, 200, 20, 170, 107, 152, 19, 62, 204, 42, 43, 58, 36, 186, 77, 137, 194, 193, 23, 87, 153, 100, 84, 158, 156, 99, 71, 53, 162, 144, 81, 150, 146, 220, 33, 114, 222, 214, 101, 157, 145, 154, 32, 37, 108, 142, 118, 132, 11, 112, 50, 207, 126, 232, 24, 251, 128, 180, 120, 161, 230, 16, 90, 21, 91, 209, 121, 139, 65, 181, 12, 159, 111, 203, 122, 95, 0, 116, 124, 182, 183, 47, 67, 73, 105, 169, 109, 155, 110, 66, 68, 185, 18, 163, 125, 208, 184, 175, 34, 136, 234, 160, 82, 212, 244, 70, 1, 54, 228, 45, 127, 255, 131, 196, 92, 22, 133, 59, 29, 15, 69, 135, 96, 38, 233, 140, 138, 190, 227, 210, 48, 83, 17, 166, 13, 97, 25, 74, 63, 75, 167, 147, 76, 171, 172, 26, 98, 253, 173, 174, 7, 141, 85, 40, 30, 60, 61, 231, 143, 149, 151, 164, 176, 31, 217, 189, 86, 103, 177, 178, 179, 243, 187, 241, 35, 235, 88, 188, 191, 192, 46, 49, 195, 197, 198, 3, 199, 250, 201, 202, 205, 236, 211, 223, 213, 55, 237, 215, 216, 218, 224, 238, 225, 229, 56, 240, 245, 246, 247, 248, 252, 254, 4, 5, 8};

unsigned char getSBoxValue(unsigned char num);
unsigned char getSBoxInvert(unsigned char num);

// Implementation: Rotate
void rotate(unsigned char *word);

// Implementation: Rcon
unsigned char Rcon[255] = {
    0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
    0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
    0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
    0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab,
    0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
    0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25,
    0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01,
    0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
    0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa,
    0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
    0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02,
    0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
    0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
    0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
    0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
    0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f,
    0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
    0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33,
    0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb};

unsigned char getRconValue(unsigned char num);

// Implementation: Key Schedule Core
void core(unsigned char *word, int iteration);

// Implementation: Key Expansion

enum keySize
{
    SIZE_16 = 16,
    SIZE_24 = 24,
    SIZE_32 = 32
};

void expandKey(unsigned char *expandedKey, unsigned char *key, enum keySize, size_t expandedKeySize);

// Implementation: AES Encryption

// Implementation: subBytes
void subBytes(unsigned char *state);
// Implementation: shiftRows
void shiftRows(unsigned char *state);
void shiftRow(unsigned char *state, unsigned char nbr);
// Implementation: addRoundKey
void addRoundKey(unsigned char *state, unsigned char *roundKey);
// Implementation: mixColumns
unsigned char galois_multiplication(unsigned char a, unsigned char b);
void mixColumns(unsigned char *state);
void mixColumn(unsigned char *column);
// Implementation: AES round
void aes_round(unsigned char *state, unsigned char *roundKey);
// Implementation: the main AES body
void createRoundKey(unsigned char *expandedKey, unsigned char *roundKey);
void aes_main(unsigned char *state, unsigned char *expandedKey, int nbrRounds);
// Implementation: AES encryption
char aes_encrypt(unsigned char *input, unsigned char *output, unsigned char *key, enum keySize size);
// AES Decryption
void invSubBytes(unsigned char *state);
void invShiftRows(unsigned char *state);
void invShiftRow(unsigned char *state, unsigned char nbr);
void invMixColumns(unsigned char *state);
void invMixColumn(unsigned char *column);
void aes_invRound(unsigned char *state, unsigned char *roundKey);
void aes_invMain(unsigned char *state, unsigned char *expandedKey, int nbrRounds);
char aes_decrypt(unsigned char *input, unsigned char *output, unsigned char *key, enum keySize size);

int main(int argc, char *argv[])
{
    // the expanded keySize
    int expandedKeySize = 176;

    // the expanded key
    unsigned char expandedKey[176];

    // the cipher key
    unsigned char key[16] = { 0x57, 0x2D, 0xAF, 0x32, 0x00, 0x00, 0x00, 0x00, 0x4A, 0x0A, 
  0x27, 0x7E, 0x00, 0x00, 0x00, 0x00};

    // the cipher key size
    enum keySize size = SIZE_16;

    // the plaintext
    unsigned char plaintext[16] = {49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 49, 50, 51, 52, 53, 54};

    // the ciphertext
    unsigned char ciphertext[32]={150, 20, 145, 213, 26, 179, 49, 243, 137, 165, 161, 85, 61, 116, 78, 201, 230, 5, 134, 127, 113, 63, 68, 16, 230, 80, 222, 26, 73, 32, 53, 170};

    // the decrypted text
    unsigned char decryptedtext[32];

    int i;

    // Test the Key Expansion
    expandKey(expandedKey, key, size, expandedKeySize);

    // // AES Encryption
    // aes_encrypt(plaintext, ciphertext, key, SIZE_16);


    // for (i = 0; i < 16; i++)
    // {
    //     printf("%2.2x%c", ciphertext[i], ((i + 1) % 16) ? ' ' : '\n');
    // }

    // // AES Decryption
    aes_decrypt(ciphertext, decryptedtext, key, SIZE_16);
// uoftctf{175_ju57_435_bu7_w0r53}

    aes_decrypt(ciphertext+16, decryptedtext+16, key, SIZE_16);
    for (i = 0; i < 32; i++)
    {
        printf("%c", decryptedtext[i]);
    }

    return 0;
}

unsigned char getSBoxValue(unsigned char num)
{
    return sbox[num];
}

unsigned char getSBoxInvert(unsigned char num)
{
    return rsbox[num];
}

/* Rijndael's key schedule rotate operation
 * rotate the word eight bits to the left
 *
 * rotate(1d2c3a4f) = 2c3a4f1d
 *
 * word is an char array of size 4 (32 bit)
 */
void rotate(unsigned char *word)
{
    unsigned char c;
    int i;

    c = word[0];
    for (i = 0; i < 3; i++)
        word[i] = word[i + 1];
    word[3] = c;
}

unsigned char getRconValue(unsigned char num)
{
    return Rcon[num];
}

void core(unsigned char *word, int iteration)
{
    int i;

    // rotate the 32-bit word 8 bits to the left
    rotate(word);

    // apply S-Box substitution on all 4 parts of the 32-bit word
    for (i = 0; i < 4; ++i)
    {
        word[i] = getSBoxValue(word[i]);
    }

    // XOR the output of the rcon operation with i to the first part (leftmost) only
    word[0] = word[0] ^ getRconValue(iteration);
}

/* Rijndael's key expansion
 * expands an 128,192,256 key into an 176,208,240 bytes key
 *
 * expandedKey is a pointer to an char array of large enough size
 * key is a pointer to a non-expanded key
 */

void expandKey(unsigned char *expandedKey,
               unsigned char *key,
               enum keySize size,
               size_t expandedKeySize)
{
    // current expanded keySize, in bytes
    int currentSize = 0;
    int rconIteration = 1;
    int i;
    unsigned char t[4] = {0}; // temporary 4-byte variable

    // set the 16,24,32 bytes of the expanded key to the input key
    for (i = 0; i < size; i++)
        expandedKey[i] = key[i];
    currentSize += size;

    while (currentSize < expandedKeySize)
    {
        // assign the previous 4 bytes to the temporary value t
        for (i = 0; i < 4; i++)
        {
            t[i] = expandedKey[(currentSize - 4) + i];
        }

        /* every 16,24,32 bytes we apply the core schedule to t
         * and increment rconIteration afterwards
         */
        if (currentSize % size == 0)
        {
            core(t, rconIteration++);
        }

        // For 256-bit keys, we add an extra sbox to the calculation
        if (size == SIZE_32 && ((currentSize % size) == 16))
        {
            for (i = 0; i < 4; i++)
                t[i] = getSBoxValue(t[i]);
        }

        /* We XOR t with the four-byte block 16,24,32 bytes before the new expanded key.
         * This becomes the next four bytes in the expanded key.
         */
        for (i = 0; i < 4; i++)
        {
            expandedKey[currentSize] = expandedKey[currentSize - size] ^ t[i];
            currentSize++;
        }
    }
}

void subBytes(unsigned char *state)
{
    int i;
    /* substitute all the values from the state with the value in the SBox
     * using the state value as index for the SBox
     */
    for (i = 0; i < 16; i++)
        state[i] = getSBoxValue(state[i]);
}

void shiftRows(unsigned char *state)
{
    int i;
    // iterate over the 4 rows and call shiftRow() with that row
    for (i = 0; i < 4; i++)
        shiftRow(state + i * 4, i);
}

void shiftRow(unsigned char *state, unsigned char nbr)
{
    int i, j;
    unsigned char tmp;
    // each iteration shifts the row to the left by 1
    for (i = 0; i < nbr; i++)
    {
        tmp = state[0];
        for (j = 0; j < 3; j++)
            state[j] = state[j + 1];
        state[3] = tmp;
    }
}

void addRoundKey(unsigned char *state, unsigned char *roundKey)
{
    int i;
    for (i = 0; i < 16; i++)
        state[i] = state[i] ^ roundKey[i];
}

unsigned char galois_multiplication(unsigned char a, unsigned char b)
{
    unsigned char p = 0;
    unsigned char counter;
    unsigned char hi_bit_set;
    for (counter = 0; counter < 8; counter++)
    {
        if ((b & 1) == 1)
            p ^= a;
        hi_bit_set = (a & 0x80);
        a <<= 1;
        if (hi_bit_set == 0x80)
            a ^= 0x1b;
        b >>= 1;
    }
    return p;
}

void mixColumns(unsigned char *state)
{
    int i, j;
    unsigned char column[4];

    // iterate over the 4 columns
    for (i = 0; i < 4; i++)
    {
        // construct one column by iterating over the 4 rows
        for (j = 0; j < 4; j++)
        {
            column[j] = state[(j * 4) + i];
        }

        // apply the mixColumn on one column
        mixColumn(column);

        // put the values back into the state
        for (j = 0; j < 4; j++)
        {
            state[(j * 4) + i] = column[j];
        }
    }
}

void mixColumn(unsigned char *column)
{
    unsigned char cpy[4];
    int i;
    for (i = 0; i < 4; i++)
    {
        cpy[i] = column[i];
    }
    column[0] = galois_multiplication(cpy[0], 2) ^
                galois_multiplication(cpy[3], 1) ^
                galois_multiplication(cpy[2], 1) ^
                galois_multiplication(cpy[1], 3);

    column[1] = galois_multiplication(cpy[1], 2) ^
                galois_multiplication(cpy[0], 1) ^
                galois_multiplication(cpy[3], 1) ^
                galois_multiplication(cpy[2], 3);

    column[2] = galois_multiplication(cpy[2], 2) ^
                galois_multiplication(cpy[1], 1) ^
                galois_multiplication(cpy[0], 1) ^
                galois_multiplication(cpy[3], 3);

    column[3] = galois_multiplication(cpy[3], 2) ^
                galois_multiplication(cpy[2], 1) ^
                galois_multiplication(cpy[1], 1) ^
                galois_multiplication(cpy[0], 3);
}

void aes_round(unsigned char *state, unsigned char *roundKey)
{
    subBytes(state);
    shiftRows(state);
    mixColumns(state);
    addRoundKey(state, roundKey);
}

void createRoundKey(unsigned char *expandedKey, unsigned char *roundKey)
{
    int i, j;
    // iterate over the columns
    for (i = 0; i < 4; i++)
    {
        // iterate over the rows
        for (j = 0; j < 4; j++)
            roundKey[(i + (j * 4))] = expandedKey[(i * 4) + j];
    }
}

void aes_main(unsigned char *state, unsigned char *expandedKey, int nbrRounds)
{
    int i = 0;

    unsigned char roundKey[16];

    createRoundKey(expandedKey, roundKey);
    addRoundKey(state, roundKey);

    for (i = 1; i < nbrRounds; i++)
    {
        createRoundKey(expandedKey + 16 * i, roundKey);
        aes_round(state, roundKey);
    }

    createRoundKey(expandedKey + 16 * nbrRounds, roundKey);
    subBytes(state);
    shiftRows(state);
    addRoundKey(state, roundKey);
}

char aes_encrypt(unsigned char *input,
                 unsigned char *output,
                 unsigned char *key,
                 enum keySize size)
{
    // the expanded keySize
    int expandedKeySize;

    // the number of rounds
    int nbrRounds;

    // the expanded key
    unsigned char *expandedKey;

    // the 128 bit block to encode
    unsigned char block[16];

    int i, j;

    // set the number of rounds
    switch (size)
    {
    case SIZE_16:
        nbrRounds = 10;
        break;
    case SIZE_24:
        nbrRounds = 12;
        break;
    case SIZE_32:
        nbrRounds = 14;
        break;
    default:
        return ERROR_AES_UNKNOWN_KEYSIZE;
        break;
    }

    expandedKeySize = (16 * (nbrRounds + 1));

    expandedKey = (unsigned char *)malloc(expandedKeySize * sizeof(unsigned char));

    if (expandedKey == NULL)
    {
        return ERROR_MEMORY_ALLOCATION_FAILED;
    }
    else
    {
        /* Set the block values, for the block:
         * a0,0 a0,1 a0,2 a0,3
         * a1,0 a1,1 a1,2 a1,3
         * a2,0 a2,1 a2,2 a2,3
         * a3,0 a3,1 a3,2 a3,3
         * the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3
         */

        // iterate over the columns
        for (i = 0; i < 4; i++)
        {
            // iterate over the rows
            for (j = 0; j < 4; j++)
                block[(i + (j * 4))] = input[(i * 4) + j];
        }

        // expand the key into an 176, 208, 240 bytes key
        expandKey(expandedKey, key, size, expandedKeySize);

        // encrypt the block using the expandedKey
        aes_main(block, expandedKey, nbrRounds);

        // unmap the block again into the output
        for (i = 0; i < 4; i++)
        {
            // iterate over the rows
            for (j = 0; j < 4; j++)
                output[(i * 4) + j] = block[(i + (j * 4))];
        }

        // de-allocate memory for expandedKey
        free(expandedKey);
        expandedKey = NULL;
    }

    return SUCCESS;
}

void invSubBytes(unsigned char *state)
{
    int i;
    /* substitute all the values from the state with the value in the SBox
     * using the state value as index for the SBox
     */
    for (i = 0; i < 16; i++)
        state[i] = getSBoxInvert(state[i]);
}

void invShiftRows(unsigned char *state)
{
    int i;
    // iterate over the 4 rows and call invShiftRow() with that row
    for (i = 0; i < 4; i++)
        invShiftRow(state + i * 4, i);
}

void invShiftRow(unsigned char *state, unsigned char nbr)
{
    int i, j;
    unsigned char tmp;
    // each iteration shifts the row to the right by 1
    for (i = 0; i < nbr; i++)
    {
        tmp = state[3];
        for (j = 3; j > 0; j--)
            state[j] = state[j - 1];
        state[0] = tmp;
    }
}

void invMixColumns(unsigned char *state)
{
    int i, j;
    unsigned char column[4];

    // iterate over the 4 columns
    for (i = 0; i < 4; i++)
    {
        // construct one column by iterating over the 4 rows
        for (j = 0; j < 4; j++)
        {
            column[j] = state[(j * 4) + i];
        }

        // apply the invMixColumn on one column
        invMixColumn(column);

        // put the values back into the state
        for (j = 0; j < 4; j++)
        {
            state[(j * 4) + i] = column[j];
        }
    }
}

void invMixColumn(unsigned char *column)
{
    unsigned char cpy[4];
    int i;
    for (i = 0; i < 4; i++)
    {
        cpy[i] = column[i];
    }
    column[0] = galois_multiplication(cpy[0], 14) ^
                galois_multiplication(cpy[3], 9) ^
                galois_multiplication(cpy[2], 13) ^
                galois_multiplication(cpy[1], 11);
    column[1] = galois_multiplication(cpy[1], 14) ^
                galois_multiplication(cpy[0], 9) ^
                galois_multiplication(cpy[3], 13) ^
                galois_multiplication(cpy[2], 11);
    column[2] = galois_multiplication(cpy[2], 14) ^
                galois_multiplication(cpy[1], 9) ^
                galois_multiplication(cpy[0], 13) ^
                galois_multiplication(cpy[3], 11);
    column[3] = galois_multiplication(cpy[3], 14) ^
                galois_multiplication(cpy[2], 9) ^
                galois_multiplication(cpy[1], 13) ^
                galois_multiplication(cpy[0], 11);
}

void aes_invRound(unsigned char *state, unsigned char *roundKey)
{

    invShiftRows(state);
    invSubBytes(state);
    addRoundKey(state, roundKey);
    invMixColumns(state);
}

void aes_invMain(unsigned char *state, unsigned char *expandedKey, int nbrRounds)
{
    int i = 0;

    unsigned char roundKey[16];

    createRoundKey(expandedKey + 16 * nbrRounds, roundKey);
    addRoundKey(state, roundKey);

    for (i = nbrRounds - 1; i > 0; i--)
    {
        createRoundKey(expandedKey + 16 * i, roundKey);
        aes_invRound(state, roundKey);
    }

    createRoundKey(expandedKey, roundKey);
    invShiftRows(state);
    invSubBytes(state);
    addRoundKey(state, roundKey);
}

char aes_decrypt(unsigned char *input,
                 unsigned char *output,
                 unsigned char *key,
                 enum keySize size)
{
    // the expanded keySize
    int expandedKeySize;

    // the number of rounds
    int nbrRounds;

    // the expanded key
    unsigned char *expandedKey;

    // the 128 bit block to decode
    unsigned char block[16];

    int i, j;

    // set the number of rounds
    switch (size)
    {
    case SIZE_16:
        nbrRounds = 10;
        break;
    case SIZE_24:
        nbrRounds = 12;
        break;
    case SIZE_32:
        nbrRounds = 14;
        break;
    default:
        return ERROR_AES_UNKNOWN_KEYSIZE;
        break;
    }

    expandedKeySize = (16 * (nbrRounds + 1));

    expandedKey = (unsigned char *)malloc(expandedKeySize * sizeof(unsigned char));

    if (expandedKey == NULL)
    {
        return ERROR_MEMORY_ALLOCATION_FAILED;
    }
    else
    {
        /* Set the block values, for the block:
         * a0,0 a0,1 a0,2 a0,3
         * a1,0 a1,1 a1,2 a1,3
         * a2,0 a2,1 a2,2 a2,3
         * a3,0 a3,1 a3,2 a3,3
         * the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3
         */

        // iterate over the columns
        for (i = 0; i < 4; i++)
        {
            // iterate over the rows
            for (j = 0; j < 4; j++)
                block[(i + (j * 4))] = input[(i * 4) + j];
        }

        // expand the key into an 176, 208, 240 bytes key
        expandKey(expandedKey, key, size, expandedKeySize);

        // decrypt the block using the expandedKey
        aes_invMain(block, expandedKey, nbrRounds);

        // unmap the block again into the output
        for (i = 0; i < 4; i++)
        {
            // iterate over the rows
            for (j = 0; j < 4; j++)
                output[(i * 4) + j] = block[(i + (j * 4))];
        }

        // de-allocate memory for expandedKey
        free(expandedKey);
        expandedKey = NULL;
    }

    return SUCCESS;
}