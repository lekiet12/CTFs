#include<iostream>
#include<Windows.h>
using namespace std;
int main(){
    LPVOID lpAddress;
    lpAddress = VirtualAlloc(NULL, 0x1000, MEM_COMMIT | MEM_RESERVE, PAGE_GUARD | PAGE_READONLY);
    if (lpAddress == NULL){
        cout << "VirtualAlloc failed" << endl;
        return 1;
    }
    else{
        cout << "VirtualAlloc success" << endl;
    }
    memset(lpAddress, 0, 0x1000);    
    return 0;
}