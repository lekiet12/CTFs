## Pico CTF 2024
### Packer
* Ta kiểm tra file bằng `detect it easy` thì biết đó là file elf đã bị packed.

![image](https://hackmd.io/_uploads/SJwff6vRp.png)

* Ta unpacked:`upx -d out`
* Ta load vào IDA

![image](https://hackmd.io/_uploads/SJAUNxsRa.png)

* Ta chuyển chuỗi hex sang string
* Flag: `picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_6ff964ef}`
### FactCheck
* Ta kiểm tra file

![image](https://hackmd.io/_uploads/SJpi0AqRp.png)

* Ta load vào IDA

![image](https://hackmd.io/_uploads/rk76C0cAT.png)

![image](https://hackmd.io/_uploads/H1NRCA5AT.png)

* Ta thấy chuỗi `picoCTF{wELF_d0N3_mate_` được gán vào v22 và được nối thêm các kí tự. Vậy ta chỉ cần nối các kí tự đó vào được.
* Flag: `picoCTF{wELF_d0N3_mate_fd65ee4e}`
### WinAntiDbg0x100
* Ta load vào IDA 

![image](https://hackmd.io/_uploads/rkP-e1jR6.png)

* Bài này ta chỉ cần bypass các anti-debug thì sẽ in ra được các flag
* Tại điểm rẽ hướng có các anti-debug của chương trình chỉ cần thay đổi cho nó đi theo hướng ngược lại là được

![image](https://hackmd.io/_uploads/H1VBZyjRT.png)

![image](https://hackmd.io/_uploads/HyFOM1j0a.png)

* Flag : `picoCTF{d3bug_f0r_th3_Win_0x100_cc0ff664}`
### Classic Crackme 0x100
* Kiểm tra file:

![image](https://hackmd.io/_uploads/SkrAGys0T.png)

* Ta load vào IDA:

![image](https://hackmd.io/_uploads/rkVhsksAp.png)

* Chương trình yêu cầu ta nhập input sau đó mã hóa input và so sánh với chuỗi output
* Ta thấy các giá trị để input thay đổi thì chỉ có random2 bị thay đổi nên ta cần tìm các giá trị cảu random2
```python
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
j=0
lst=[]
while ( j <= 2 ):
    for i_0 in range(50):
        random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
        random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
        lst.append(random2)
    j+=1
print(lst)
```
* Sau khi đã có các giá trị đó thì ta sẽ giải mã tìm ra các input.
```python
output="qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze"
lst=[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 32, 33, 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 32, 33, 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 16, 17, 17, 18, 17, 18, 18, 19, 17, 18, 18, 19, 18, 19, 19, 20, 32, 33]
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
for i_0 in range(50):
    for i in range(97,128):
        char=i
        j=0
        while ( j <= 2 ):
            random2=lst[i_0+j*50]
            char = ((random2 & secret3) + char - fix + (secret3 & (random2 >> 4))) % 26 + fix
            j+=1
        if chr(char)==output[i_0]:
            print(chr(i),end="")
            break
# qezjdvjltvuxavgiibmkrsncqrntxfykgmntwsepmyvyguzwtv
# picoCTF{s0lv3_angry_symb0ls_4699696e}
```
* Sau đó nc lên server và có được flag:`picoCTF{s0lv3_angry_symb0ls_4699696e}`
### 
* Đề bài cho ta một file chứa python bytecode 
* Ta cần chuyển nó sang mã python (có thể dùng chatgpt)
```python
input_list = [
    4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 
    70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 104, 44, 91, 7, 18, 106, 
    124, 89, 78
]

key_str = "J_o3t"
key_list = [ord(char) for char in key_str]

while len(key_list) < len(input_list):
    key_list.extend(key_list)

result = ''.join(chr(a ^ b) for a, b in zip(input_list, key_list))
result_text = ''.join(map(chr, result))

print(result_text)
```
* Ta thấy `input_list` sẽ được xor với `key` 
* Sau khi chạy thử thì cho kết quả không đúng nên có thể key bị sai mà ta biết định dạng của flag là`picoCTF{}` 
* Nên có thể tìm ra key của nó bằng cách xor `picoC` với 5 số đầu tiên của `input_list`
* Solve.py
```python
input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 104, 44, 91, 7, 18, 106, 124, 89, 78]

key=[116,95,74,111,51]
for i in range(len(input_list)):
    print(chr(input_list[i]^key[i%len(key)]),end="")
# picoCTF{N0t_sO_coNfus1ng_sn@ke_7f44f566}
```
* Flag: `picoCTF{N0t_sO_coNfus1ng_sn@ke_7f44f566}`
### WinAntiDbg0x200
* Ta tiếp tục bypass tương tự như bài `WinAntiDbg0x100` 
* Flag: `picoCTF{0x200_debug_f0r_Win_3fa9b221}`
### WinAntiDbg0x300
* Ta kiểm tra file:

![image](https://hackmd.io/_uploads/rk-lggsRa.png)

* Ta thấy file đã bị pack nên ta sẽ unpack nó `upx -d WinAntiDbg0x300.exe`
* Ta load vào IDA 
* Ta tiếp tục bypass tương tự như hai bài trên và ta cần chú ý hàm `StartAddress_0`

![image](https://hackmd.io/_uploads/r1ogmls0p.png)

* Nó có một luồng không hiện khi ta `f5` nên ta sẽ thay đổi luồng chương trình để nó đi vào nơi ta muốn và ta sẽ có được flag.

![Screenshot 2024-03-22 185808](https://hackmd.io/_uploads/HJUKmgj06.png)

* Flag: `picoCTF{Wind0ws_antid3bg_0x300_86fcf897}`