import hashlib
import string
import itertools
char = string.ascii_letters+string.digits+'_'
res=['']*5
for flag in itertools.product(char,repeat=4):
    flag="".join(flag)
    hashcode = hashlib.md5(flag.encode()).hexdigest()
    if "09d15b9f2464cf02284a7e1abdb1fd17" == hashcode:
        print(flag)
        res[0]=flag
    elif "e7c50ea784c33f4c9af6c10884f432b1" == hashcode:
        print(flag)
        res[1]=flag 
    elif "1b8910d2945628d17722ba4172fe6dc8" == hashcode:
        print(flag)
        res[2]=flag
    elif "1beeee88127bbfaffbedea161d825230" == hashcode:
        print(flag)
        res[3]=flag
    elif "cb1ca008224675a7158b0ee3fd3ee08c" == hashcode:
        print(flag)
        res[4]=flag
print("".join(res))
# 09d15b9f2464cf02284a7e1abdb1fd17 SUper_e4sy_Md5_CR4CK
# e7c50ea784c33f4c9af6c10884f432b1
# 1b8910d2945628d17722ba4172fe6dc8
# 1beeee88127bbfaffbedea161d825230
# cb1ca008224675a7158b0ee3fd3ee08c



