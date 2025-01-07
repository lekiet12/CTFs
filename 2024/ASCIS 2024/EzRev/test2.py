import subprocess
import sys
import string 
import os
def check_char_index(cipher,index,flag,filename):
    with open("flag.txt","w") as file:
        file.write(flag)
        file.close()

    server = subprocess.Popen(f"./{filename}",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
    client = subprocess.Popen("./client.exe",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
    stdout_client, stderr_client = client.communicate()
    stdout_server, stderr_server = server.communicate()
    array_client = list(bytes.fromhex(stdout_client))
    if cipher[index] == array_client[index]:
        return True 
    else:
        return False
    
def run_check(seed,filename):
    cipher =[0xbd,0xbb,0xfa,0x2e,0x1c,0x2d,0x53,0x91,0x2f,0x5b,0x33,0x92,0xba,0x1a,0x94,0x3f,0x06,0x89,0xa1,0x28,0x73,0xc2,0x08,0x39,0xba,0xc1,0x20,0xcd,0xdd,0xcf,0xb4,0xd4,0x70,0xcb,0x53,0x7a,0xda,0xcd,0x8e,0x1e,0x47,0xd8,0x7d,0x18,0xd4,0x2d,0x72,0x23,0xac,0x29,0x06,0x8d,0xe1,0x2c,0x47,0xca,0x6f,0x37,0x06,0xfb,0x25,0x9e,0xc8,0xe5]
    server = subprocess.Popen(f"./{filename}",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
    client = subprocess.Popen("./client.exe",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
    stdout_client, stderr_client = client.communicate()
    stdout_server, stderr_server = server.communicate()
    array_client = list(bytes.fromhex(stdout_client))
    if array_client[63] == 0xe5:
        print("seed: "+str(seed))
        flag = list('1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcde}')
        character = string.ascii_letters+string.digits+'_'+'{}'
        for i in range(len(flag)-2,-1,-1):
            check = False
            for char in character:
                flag[i]=char
                if check_char_index(cipher,i,"".join(flag),filename):
                    check=False
                    break
            if check == False:
                break
        print("".join(flag))
        if check == True:
            print(flag)
# bin_server = bytearray(open("server.exe",'rb').read())
# for seed in range(0xffffffff):
#     patch_bytes = seed.to_bytes(4,'little')
#     bin_server[0x770:0x770+4] = patch_bytes
#     filename = "server_patch_"+str(seed)+".exe"
#     with open(filename,'wb') as f:
#         f.write(bin_server)
#         f.close()
#     try:
#         run_check(seed,filename)
#     finally:
#         os.remove(filename)

    

server = subprocess.Popen("./server.exe",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
client = subprocess.Popen("./client.exe",stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=subprocess.PIPE)
stdout_client, stderr_client = client.communicate()
stdout_server, stderr_server = server.communicate()
print(stdout_client)
