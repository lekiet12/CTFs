
cipher = [0]*12
cipher[0] = 0xBEB745E9
cipher[1] = 0x34EFB88C
cipher[2] = 0xA945C1EF
cipher[3] = 0x53B472FB
cipher[4] = 0x286EE702
cipher[5] = 0xA179B5E6
cipher[6] = 0x6CE124EB
cipher[7] = 0xDBA4B3F7
cipher[8] = 0x66BC5ABA
cipher[9] = 0x743F71EB
cipher[10] = 0xDA1F311A
cipher[11] = 0x7B957DD8
res=b''
for i in range(0,len(cipher),2):
    res+=((cipher[i+1]).to_bytes(4,'big'))+(cipher[i]).to_bytes(4,'big')
print(res.hex())
print(len(res))

# W1{dO_YoU_KnOw_wHaT_ThE_LoNgEsT_PaSsWoRd_iN_RoCkYoU_Is?}