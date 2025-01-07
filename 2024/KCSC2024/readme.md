# KCSC 2024
### f@k3
* Ta chạy thử file:

![image](https://hackmd.io/_uploads/HyZn_OCz0.png)

* Ta thấy là dù nhập bất cứ gì đều hiện ra correct
* Ta load vào IDA:

![image](https://hackmd.io/_uploads/HJRttOAM0.png)

* Ta debug và thấy nó giải mã ra một chuỗi:`KCSC{Could_be_a_f*k*_flag!}`

![image](https://hackmd.io/_uploads/HJc-9uAGR.png)

* Nhưng khi submit lại sai. Nên ta tìm trong chương trình và thấy một hàm:
```c
__int64 __fastcall sub_7FF621F51230(__int64 a1, __int64 a2)
{
  int i; // [rsp+20h] [rbp-128h]
  char Str[128]; // [rsp+30h] [rbp-118h] BYREF
  char v5[128]; // [rsp+B0h] [rbp-98h] BYREF

  qmemcpy(Str, "fM", 2);
  Str[2] = 12;
  Str[3] = -95;
  Str[4] = 86;
  Str[5] = 63;
  Str[6] = 43;
  Str[7] = -67;
  Str[8] = 78;
  Str[9] = 97;
  Str[10] = 106;
  Str[11] = -114;
  Str[12] = 73;
  Str[13] = 81;
  Str[14] = 61;
  Str[15] = -121;
  Str[16] = 114;
  Str[17] = 124;
  Str[18] = 54;
  Str[19] = -123;
  Str[20] = 69;
  Str[21] = 122;
  Str[22] = 104;
  Str[23] = -67;
  Str[24] = 75;
  Str[25] = 98;
  Str[26] = 62;
  Str[27] = -37;
  Str[28] = 114;
  Str[29] = 102;
  Str[30] = 58;
  Str[31] = -112;
  Str[32] = 72;
  Str[33] = 81;
  Str[34] = 1;
  Str[35] = -52;
  Str[36] = 115;
  Str[37] = 78;
  Str[38] = 31;
  Str[39] = -97;
  memset(&Str[40], 0, 0x58ui64);
  memset(v5, 0, sizeof(v5));
  for ( i = 0; i < strlen(Str); ++i )
    v5[i] = *(_BYTE *)(a2 + i % 4) ^ Str[i];
  return 0i64;
}
```
* Ta thấy mảng `Str` sẽ xor với mảng `a2` mà a2 chỉ có 5 kí tự và ta biết 5 kí tự đầu tiên của flag luôn luôn là `KCSC{` nên ta có thể tìm được `a2` và tìm được v5
* solve.py 
```python
Str=[0]*40
Str[0]=ord('f')
Str[1]=ord('M')
Str[2] = 12
Str[3] = -95
Str[4] = 86
Str[5] = 63
Str[6] = 43
Str[7] = -67
Str[8] = 78
Str[9] = 97
Str[10] = 106
Str[11] = -114
Str[12] = 73
Str[13] = 81
Str[14] = 61
Str[15] = -121
Str[16] = 114
Str[17] = 124
Str[18] = 54
Str[19] = -123
Str[20] = 69
Str[21] = 122
Str[22] = 104
Str[23] = -67
Str[24] = 75
Str[25] = 98
Str[26] = 62
Str[27] = -37
Str[28] = 114
Str[29] = 102
Str[30] = 58
Str[31] = -112
Str[32] = 72
Str[33] = 81
Str[34] = 1
Str[35] = -52
Str[36] = 115
Str[37] = 78
Str[38] = 31
Str[39] = -97
flag="KCSC{"
key=""
for i in range(len(flag)):
    key+=chr(ord(flag[i])^(Str[i]&0xff))
for i in range(len(Str)):
    print(chr(ord(key[i%4])^(Str[i]&0xff)),end="")
# KCSC{1t_co5ld_be_right7_fla9_here_^.^@@}
```
* Flag: `KCSC{1t_co5ld_be_right7_fla9_here_^.^@@}`
### Re x Rust
* Trong hàm main ta cần chú ý đoạn này:

![image](https://hackmd.io/_uploads/H1qnhO0GC.png)

* Đây là đoạn sẽ mã hóa input của chúng ta.
* Khi debug ta có thể nhận thấy là hàm phase 1 sẽ đảo ngược chuỗi input của chúng ta. 
* Tiếp đến hàm phase 2 

![image](https://hackmd.io/_uploads/HyCLCOCGR.png)

* Mỗi lần lặp sẽ mã hóa hai kí tự.
* Hàm phase 3:

![image](https://hackmd.io/_uploads/rJD0ROAGC.png)

* Nhìn khá khó hiểu nên ta sẽ vừa debug vừa đọc code để kiểm tra xem các giá trị thay đổi như thế nào. Cuối cùng ta có thể viết lại hàm phase 3 như sau:

```python
for i in range(0,len(lst)-2):
    lst[i]=lst[i]-lst[i+2]
    lst[i]&=0xff
    lst[i+2]=lst[i+2]-lst[i]
    lst[i+2]&=0xff
```
* Hàm phase 4:

![image](https://hackmd.io/_uploads/Sk7MZtRfR.png)

* Ta thấy là nó sẽ xor với v2 mà khi debug thì ta nhận thấy mỗi lần debug thì v2 lại có một giá trị khác

![image](https://hackmd.io/_uploads/HJccWYRGC.png)

Có thể viết lại như sau:

* Phase 1: đảo ngược chuỗi input
* Phase 2:
```python
lst=[]
for i in range(0,len(data)-1,2):
    v1=((flag[i]) & 0xF | (flag[i + 1]) & 0xF0)
    v2=((flag[i+1]) & 0xF | (flag[i]) & 0xF0)
    lst.append(v2)
    lst.append(v1)
```
* Phase 3:
```python
for i in range(0,len(lst)-2):
    lst[i]=lst[i]-lst[i+2]
    lst[i]&=0xff
    lst[i+2]=lst[i+2]-lst[i]
    lst[i+2]&=0xff
```
* Phase 4:
```python
for i in range(len(data)):
    lst[i]=(lst[i]^((xor>>0)&0xff)^((xor>>0x8)&0xff)^((xor>>0x10)&0xff)^((xor>>0x18)&0xff))
```
* solve.py
```python
with open("flag.enc", "rb") as f:
    data=f.read()
data=[i for i in data]
print(data)
from z3 import*
flag=[BitVec(f"x{i}",32) for i in range(len(data))]
xor=BitVec('xor', 32)
temp=flag[:]
flag=flag[::-1]
lst=[]
s=Solver()
for i in range(len(data)):
    s.add(And(flag[i]<127,flag[i]>32))
for i in range(0,len(data)-1,2):
    v1=((flag[i]) & 0xF | (flag[i + 1]) & 0xF0)
    v2=((flag[i+1]) & 0xF | (flag[i]) & 0xF0)
    lst.append(v2)
    lst.append(v1)
for i in range(0,len(lst)-2):
    lst[i]=lst[i]-lst[i+2]
    lst[i]&=0xff
    lst[i+2]=lst[i+2]-lst[i]
    lst[i+2]&=0xff
for i in range(len(data)):
    lst[i]=(lst[i]^((xor>>0)&0xff)^((xor>>0x8)&0xff)^((xor>>0x10)&0xff)^((xor>>0x18)&0xff))
for i in range(len(data)):
    s.add(lst[i]==data[i])
if s.check()==sat:
    m=s.model()
    print(m)
    for i in temp:
        print(chr(m[i].as_long()),end="")
# KCSC{r3v3rs3_rust_1s_funny_4nd_34sy_227da29931351}
```
* Flag: `KCSC{r3v3rs3_rust_1s_funny_4nd_34sy_227da29931351}`
### p2p
* Bài này sử dụng kĩ thuật process hollowing. Ta có thể nhận thấy thông qua việc debug và xem chương trình gọi các api.
Tham khảo kĩ thuật: https://sec.vnpt.vn/2019/01/process-hollowing/

![image](https://hackmd.io/_uploads/Hyc8ZqZQR.png)

* Tại đây ta có thể thấy là chương trình đã tạo một vùng dữ liệu và đang so sánh với một process khác. Mà ở đây đó chính là cmd.exe
* Để chắc chắn hơn ta có thể kiểm tra các tiến trình nào đang chạy bằng `process hacker`

![image](https://hackmd.io/_uploads/r1wuGcbmR.png)

* Ta có thể thấy trong `mixture.exe` đang có `cmd.exe`.
* Bây giờ ta dump chương trình `cmd.exe` bằng `hollows_hunter` (hoặc có thể dump tay)
* Ta sẽ load chương trình đó vào IDA. Trong hàm main ta thấy có chức năng kiểm tra flag

![image](https://hackmd.io/_uploads/SkqsBqWmA.png)

* Ta sẽ debug chương trình đến hàm check flag
* Ta sẽ chú ý đến đoạn code này:

![image](https://hackmd.io/_uploads/B14jU9bmR.png)

* Ta thấy 
    * `(a1 + 80))(&v15, 0, 0, 24, -268435456)`là advapi32_CryptAcquireContextA
    * `(a1 + 84))(v15, &dword_CF5434, 44, 0, 0, &v16)` là advapi32_CryptImportKey và ta lấy được key: 
    > 8, 2, 0, 0, 16, 102, 0, 0, 32, 0, 0, 0, 49, 115, 116, 39, 116, 95, 55, 108, 64, 103, 95, 117, 95, 50, 104, 48, 117, 108, 100, 110, 39, 116, 95, 115, 53, 98, 109, 49, 116, 95, 49, 116
    * `(a1 + 88))(v16, 1, v20, 0)` là advapi32_CryptSetKeyParam với v20 = [0x05, 0x17, 0x2B, 0x0C, 0x22, 0x41, 0x0C, 0x2D, 0x0C, 0x22,0x20, 0x5E, 0x1C, 0x22, 0x2C, 0x4F]
    * `(a1 + 92))(v16,0,1,0,v17,&v11,1024)` là advapi32_CryptEncrypt
    * `(a1 + 52))(v18, v17)` là kernel32_lstrcmp và ta lấy được cipher = [153, 40, 103, 72, 176, 86, 195, 101, 161, 108, 17, 153, 254, 136, 90, 164, 112, 253, 94, 167, 150, 58, 31, 204, 178, 223, 203, 39, 139, 124, 195, 150, 168, 158, 88, 186, 158, 151, 101, 19, 5, 36, 72, 106, 188, 125, 25, 41]
* Ta sẽ decrypt nó:
```cpp
#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#include <string.h>

BYTE cipher[] = {153, 40, 103, 72, 176, 86, 195, 101, 161, 108, 17, 153, 254, 136, 90, 164, 112, 253, 94, 167, 150, 58, 31, 204, 178, 223, 203, 39, 139, 124, 195, 150, 168, 158, 88, 186, 158, 151, 101, 19, 5, 36, 72, 106, 188, 125, 25, 41};
int main() {
    HCRYPTPROV hProv;
    HCRYPTKEY hKey;
    BYTE keyString[] = {8, 2, 0, 0, 16, 102, 0, 0, 32, 0, 0, 0, 49, 115, 116, 39, 116, 95, 55, 108, 64, 103, 95, 117, 95, 50, 104, 48, 117, 108, 100, 110, 39, 116, 95, 115, 53, 98, 109, 49, 116, 95, 49, 116};
    if (CryptAcquireContextA(&hProv, 0, 0,24, -268435456)){
        printf("Success CryptAcquireContextA\n");
    }
    if (CryptImportKey(hProv,keyString,44,0,0,&hKey)){
        printf("Success CryptImportKey\n");
    }
    BYTE iv[]={0x05, 0x17, 0x2B, 0x0C, 0x22, 0x41, 0x0C, 0x2D, 0x0C, 0x22,0x20, 0x5E, 0x1C, 0x22, 0x2C, 0x4F};
    if (CryptSetKeyParam(hKey,1,iv,0)){
        printf("Success CryptSetKeyParam\n");
    }
    DWORD len=1024;
    CryptDecrypt(hKey,0,1,0,(BYTE*)cipher,&len);
    printf("flag : %s", cipher);
    return 0;
}
// Success CryptAcquireContextA
// Success CryptImportKey
// Success CryptSetKeyParam
// flag : KCSC{C0n9r@tulRQ10n2_0n_mak1ng_1t(^.^)}
```
* Nhưng flag: `KCSC{C0n9r@tulRQ10n2_0n_mak1ng_1t(^.^)}` sai
* Sau đó mình có hỏi anh Minh Hy và biết được hai số cuối của IV là lấy từ serial number volume của máy nên bây giờ cần phải biết số của author. Mà số mỗi máy lại khác nhau nên có lẽ hai số đó chỉ đoán thôi.
* Flag đúng: `KCSC{C0n9r@tul@t10n2_0n_mak1ng_1t(^.^)}`
### behind the scenes
* Hàm main:

![image](https://hackmd.io/_uploads/B1B135bQ0.png)

* Trước tiên ta debug để gen lại mã và patch một số byte để có thể F5 được loc_401FF0
* Hàm đó sau khi patch và F5
```c
int sub_BE1FF0()
{
  const char *v0; // eax
  int v1; // eax
  const char *v3; // eax
  char v4; // al
  char v5; // al
  int v6; // [esp+4h] [ebp-130h]
  int (__stdcall *v7)(char *, int); // [esp+1Ch] [ebp-118h]
  int i; // [esp+20h] [ebp-114h]
  int v9; // [esp+24h] [ebp-110h]
  char v10[4]; // [esp+28h] [ebp-10Ch] BYREF
  char v11[260]; // [esp+2Ch] [ebp-108h] BYREF

  (*(void (__thiscall **)(int, int, char *))(*(_DWORD *)dword_BE7794 + 32))(dword_BE7794, 260, v11);
  v0 = (const char *)sub_BE2FE0("Q2FjaGVkYXRhLmJpbg==", v10);
  sprintf_s(Buffer, 0x104u, "%s%s", v11, v0);
  for ( i = 0; i < 48; ++i )
    ;
  if ( (unsigned __int8)sub_BE2240(Buffer) )
  {
    v3 = (const char *)sub_BE2FE0("S0NTQy5kbGw=", v10);
    sprintf_s(byte_BE7550, 0x104u, "%s%s", v11, v3);
    sub_BE3860(Buffer, byte_BE7550);
    v9 = (**(int (__thiscall ***)(int, char *, int))dword_BE7794)(dword_BE7794, byte_BE7550, 12460239);
    if ( v9 )
    {
      v7 = (int (__stdcall *)(char *, int))(*(int (__thiscall **)(int, int, const char *))(*(_DWORD *)dword_BE7794 + 8))(
                                             dword_BE7794,
                                             v9,
                                             "HelloWorld");
      if ( v7 )
      {
        if ( v7(aAaaaaaaaaaa, v6) )
        {
          (*(void (__thiscall **)(int, int))(*(_DWORD *)dword_BE7794 + 4))(dword_BE7794, v9);
          v4 = sub_BE3340("Q29ycmVjdA==", v10);
          sub_BE1F20("%s", v4);
        }
        else
        {
          (*(void (__thiscall **)(int, int))(*(_DWORD *)dword_BE7794 + 4))(dword_BE7794, v9);
          v5 = sub_BE3340("V3Jvbmc=", v10);
          sub_BE1F20("%s", v5);
        }
        (*(void (__thiscall **)(int, int))(*(_DWORD *)dword_BE7794 + 4))(dword_BE7794, v9);
        return 0;
      }
      else
      {
        return 0;
      }
    }
    else
    {
      return 0;
    }
  }
  else
  {
    v1 = sub_BE2640(std::cerr, "Wrong");
    std::ostream::operator<<(v1, sub_BE2930);
    return 0;
  }
}
```
* Ta thấy `sub_BE2FE0` là hàm decode base64
* Ta thấy sau `sub_BE2240((int)Buffer)` là chương trình đã tải một `Cachedata.bin` và lưu ở C:\Users\LeKie\AppData\Local\Temp\KCSC.dllCachedata.bin
* Tiếp theo thì chương trình decrypt file `Cachadata.bin` thành file `KCSC.dll` 

![image](https://hackmd.io/_uploads/BJmObjbQA.png)

* Và ta sẽ lấy được `KCSC.dll` theo đường dẫn C:\Users\LeKie\AppData\Local\Temp\KCSC.dll
* Ta debug tiếp thì ta thấy nó gọi đến hàm `kcsc_HelloWorld` trong KCSC.dll để mã hóa input và kiểm tra các kí tự sau khi mã hóa.
* Ta load file KCSC.dll vào IDA, ta thấy sẽ kiểm tra input có bắt đầu bằng `de(RYpt3d_bu` không và input có độ dài là 44.

![image](https://hackmd.io/_uploads/SJC3fiZQ0.png)

![image](https://hackmd.io/_uploads/By4lXjbQC.png)

* Tiếp đến ta cần hiểu được input được mã hóa như thế nào. Và các kí tự sau khi mã hóa sẽ được so sánh với mảng
`v27[0] = xmmword_10003470;v27[1] = xmmword_100031E0;`
* Sau khi phân tích thì ta có thể giair mã như sau:
```python
cipher = [209, 70, 64, 145, 47, 100, 66, 214, 233, 45, 25, 40, 16, 200, 121, 136, 112, 50, 198, 71, 53, 141, 51, 231, 184, 112, 242, 135, 219, 219, 219, 253, 38, 91, 166, 181, 165, 223, 154, 91, 87, 183, 181, 125, 196, 173, 229, 196, 114, 86, 88, 17, 43, 171, 134, 90, 118, 138, 103, 62, 130, 140, 116, 145, 201, 102, 50, 29, 61, 211, 51, 128, 209, 16, 231, 199, 89, 78, 49, 101, 145, 237, 102, 24, 190, 155, 12, 38, 120, 117, 231, 158, 12, 232, 194, 230, 252, 60, 83, 140, 193, 11, 42, 18, 49, 170, 168, 50, 27, 104, 144, 104, 249, 188, 115, 183, 62, 228, 9, 174, 201, 233, 205, 172, 138, 196, 140, 79, 15, 104, 218, 168, 118, 42, 138, 109, 83, 127, 172, 213, 254, 60, 159, 92, 154, 21, 34, 22, 127, 28, 204, 146, 19, 81, 191, 207, 124, 149, 202, 255, 203, 89, 175, 233, 37, 15, 74, 166, 76, 30, 122, 212, 45, 88, 176, 176, 42, 214, 181, 140, 191, 21, 167, 179, 119, 235, 234, 3, 208, 74, 196, 101, 155, 212, 193, 232, 216, 182, 68, 225, 91, 30, 153, 28, 126, 223, 181, 98, 39, 178, 147, 94, 250, 57, 112, 191, 88, 79, 35, 175, 106, 167, 173, 72, 232, 20, 25, 118, 32, 29, 29, 99, 3, 66, 243, 29, 99, 3, 66, 243, 23, 175, 135, 188, 135, 38, 236, 132, 132, 172, 133, 77, 253, 247, 9, 31, 85, 134, 144, 33, 129, 200, 200, 218, 117, 77, 175, 21, 175, 78, 238, 153, 105, 57, 176, 122, 246, 251, 148, 22, 65, 72, 236, 56, 40, 205, 5, 28, 198, 73, 206, 24, 224, 26, 110, 102, 228, 164, 242, 150, 75, 236, 116, 36, 167, 239, 218, 100, 10, 138, 163, 41, 215, 216, 181, 10, 193, 66, 8, 220, 70, 43, 51, 34, 243, 201, 223, 34, 105, 205, 102, 207, 4, 42, 7, 1, 47, 5, 182, 7, 186, 248, 229, 126, 155, 82, 252, 145, 73, 134, 37, 163, 46, 100, 158, 241, 252, 15, 53, 33, 40, 109, 72, 99, 245, 17, 213, 200, 212, 193, 208, 5, 156, 92, 170, 73, 27, 239, 117, 189, 106, 144, 189, 19, 118, 110, 173, 255, 226, 251, 37, 57, 186, 21, 45, 195, 97, 117, 142, 215, 173, 212, 104, 228, 44, 124, 232, 209, 70, 116, 73, 95, 38, 1, 237, 132, 205, 113, 45, 39, 115, 233, 171, 135, 9, 20, 240, 81, 14, 204, 12, 206, 191, 187, 47, 134, 9, 137, 70, 218, 89, 60, 77, 196, 136, 25, 99, 249, 160, 118, 38, 69, 45, 164, 102, 118, 91, 113, 33, 19, 54, 193, 119, 236, 244, 243, 237, 17, 168, 240, 43, 75, 168, 162, 183, 50, 83, 88, 107, 209, 39, 235, 226, 5, 231, 31, 88, 104, 7, 60, 157, 30, 48, 34, 201, 165, 133, 65, 212, 222, 69, 40, 177, 38, 97, 22, 187, 88, 248, 178, 173, 244, 236, 155, 146, 19, 13, 100, 218, 143, 8, 212, 241, 204, 234, 51, 193, 27, 197, 109, 246, 171, 78, 31, 63, 103, 122, 240, 224, 239, 29, 165, 58, 24, 221, 59, 60, 101, 165, 7, 93, 137, 41, 172, 234, 139, 35, 43, 211, 88, 59, 188, 204, 105, 59, 32, 100, 228, 219, 205, 78, 97, 172, 23, 175, 152, 234, 234, 135, 223, 221, 54, 65, 243, 70, 13, 107, 201, 177, 113, 246, 14, 217, 12, 126, 161, 67, 205, 131, 4, 164, 106, 169, 96, 20, 77, 119, 136, 4, 191, 62, 81, 171, 190, 9, 44, 192, 230, 31, 229, 66, 255, 21, 50, 252, 74, 34, 148, 248, 102, 202, 141, 145, 175, 139, 97, 164, 56, 23, 30, 212, 111, 25, 80, 191, 104, 176, 18, 145, 42, 192, 131, 18, 189, 12, 105, 201, 149, 172, 110, 207, 206, 174, 180, 88, 111, 164, 38, 184, 156, 64, 84, 91, 177, 72, 128, 210, 98, 195, 189, 138, 250, 96, 16, 23, 178, 232, 53, 17, 100, 133, 112, 60, 154, 16, 42, 18, 217, 159, 190, 105, 53, 99, 94, 74, 47, 17, 80, 226, 52, 120, 14, 189, 133, 87, 21, 174, 124, 11, 133, 250, 21, 223, 249, 163, 126, 12, 21, 216, 130, 134, 221, 254, 81, 218, 169, 49, 34, 218, 219, 11, 255, 231, 51, 99, 163, 234, 226, 97, 53, 25, 98, 53, 135, 19, 222, 53, 133, 252, 24, 66, 188, 18, 14, 119, 97, 37, 108, 151, 26, 45, 114, 65, 27, 153, 73, 174, 126, 151, 102, 114, 88, 72, 249, 37, 97, 129, 56, 131, 106, 126, 113, 160, 2, 56, 80, 147, 109, 211, 89, 192, 227, 62, 215, 167, 196, 139, 90, 73, 12, 27, 11, 117, 215, 150, 151, 29, 50, 249, 17, 36, 176, 238, 76, 145, 157, 102, 81, 169, 60, 76, 65, 184, 229, 231, 154, 34, 212, 243, 29, 187, 58, 6, 136, 44, 7, 39, 133, 116, 12, 10, 179, 153, 5, 42, 96, 223, 2, 123, 96, 187, 229, 196, 183, 48, 87, 20, 129, 109, 229, 136, 209, 67, 19, 131, 50, 153, 191, 77, 86, 198, 161, 47, 102, 83, 135, 179, 147, 20, 163, 94, 94, 135, 134, 121, 51, 236, 241, 192, 100, 171, 242, 35, 77, 64, 220, 195, 196, 63, 58, 21, 40, 183, 134, 225, 215, 21, 218, 116, 193, 5, 68, 70, 5, 40, 7, 214, 190, 175, 92, 168, 59, 11, 20, 78, 20, 207, 183, 241, 171, 124, 245, 99, 240, 220, 194, 48, 219, 197, 47, 185, 197, 87, 42, 191, 80, 245, 57, 93, 90, 118, 99, 147, 123, 97, 29, 18, 231, 195, 11, 97, 169, 251, 38, 21, 98, 186, 50, 53, 78, 9, 194, 50, 49, 178, 149, 213, 142, 81, 162, 195, 52, 29, 184, 97, 141, 37, 181, 151, 29, 2, 250, 85, 249, 163, 177, 74, 186, 76, 190, 43, 65, 168, 113, 95, 27, 221, 44, 84, 118, 88, 193, 222, 110, 42, 124, 95, 147, 161, 4, 223, 69, 49, 224, 17, 50, 71, 155, 28, 13, 4, 146, 2, 68, 41, 178, 17, 50, 124, 214, 241, 46, 190, 179, 169, 4, 233, 250, 81, 15, 40, 69, 62, 131, 43, 111, 109, 250, 232, 133, 82, 15, 151, 147, 29, 163, 240, 171, 7, 63, 184, 58, 48, 248, 146, 45, 4, 152, 39, 6, 160, 194, 92, 29, 190, 8, 96, 30, 215, 63, 119, 2, 223, 119, 44, 163, 206, 100, 153, 81]
enc = [15, 33, 203, 71, 246, 176, 14, 160, 105, 81, 90, 8, 71, 126, 33, 213, 142, 49, 244, 214, 175, 208, 154, 64, 3, 43, 214, 76, 215, 88, 209, 71, 214, 169, 158, 41, 100, 115, 170, 72, 223, 70, 194, 186]
from z3 import *
flag=[BitVec(f"x{i}",8) for i in range(44)]
temp=flag[:]
v2=0
string = "de(RYpt3d_bu"
s=Solver()
for i in range(len(string)):
    s.add(flag[i]==ord(string[i]))
for i in range(len(flag)):
    s.add(flag[i] > 0x20)
    s.add(flag[i] < 0x7f)
for index in range(24):
    flag0=flag[0]
    if (index % 2):
        for i in range(44):
            if (v2%3==0):
                if (i!=43):
                    flag[i]^=((flag[i+1]-cipher[v2])&0xff)
                else:
                    flag[i]^=((flag0-cipher[v2])&0xff)
            if (v2%3==2):
                if (i==43):
                    flag[i]=(((flag0+cipher[v2])&0xff) -flag[i])&0xff
                else:
                    flag[i]=(((cipher[v2]+flag[i+1])&0xff)-flag[i])&0xff
            if (v2%3==1):
                if (i==43):
                    flag[i]=(flag[i]+(flag0^cipher[v2]))&0xff
                else:
                    flag[i]= (flag[i]+(cipher[v2]^flag[i+1]))&0xff
            v2+=1
    else:
        for i in range(44):
            if (v2%3==0):
                if (i==0):
                    tmp2=flag0^cipher[v2]
                else:
                    tmp1=flag[i]^((flag[i-1]-cipher[v2])&0xff)
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (v2%3==2):
                if (i==0):
                    tmp2=(flag0-cipher[v2])&0xff
                else:
                    tmp1=(((flag[i-1]+cipher[v2])&0xff) - flag[i]) & 0xff
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (v2%3==1):
                if (i==0):
                    tmp2=(flag0+cipher[v2])&0xff
                else:
                    tmp1=flag[i]+((flag[i-1]^cipher[v2])&0xff)
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (i==43):
                flag[i]=tmp2
            v2+=1

for i in range(44):
    s.add(flag[i]==enc[i])
if s.check()==sat:
    m=s.model()
    print(m)
    for i in temp:
        print(chr(m[i].as_long()),end="")
# de(RYpt3d_but_m@y_be_you_5th_this_i5nt_f|agg
```
* Nhưng đây lại là flag fake.
* Ta kiểm tra lại chương trình thì phát hiện có một anti-debug được sử dụng:

![image](https://hackmd.io/_uploads/rJ-4HFnm0.png)

* Nó kiểm tra chương trình có đang chạy với cmd.exe , explorer.exe và chall.exe hay không.
* Nếu có thì nó gọi đến hàm `sub_218D0();`
* Sau khi chạy xong thì ta thấy file KCSC.dll đã bị thay đổi
* 12 kí tự đầu so sánh với `KCSC{kcscctf` và enc = [65, 165, 195, 199, 154, 53, 126, 233, 32, 184, 76, 184, 70, 80, 41, 10, 172, 194, 25, 250, 171, 204, 228, 244, 146, 104, 254, 223, 214, 34, 170, 42, 61, 165, 58, 88, 40, 132, 53, 15, 230, 233, 49, 146]
* solve.py
```python
cipher = [209, 70, 64, 145, 47, 100, 66, 214, 233, 45, 25, 40, 16, 200, 121, 136, 112, 50, 198, 71, 53, 141, 51, 231, 184, 112, 242, 135, 219, 219, 219, 253, 38, 91, 166, 181, 165, 223, 154, 91, 87, 183, 181, 125, 196, 173, 229, 196, 114, 86, 88, 17, 43, 171, 134, 90, 118, 138, 103, 62, 130, 140, 116, 145, 201, 102, 50, 29, 61, 211, 51, 128, 209, 16, 231, 199, 89, 78, 49, 101, 145, 237, 102, 24, 190, 155, 12, 38, 120, 117, 231, 158, 12, 232, 194, 230, 252, 60, 83, 140, 193, 11, 42, 18, 49, 170, 168, 50, 27, 104, 144, 104, 249, 188, 115, 183, 62, 228, 9, 174, 201, 233, 205, 172, 138, 196, 140, 79, 15, 104, 218, 168, 118, 42, 138, 109, 83, 127, 172, 213, 254, 60, 159, 92, 154, 21, 34, 22, 127, 28, 204, 146, 19, 81, 191, 207, 124, 149, 202, 255, 203, 89, 175, 233, 37, 15, 74, 166, 76, 30, 122, 212, 45, 88, 176, 176, 42, 214, 181, 140, 191, 21, 167, 179, 119, 235, 234, 3, 208, 74, 196, 101, 155, 212, 193, 232, 216, 182, 68, 225, 91, 30, 153, 28, 126, 223, 181, 98, 39, 178, 147, 94, 250, 57, 112, 191, 88, 79, 35, 175, 106, 167, 173, 72, 232, 20, 25, 118, 32, 29, 29, 99, 3, 66, 243, 29, 99, 3, 66, 243, 23, 175, 135, 188, 135, 38, 236, 132, 132, 172, 133, 77, 253, 247, 9, 31, 85, 134, 144, 33, 129, 200, 200, 218, 117, 77, 175, 21, 175, 78, 238, 153, 105, 57, 176, 122, 246, 251, 148, 22, 65, 72, 236, 56, 40, 205, 5, 28, 198, 73, 206, 24, 224, 26, 110, 102, 228, 164, 242, 150, 75, 236, 116, 36, 167, 239, 218, 100, 10, 138, 163, 41, 215, 216, 181, 10, 193, 66, 8, 220, 70, 43, 51, 34, 243, 201, 223, 34, 105, 205, 102, 207, 4, 42, 7, 1, 47, 5, 182, 7, 186, 248, 229, 126, 155, 82, 252, 145, 73, 134, 37, 163, 46, 100, 158, 241, 252, 15, 53, 33, 40, 109, 72, 99, 245, 17, 213, 200, 212, 193, 208, 5, 156, 92, 170, 73, 27, 239, 117, 189, 106, 144, 189, 19, 118, 110, 173, 255, 226, 251, 37, 57, 186, 21, 45, 195, 97, 117, 142, 215, 173, 212, 104, 228, 44, 124, 232, 209, 70, 116, 73, 95, 38, 1, 237, 132, 205, 113, 45, 39, 115, 233, 171, 135, 9, 20, 240, 81, 14, 204, 12, 206, 191, 187, 47, 134, 9, 137, 70, 218, 89, 60, 77, 196, 136, 25, 99, 249, 160, 118, 38, 69, 45, 164, 102, 118, 91, 113, 33, 19, 54, 193, 119, 236, 244, 243, 237, 17, 168, 240, 43, 75, 168, 162, 183, 50, 83, 88, 107, 209, 39, 235, 226, 5, 231, 31, 88, 104, 7, 60, 157, 30, 48, 34, 201, 165, 133, 65, 212, 222, 69, 40, 177, 38, 97, 22, 187, 88, 248, 178, 173, 244, 236, 155, 146, 19, 13, 100, 218, 143, 8, 212, 241, 204, 234, 51, 193, 27, 197, 109, 246, 171, 78, 31, 63, 103, 122, 240, 224, 239, 29, 165, 58, 24, 221, 59, 60, 101, 165, 7, 93, 137, 41, 172, 234, 139, 35, 43, 211, 88, 59, 188, 204, 105, 59, 32, 100, 228, 219, 205, 78, 97, 172, 23, 175, 152, 234, 234, 135, 223, 221, 54, 65, 243, 70, 13, 107, 201, 177, 113, 246, 14, 217, 12, 126, 161, 67, 205, 131, 4, 164, 106, 169, 96, 20, 77, 119, 136, 4, 191, 62, 81, 171, 190, 9, 44, 192, 230, 31, 229, 66, 255, 21, 50, 252, 74, 34, 148, 248, 102, 202, 141, 145, 175, 139, 97, 164, 56, 23, 30, 212, 111, 25, 80, 191, 104, 176, 18, 145, 42, 192, 131, 18, 189, 12, 105, 201, 149, 172, 110, 207, 206, 174, 180, 88, 111, 164, 38, 184, 156, 64, 84, 91, 177, 72, 128, 210, 98, 195, 189, 138, 250, 96, 16, 23, 178, 232, 53, 17, 100, 133, 112, 60, 154, 16, 42, 18, 217, 159, 190, 105, 53, 99, 94, 74, 47, 17, 80, 226, 52, 120, 14, 189, 133, 87, 21, 174, 124, 11, 133, 250, 21, 223, 249, 163, 126, 12, 21, 216, 130, 134, 221, 254, 81, 218, 169, 49, 34, 218, 219, 11, 255, 231, 51, 99, 163, 234, 226, 97, 53, 25, 98, 53, 135, 19, 222, 53, 133, 252, 24, 66, 188, 18, 14, 119, 97, 37, 108, 151, 26, 45, 114, 65, 27, 153, 73, 174, 126, 151, 102, 114, 88, 72, 249, 37, 97, 129, 56, 131, 106, 126, 113, 160, 2, 56, 80, 147, 109, 211, 89, 192, 227, 62, 215, 167, 196, 139, 90, 73, 12, 27, 11, 117, 215, 150, 151, 29, 50, 249, 17, 36, 176, 238, 76, 145, 157, 102, 81, 169, 60, 76, 65, 184, 229, 231, 154, 34, 212, 243, 29, 187, 58, 6, 136, 44, 7, 39, 133, 116, 12, 10, 179, 153, 5, 42, 96, 223, 2, 123, 96, 187, 229, 196, 183, 48, 87, 20, 129, 109, 229, 136, 209, 67, 19, 131, 50, 153, 191, 77, 86, 198, 161, 47, 102, 83, 135, 179, 147, 20, 163, 94, 94, 135, 134, 121, 51, 236, 241, 192, 100, 171, 242, 35, 77, 64, 220, 195, 196, 63, 58, 21, 40, 183, 134, 225, 215, 21, 218, 116, 193, 5, 68, 70, 5, 40, 7, 214, 190, 175, 92, 168, 59, 11, 20, 78, 20, 207, 183, 241, 171, 124, 245, 99, 240, 220, 194, 48, 219, 197, 47, 185, 197, 87, 42, 191, 80, 245, 57, 93, 90, 118, 99, 147, 123, 97, 29, 18, 231, 195, 11, 97, 169, 251, 38, 21, 98, 186, 50, 53, 78, 9, 194, 50, 49, 178, 149, 213, 142, 81, 162, 195, 52, 29, 184, 97, 141, 37, 181, 151, 29, 2, 250, 85, 249, 163, 177, 74, 186, 76, 190, 43, 65, 168, 113, 95, 27, 221, 44, 84, 118, 88, 193, 222, 110, 42, 124, 95, 147, 161, 4, 223, 69, 49, 224, 17, 50, 71, 155, 28, 13, 4, 146, 2, 68, 41, 178, 17, 50, 124, 214, 241, 46, 190, 179, 169, 4, 233, 250, 81, 15, 40, 69, 62, 131, 43, 111, 109, 250, 232, 133, 82, 15, 151, 147, 29, 163, 240, 171, 7, 63, 184, 58, 48, 248, 146, 45, 4, 152, 39, 6, 160, 194, 92, 29, 190, 8, 96, 30, 215, 63, 119, 2, 223, 119, 44, 163, 206, 100, 153, 81]
enc = [65, 165, 195, 199, 154, 53, 126, 233, 32, 184, 76, 184, 70, 80, 41, 10, 172, 194, 25, 250, 171, 204, 228, 244, 146, 104, 254, 223, 214, 34, 170, 42, 61, 165, 58, 88, 40, 132, 53, 15, 230, 233, 49, 146]

from z3 import *
flag=[BitVec(f"x{i}",8) for i in range(44)]
temp=flag[:]
v2=0
string = "KCSC{kcscctf"
s=Solver()
for i in range(len(string)):
    s.add(flag[i]==ord(string[i]))
for i in range(len(flag)):
    s.add(flag[i] > 0x20)
    s.add(flag[i] < 0x7f)
for index in range(24):
    flag0=flag[0]
    if (index % 2):
        for i in range(44):
            if (v2%3==0):
                if (i!=43):
                    flag[i]^=((flag[i+1]-cipher[v2])&0xff)
                else:
                    flag[i]^=((flag0-cipher[v2])&0xff)
            if (v2%3==2):
                if (i==43):
                    flag[i]=(((flag0+cipher[v2])&0xff) -flag[i])&0xff
                else:
                    flag[i]=(((cipher[v2]+flag[i+1])&0xff)-flag[i])&0xff
            if (v2%3==1):
                if (i==43):
                    flag[i]=(flag[i]+(flag0^cipher[v2]))&0xff
                else:
                    flag[i]= (flag[i]+(cipher[v2]^flag[i+1]))&0xff
            v2+=1
    else:
        for i in range(44):
            if (v2%3==0):
                if (i==0):
                    tmp2=flag0^cipher[v2]
                else:
                    tmp1=flag[i]^((flag[i-1]-cipher[v2])&0xff)
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (v2%3==2):
                if (i==0):
                    tmp2=(flag0-cipher[v2])&0xff
                else:
                    tmp1=(((flag[i-1]+cipher[v2])&0xff) - flag[i]) & 0xff
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (v2%3==1):
                if (i==0):
                    tmp2=(flag0+cipher[v2])&0xff
                else:
                    tmp1=flag[i]+((flag[i-1]^cipher[v2])&0xff)
                    flag[i-1]=tmp2
                    tmp2=tmp1
            if (i==43):
                flag[i]=tmp2
            v2+=1

for i in range(44):
    s.add(flag[i]==enc[i])
if s.check()==sat:
    m=s.model()
    print(m)
    for i in temp:
        print(chr(m[i].as_long()),end="")
# KCSC{kcscctf_2024_1_l0v3_y0u_@RSeqTke3a5v3D}
```
* Flag: `KCSC{kcscctf_2024_1_l0v3_y0u_@RSeqTke3a5v3D}`
