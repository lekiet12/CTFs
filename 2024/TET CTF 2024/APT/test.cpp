#include <windows.h>
#include <wincrypt.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    HCRYPTPROV hProv;         
    HCRYPTKEY hKey;    
    BYTE *pbData;    
    const char *pbKey = "encrypted_by_pepega_DESKTOP-O6RCQQC_johndoe\x00"; 
    FILE *file;
    fopen_s(&file, "important_note.txt", "rb");
    if (file == NULL) {
        printf("File not found\n");
        return 1;
    }

    fseek(file, 0, SEEK_END); 
    DWORD dwFileSize = ftell(file); 
    fseek(file, 0, SEEK_SET);
    
    pbData = (BYTE*)malloc(dwFileSize);
    if (pbData == NULL) {
        printf("Memory allocation failed\n");
        fclose(file);
        return 1;
    }

    fread(pbData, 1, dwFileSize, file);
    fclose(file);
    DWORD dwDataLen = dwFileSize;

    if (!CryptAcquireContextA(&hProv, NULL, NULL, 24, 0xF0000000)) {
        printf("CryptAcquireContext failed, Error: %lu\n", GetLastError());
        return 1;
    }

    HCRYPTHASH hHash;
    if (!CryptCreateHash(hProv, CALG_SHA_256, 0, 0, &hHash)) {
        printf("CryptCreateHash failed, Error: %lu\n", GetLastError());
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    if (!CryptHashData(hHash, (BYTE*)pbKey, 44, 0)) {
        printf("CryptHashData failed, Error: %lu\n", GetLastError());
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    if (!CryptDeriveKey(hProv, CALG_RC4, hHash, 0x580011, &hKey)) {
        printf("CryptDeriveKey failed, Error: %lu\n", GetLastError());
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }
    if (!CryptDecrypt(hKey, 0, TRUE, 0, pbData, &dwDataLen)) {
        printf("CryptEncrypt failed, Error: %lu\n", GetLastError());
        CryptDestroyKey(hKey);
        CryptReleaseContext(hProv, 0);
        return 1;
    }
    for (DWORD i = 0; i < dwDataLen; i++) {
        printf("%c", pbData[i]);
    }
    printf("\n");
    CryptDestroyHash(hHash);  
    CryptDestroyKey(hKey);
    CryptReleaseContext(hProv, 0);
    free(pbData);

    return 0;
}
