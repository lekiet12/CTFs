import marshal
import dis
with open('passwordProtector.pyc', 'rb') as f:
    f.read(16) 
    code_object = marshal.load(f)
dis.dis(code_object)
secret = "Mwahahaha you will nOcmu{9gtufever crack into my passMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ympword, i'll even give you the key and the executable:::: Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
a="Ocmu{9gtuf"
b="MmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp"
c="Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
import base64
secret = "Mwahahaha you will nOcmu{9gtufever crack into my passMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ympword, i'll even give you the key and the executable:::: Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
four="Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp"
bittys = base64.b64decode(b"Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV")
decoded_third = ''.join(chr(ord(c) - 1) for c in four)
second = base64.b64decode(decoded_third)
first = int.from_bytes(second, 'big') ^ int.from_bytes(bittys, 'big')
first_bytes = first.to_bytes(len(second), 'big')
print(first_bytes)

# b'PCTF{I_<3_$3CUR1TY_THR0UGH_0B5CUR1TY!!}'