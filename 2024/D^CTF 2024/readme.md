# D^CTF 2024
## RandomVM

![image](https://hackmd.io/_uploads/BkjAgG-GA.png)

* Kiểm tra file

![image](https://hackmd.io/_uploads/Hki2xfbGA.png)

* Sau nhiều lần chạy thử thì ta biết được input gồm 12 hoặc 11 kí tự
* Ta load vào IDA:

![image](https://hackmd.io/_uploads/Hkbd-G-fR.png)

* Ta có thể dễ dàng hiểu được là nó sẽ mã hóa đầu vào sau đó so sánh với mảng `unk_B010`
* Ta sử dụng strace
```c
execve("./RandomVM", ["./RandomVM"], 0x7ffe68291770 /* 30 vars */) = 0
brk(NULL)                               = 0x55c4202dd000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f3482549000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=50131, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 50131, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f348253c000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220x\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=1926256, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 1974096, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f348235a000
mmap(0x7f3482380000, 1396736, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x26000) = 0x7f3482380000
mmap(0x7f34824d5000, 344064, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17b000) = 0x7f34824d5000
mmap(0x7f3482529000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1cf000) = 0x7f3482529000
mmap(0x7f348252f000, 53072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f348252f000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f3482357000
arch_prctl(ARCH_SET_FS, 0x7f3482357740) = 0
set_tid_address(0x7f3482357a10)         = 34
set_robust_list(0x7f3482357a20, 24)     = 0
rseq(0x7f3482358060, 0x20, 0, 0x53053053) = 0
mprotect(0x7f3482529000, 16384, PROT_READ) = 0
mprotect(0x55c41e3f2000, 4096, PROT_READ) = 0
mprotect(0x7f348257b000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7f348253c000, 50131)           = 0
read(0, 123456789012
"1", 1)                         = 1
read(0, "2", 1)                         = 1
ptrace(PTRACE_TRACEME)                  = -1 EPERM (Operation not permitted)
read(12, 0x55c41e3f3086, 0)             = -1 EBADF (Bad file descriptor)
write(0, "\6\f\0\0\0\0\0\0\0\0\0\0", 12
                                       ) = 12
brk(NULL)                               = 0x55c4202dd000
creat(NULL, 030205)                     = -1 EFAULT (Bad address)
read(0, "3", 1)                         = 1
read(0, "4", 1)                         = 1
read(0, "5", 1)                         = 1
read(0, "6", 1)                         = 1
read(0, "7", 1)                         = 1
read(0, "8", 1)                         = 1
ptrace(PTRACE_TRACEME)                  = -1 EPERM (Operation not permitted)
read(0, "9", 1)                         = 1
read(0, "0", 1)                         = 1
read(0, "1", 1)                         = 1
newfstatat(1, "", {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}, AT_EMPTY_PATH) = 0
getrandom("\x3f\x65\x9c\x20\xcc\xaa\x61\xcf", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x55c4202dd000
brk(0x55c4202fe000)                     = 0x55c4202fe000
write(1, "No. Try again.\n", 15No. Try again.
)        = 15
exit_group(0)                           = ?
+++ exited with 0 +++
```
* Ta thấy là nó đọc lần lượt các kí tự và thực hiện mã hóa. Điều ta cần chú ý là lệnh gọi ptrace được sử dụng, đây là một anti-debug được sử dụng trong bài này.
* Ta đặt breakpoint tại các lệnh syscall và unk_B040 đề quan sát quá tình mã hóa của nó.
* Sau khi debug, ta biết được quá trình mã hóa của nó như sau:
```python
flag[0]=(x[0] >> 3 | x[0] << (8 - 3)) & 0xff
flag[0]^=3
flag[0]^=x[1]

flag[1]=(x[1] >> 5 | x[1] << (8 - 5)) & 0xff
flag[1]^=x[2]

flag[2]=(x[2] >> 6 | x[2] << (8 - 6)) & 0xff
flag[2]^=x[3]

flag[3]=(x[3] >> 7 | x[3] << (8 - 7)) & 0xff
flag[3]^=7
flag[3]^=x[4]

flag[4]=(x[4] >> 4 | x[4] << (8 - 4)) & 0xff
flag[4]^=4
flag[4]^=x[5]

flag[5]=(x[5] >> 4 | x[5] << (8 - 4)) & 0xff
flag[5]^=x[6]

flag[6]=(x[6] >> 7 | x[6] << (8 - 7)) & 0xff
flag[6]^=7
flag[6]^=x[7]

flag[7]=(x[7] >> 7 | x[7] << (8 - 7)) & 0xff
flag[7]^=x[8]

flag[8]=(x[8] >> 2 | x[8] << (8 - 2)) & 0xff
flag[8]^=x[9]

flag[9]=(x[9] >> 4 | x[9] << (8 - 4)) & 0xff
flag[9]^=x[10]

flag[10]=(x[10] >> 4 | x[10] << (8 - 4)) & 0xff
flag[10]^=x[11]

flag[11]=(x[11] >> 7 | x[11] << (8 - 7)) & 0xff
flag[11]^=7
temp=[0]*12
temp[0]=flag[0]

lst=[157, 107, 161, 2, 215, 237, 64, 246, 14, 174, 132, 25]

for i in range(1,12):
    temp[i]=temp[i-1]^flag[i]
```
* Từ đó ta sẽ tìm được input
* solve.py
```python
from z3 import*
s=Solver()
x=[BitVec(f"x{i}",8) for i in range(12)]
tmp=x[:]
flag=[0]*12
flag[0]=(x[0] >> 3 | x[0] << (8 - 3)) & 0xff
flag[0]^=3
flag[0]^=x[1]

flag[1]=(x[1] >> 5 | x[1] << (8 - 5)) & 0xff
flag[1]^=x[2]

flag[2]=(x[2] >> 6 | x[2] << (8 - 6)) & 0xff
flag[2]^=x[3]

flag[3]=(x[3] >> 7 | x[3] << (8 - 7)) & 0xff
flag[3]^=7
flag[3]^=x[4]

flag[4]=(x[4] >> 4 | x[4] << (8 - 4)) & 0xff
flag[4]^=4
flag[4]^=x[5]

flag[5]=(x[5] >> 4 | x[5] << (8 - 4)) & 0xff
flag[5]^=x[6]

flag[6]=(x[6] >> 7 | x[6] << (8 - 7)) & 0xff
flag[6]^=7
flag[6]^=x[7]

flag[7]=(x[7] >> 7 | x[7] << (8 - 7)) & 0xff
flag[7]^=x[8]

flag[8]=(x[8] >> 2 | x[8] << (8 - 2)) & 0xff
flag[8]^=x[9]

flag[9]=(x[9] >> 4 | x[9] << (8 - 4)) & 0xff
flag[9]^=x[10]

flag[10]=(x[10] >> 4 | x[10] << (8 - 4)) & 0xff
flag[10]^=x[11]

flag[11]=(x[11] >> 7 | x[11] << (8 - 7)) & 0xff
flag[11]^=7
temp=[0]*12
temp[0]=flag[0]

lst=[157, 107, 161, 2, 215, 237, 64, 246, 14, 174, 132, 25]

for i in range(1,12):
    temp[i]=temp[i-1]^flag[i]

for i in range(len(lst)):
    s.add(temp[i]==lst[i])
if s.check()==sat:
    m=s.model()
    print(m)
    for i in tmp:
        print(chr(m[i].as_long()),end="")

# [x11 = 77,
#  x9 = 109,
#  x4 = 74,
#  x5 = 117,
#  x6 = 109,
#  x8 = 86,
#  x2 = 111,
#  x1 = 51,
#  x10 = 118,
#  x0 = 109,
#  x3 = 119,
#  x7 = 112]
# m3owJumpVmvM
```
* Flag: `d3ctf{m3owJumpVmvM}`
## ezjunk
![image](https://hackmd.io/_uploads/SJUuV-XG0.png)

* Ta load file vào IDA:

![image](https://hackmd.io/_uploads/rygoVbXz0.png)

* Ta debug để tạo lại mã 
* Đây là hàm main sau khi debug

![image](https://hackmd.io/_uploads/SJlGSZQMC.png)

![image](https://hackmd.io/_uploads/rkjmrZXz0.png)

* Ta thấy có các byte rác nên không F5 được. Ta sẽ loại bỏ các byte rác dó. 
* Hàm main sau khi bỏ các byte rác: 

![image](https://hackmd.io/_uploads/H1FMP-QfA.png)

* Hàm sub_401917:

![image](https://hackmd.io/_uploads/r1GlYWXGA.png)

* Hàm sub_401663:

![image](https://hackmd.io/_uploads/BJwbYZmGR.png)

* Ta thấy các giá trị sau khi mã hóa sẽ được so sánh với mảng unk_404360. Nhưng sau khi so sánh thì nó lại đi tới hàm này:

![image](https://hackmd.io/_uploads/HyUL6WQGR.png)

* Như vậy ta biết hàm phía trước chỉ thực hiện mã hóa và hàm này mới thực hiện kiểm tra các giá trị.
* Cộng thêm việc sau khi kiểm tra thì ta phát hiện có một anti-debug được sử dụng để làm thay đổi các giá trị.

![image](https://hackmd.io/_uploads/ryLs6WXGR.png)

* Để giải mã được ta cần tìm các giá trị sau khi mã hóa:
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v2 = {-1226984535, 907422755, 411695807, 1826940731, 173734140, 570393621, 1149605207, 767698871};
    std::vector<int> dword_408040(8, 0);
    int i=0;
   
        for (int num = 0; num < 0xffffffff; ++num) {
            std::cout << "\r" << num;
            dword_408040[i] = num;

            for (int j = 0; j < 32; ++j) {
                if (dword_408040[i] < 0) {
                    dword_408040[i] *= 2;
                    int v0 = dword_408040[i] ^ 0x84A6972F;
                    dword_408040[i] = v0;
                }
                else {
                    int v0 = 2 * dword_408040[i];
                    dword_408040[i] = v0;
                }
            }

            for (int k = 0; k < v2.size(); ++k) {
                if (dword_408040[i] == v2[k]) {
                    std::cout << "\nNum: " << num <<" "<<k<< std::endl;
                    break;
                }
            }
        }
    return 0;
}
```
> lst=[3710139819,2307229656,3137309,197438626,1298702698,1634491689,1536236277,1282871516]

* solve.py
```python
lst=[3710139819,2307229656,3137309,197438626,1298702698,1634491689,1536236277,1282871516]
arr=[3892409088, 3903355263, 3914301438, 3925247613, 3936193788, 3947139963, 3958086138, 3969032313, 3979978488, 3990924663, 4001870838, 4012817013, 4023763188, 4034709363, 4045655538, 4056601713, 4067547888, 4078494063, 4089440238, 4100386413, 4111332588, 4122278763, 4133224938, 4144171113, 4155117288, 4166063463, 4177009638, 4187955813, 4198901988, 4209848163, 4220794338, 4231740513]
from Crypto.Util.number import *
flag=b""
for k in range(0,8,2):
    a4=[0x5454,0x4602,0x4477,0x5e5e]
    v7=lst[k]
    v6=lst[k+1]
    for i in range(32):
        a2=arr[32-1-i]
        v6 -= (v7 + ((((v7 & 0xfffffff)<<5)) ^ (v7 >> 6))) ^ ((a4[((a2 >> 11) & 3)] ) + a2) ^ 0x33
        v6&=0xffffffff
        v7 -= (v6 + (((v6 & 0xfffffff)*16) ^ (v6 >> 5))) ^ ((a4[(a2 & 3)]) + a2) ^ 0x44
        v7 &=0xffffffff 
    flag+=long_to_bytes(v7)[::-1]
    flag+=long_to_bytes(v6)[::-1]
print(flag)
# d3ctf{ea3yjunk_c0d3_4nd_ea5y_re}
```
* Flag: `d3ctf{ea3yjunk_c0d3_4nd_ea5y_re}`
