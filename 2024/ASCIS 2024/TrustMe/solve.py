from scapy.all import *
from scapy.all import TCP
from Crypto.Cipher import ARC4

packets = rdpcap("record.pcapng")
array_data = []
for packet in packets:
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        if tcp_layer.haslayer(Raw) and tcp_layer.dport == 31337:
            raw_payload = tcp_layer[Raw].load
            array_data.append(raw_payload)
idx_key = []
array_data=array_data[3:]
lst = []
data = b''
for i in range(len(array_data)):
    if len(array_data[i])==4:
        if array_data[i]==b'9\xbe\x14\xbe':
            idx_key.append(0)
        elif array_data[i]==b'\x67\xfc\xa9\xdf':
            idx_key.append(1)
        elif array_data[i]==b'\x70\xd3\x03\x96':
            idx_key.append(2)
        elif array_data[i]==b'\xE0\xDC\xED\x60':
            idx_key.append(3)
        lst.append(data)
        data = b''
    else:
        data+=array_data[i]
lst=lst[1:]
image = b''
for i in range(len(lst)):
    if idx_key[i] == 0:
        key =b'MnbivxwTqsaDwDmDPlufDqJXpDVbgekuzKrOddMKVymjiawsFZrqPNqfaJbWjPTW'
        p = ARC4.new(key=key)
        image+=p.decrypt(lst[i])
    elif idx_key[i] == 1:
        key =b'wtpJwBjAFQnpQRzfSWAIJMYvkmDDoRkZUKEGBvdPxjQdFULpdMdWdASQtWXVIBNm'
        p = ARC4.new(key=key)
        image+=p.decrypt(lst[i])
    elif idx_key[i] == 2:
        key =b'MWTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibn'
        p = ARC4.new(key=key)
        image+=p.decrypt(lst[i])
    elif idx_key[i] == 3:
        key =b'JGCwJoWnsdACdeMSfjnvwzlIXZqqBeXmhxrtoIQcKWdQshyCQzQjQnfdGjkivoaZ'
        p = ARC4.new(key=key)
        image+=p.decrypt(lst[i])
with open("flag.bmp",'wb') as f:
    f.write(image)


# MnbivxwTqsaDwDmDPlufDqJXpDVbgekuzKrOddMKVymjiawsFZrqPNqfaJbWjPTW
# wtpJwBjAFQnpQRzfSWAIJMYvkmDDoRkZUKEGBvdPxjQdFULpdMdWdASQtWXVIBNm
# MWTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibn
# JGCwJoWnsdACdeMSfjnvwzlIXZqqBeXmhxrtoIQcKWdQshyCQzQjQnfdGjkivoaZ


# WTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibnM