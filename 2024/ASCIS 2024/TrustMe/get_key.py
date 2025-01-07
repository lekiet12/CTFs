def gen0(key):
    new_key = [0]*len(key)
    for i in range(len(key)-1,-1,-1):
        new_key[len(key)-1-i]=key[i]
    return new_key
def gen1(key):
    for i in range(len(key)):
        if key[i]>=ord('A') and key[i]<=ord('Z'):
            key[i]+=32
        else:
            key[i]-=32
    return key
def gen2(key):
    new_key = [0]*len(key)
    new_key[0]=key[len(key)-1]
    for i in range(1,len(key)):
        new_key[i]=key[i-1]
    return new_key
def gen3(key):
    v1 = len(key)
    result = [0] * v1
    for i in range(v1):
        v5 = key[i]
        if ord('A') <= v5 <= ord('Z'):
            v6 = (((v5) - 52) % 26 + 65)
        elif ord('a') <= v5 <= ord('z'):
            v6 = (((v5) - 84) % 26 + 97)
        else:
            v6 = v5
        result[i] = v6
    return result


key = b'WTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibnM'
key=[i for i in key]
print(bytearray(gen0(key)).decode())
key = b'WTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibnM'
key=[i for i in key]
print(bytearray(gen1(key)).decode())
key = b'WTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibnM'
key=[i for i in key]
print(bytearray(gen2(key)).decode())
key = b'WTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibnM'
key=[i for i in key]
print(bytearray(gen3(key)).decode())

# MnbivxwTqsaDwDmDPlufDqJXpDVbgekuzKrOddMKVymjiawsFZrqPNqfaJbWjPTW
# wtpJwBjAFQnpQRzfSWAIJMYvkmDDoRkZUKEGBvdPxjQdFULpdMdWdASQtWXVIBNm
# MWTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibn
# jgcWjOwNSDacDEmsFJNVWZLixzQQbExMHXRTOiqCkwDqSHYcqZqJqNFDgJKIVOAz



# MWTPjWbJafqNPqrZFswaijmyVKMddOrKzukegbVDpXJqDfulPDmDwDasqTwxvibn