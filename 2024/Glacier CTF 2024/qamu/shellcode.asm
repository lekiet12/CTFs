push r14
jmp r15
mov rax, rdi
jmp r15
push r12
jmp r15
push rbp
jmp r15
push rbx
jmp r15
mov rsi, qword ptr [rdi + 8]
jmp r15
mov rbx, qword ptr [rax + 0x70]
jmp r15
mov r11, qword ptr [rax + 0xa0]
jmp r15
mov rdx, rsi
jmp r15
lea rcx, [rsi + rsi*8]
jmp r15
mov rbp, qword ptr [rax + 0x60]
jmp r15
mov r9, qword ptr [rdi]
jmp r15
shl rdx, 5
jmp r15
mov rdi, qword ptr [rdi + 0x20]
jmp r15
mov r12, qword ptr [rax + 0x30]
jmp r15
lea rcx, [rdx + rcx*2]
jmp r15
mov r8, qword ptr [rax + 0x38]
jmp r15
mov r10, qword ptr [rax + 0xb0]
jmp r15
add rcx, rsi
jmp r15
shl rdx, 7
jmp r15
add rdx, rcx
jmp r15
mov rcx, rsi
jmp r15
shl rcx, 8
jmp r15
add rcx, rdx
jmp r15
shl rdx, 0x28
jmp r15
xor rcx, qword ptr [rax + 0x98]
jmp r15
mov rdx, rcx
jmp r15
lea r14, [rcx + rcx*8]
jmp r15
lea rdx, [rdx + r14*2]
jmp r15
mov r14, rcx
jmp r15
shl r14, 7
jmp r15
add r14, rdx
jmp r15
shl rcx, 0x28
jmp r15
shl rdx, 8
jmp r15
add rdx, r14
jmp r15
lea r14, [rdx + rcx]
jmp r15
xor r14, rbx
jmp r15
mov rdx, r14
jmp r15
lea rcx, [r14 + r14*8]
jmp r15
lea rdx, [rdx + rcx*2]
jmp r15
mov rcx, r14
jmp r15
shl rcx, 7
jmp r15
shl r14, 0x28
jmp r15
lea rcx, [rdx + r14]
jmp r15
xor rcx, qword ptr [rax + 0x68]
jmp r15
xor r14, qword ptr [rax + 0x10]
jmp r15
xor rcx, r11
jmp r15
xor r14, qword ptr [rax + 0x18]
jmp r15
xor rcx, qword ptr [rax + 0x90]
jmp r15
xor r14, qword ptr [rax + 0x40]
jmp r15
xor rcx, rbp
jmp r15
xor r14, qword ptr [rax + 0x78]
jmp r15
xor rcx, rdi
jmp r15
xor r14, r12
jmp r15
xor rcx, r9
jmp r15
xor r14, qword ptr [rax + 0x80]
jmp r15
xor rcx, r8
jmp r15
xor r14, r10
jmp r15
xor rcx, qword ptr [rax + 0x48]
jmp r15
xor rdx, qword ptr [rax + 0x50]
jmp r15
mov rcx, rdx
jmp r15
lea r14, [rdx + rdx*8]
jmp r15
shl rcx, 5
jmp r15
lea rcx, [rcx + r14*2]
jmp r15
mov r14, rdx
jmp r15
add r14, rcx
jmp r15
add rcx, r14
jmp r15
xor rcx, qword ptr [rax + 0xa8]
jmp r15
cmp qword ptr [rax + 0x28], 0x2d
jmp r15
sete r14b
jmp r15
cmp qword ptr [rax + 0x58], 0x2d
jmp r15
sete dl
jmp r15
and edx, r14d
jmp r15
cmp qword ptr [rax + 0x88], 0x2d
jmp r15
and r14d, edx
jmp r15
cmp qword ptr [rax + 0xb8], 0x3a
jmp r15
cmp qword ptr [rax + 0x18], 0x50
jmp r15
cmp r9, rsi
jmp r15
setne dl
jmp r15
cmp r12, r8
jmp r15
setne r14b
jmp r15
cmp qword ptr [rax + 0x18], rdi
jmp r15
cmp r9, rbp
jmp r15
lea r14, [r9 - 0x41]
jmp r15
cmp r14, 0x19
jmp r15
setbe r14b
jmp r15
lea r14, [rsi - 0x41]
jmp r15
mov r14, qword ptr [rax + 0x10]
jmp r15
sub r14, 0x41
jmp r15
lea r14, [rdi - 0x41]
jmp r15
lea r14, [r12 - 0x30]
jmp r15
cmp r14, 9
jmp r15
lea r14, [r8 - 0x30]
jmp r15
mov r14, qword ptr [rax + 0x40]
jmp r15
sub r14, 0x30
jmp r15
mov r14, qword ptr [rax + 0x48]
jmp r15
mov r14, qword ptr [rax + 0x50]
jmp r15
mov r14, qword ptr [rax + 0x98]
jmp r15
and r14, rsi
jmp r15
cmp r14, 0x48
jmp r15
cmp r14, 0x7a
jmp r15
mov r14, rsi
jmp r15
and r14, rdi
jmp r15
cmp r14, 0x40
jmp r15
mov r14, qword ptr [rax + 0x90]
jmp r15
xor r14, rdi
jmp r15
cmp r14, 0x20
jmp r15
mov r14, r9
jmp r15
or r14, r11
jmp r15
cmp r14, 0x6b
jmp r15
xor rsi, qword ptr [rax + 0x80]
jmp r15
cmp rsi, 0x1f
jmp r15
mov rsi, qword ptr [rax + 0x88]
jmp r15
add rsi, qword ptr [rax + 0x10]
jmp r15
cmp rsi, 0x7a
jmp r15
sete sil
jmp r15
and edx, esi
jmp r15
mov rsi, qword ptr [rax + 0x48]
jmp r15
or rsi, r8
jmp r15
cmp rsi, 0x30
jmp r15
add rsi, rbx
jmp r15
cmp rsi, 0x72
jmp r15
mov rsi, qword ptr [rax + 0x50]
jmp r15
add rsi, qword ptr [rax + 0x68]
jmp r15
mov rsi, qword ptr [rax + 0x58]
jmp r15
or rsi, rbx
jmp r15
cmp rsi, 0x6f
jmp r15
mov rsi, qword ptr [rax + 0x90]
jmp r15
and rsi, r8
jmp r15
or r9, r10
jmp r15
and esi, edx
jmp r15
cmp r9, 0x69
jmp r15
xor r8, r11
jmp r15
cmp r8, 0x5a
jmp r15
mov rdx, qword ptr [rax + 0x98]
jmp r15
xor rdx, r12
jmp r15
cmp rdx, 0x58
jmp r15
or rdi, rbp
jmp r15
cmp rdi, 0x51
jmp r15
and r12, qword ptr [rax + 0x40]
jmp r15
cmp r12, 0x30
jmp r15
mov rdx, qword ptr [rax + 0x78]
jmp r15
and rdx, r10
jmp r15
cmp rdx, 0x48
jmp r15
lea rdx, [rbp - 0x41]
jmp r15
cmp rdx, 0x19
jmp r15
setbe dl
jmp r15
sub rbp, 0x30
jmp r15
cmp rbp, 9
jmp r15
setbe dil
jmp r15
or edx, edi
jmp r15
mov rdi, qword ptr [rax + 0x68]
jmp r15
lea rsi, [rdi - 0x41]
jmp r15
cmp rsi, 0x19
jmp r15
setbe sil
jmp r15
sub rdi, 0x30
jmp r15
cmp rdi, 9
jmp r15
or esi, edi
jmp r15
lea rdx, [rbx - 0x41]
jmp r15
sub rbx, 0x30
jmp r15
cmp rbx, 9
jmp r15
mov rbx, qword ptr [rax + 0x78]
jmp r15
lea rsi, [rbx - 0x41]
jmp r15
lea rsi, [rbx - 0x30]
jmp r15
mov rbx, qword ptr [rax + 0x80]
jmp r15
cmp rsi, 9
jmp r15
mov rbx, qword ptr [rax + 0x90]
jmp r15
lea rsi, [rbx - 0x61]
jmp r15
mov rbx, qword ptr [rax + 0x98]
jmp r15
mov rbx, qword ptr [rax + 0xa8]
jmp r15
lea rsi, [r11 - 0x61]
jmp r15
sub r11, 0x30
jmp r15
cmp r11, 9
jmp r15
lea rsi, [r10 - 0x61]
jmp r15
sub r10, 0x30
jmp r15
cmp r10, 9
jmp r15
movzx esi, cl
jmp r15
cmp qword ptr [rax + 0xc0], rsi
jmp r15
movzx esi, ch
jmp r15
cmp qword ptr [rax + 0xc8], rsi
jmp r15
mov rsi, rcx
jmp r15
shr rsi, 0x10
jmp r15
movzx esi, sil
jmp r15
cmp qword ptr [rax + 0xd0], rsi
jmp r15
shr rsi, 0x18
jmp r15
cmp qword ptr [rax + 0xd8], rsi
jmp r15
shr rsi, 0x20
jmp r15
cmp qword ptr [rax + 0xe0], rsi
jmp r15
pop rbx
jmp r15
pop rbp
jmp r15
pop r12
jmp r15
pop r14
jmp r15
shr rsi, 0x28
jmp r15
cmp qword ptr [rax + 0xe8], rsi
jmp r15
shr rsi, 0x30
jmp r15
cmp qword ptr [rax + 0xf0], rsi
jmp r15
shr rcx, 0x38
jmp r15
cmp qword ptr [rax + 0xf8], rcx
jmp r15
sete al
jmp r15
movzx eax, al
jmp r15
and eax, edx
jmp r15
xor edx, edx
jmp r15
xor ecx, ecx
jmp r15
xor esi, esi
jmp r15
xor edi, edi
jmp r15
xor r8d, r8d
jmp r15
xor r9d, r9d
jmp r15
xor r10d, r10d
jmp r15
xor r11d, r11d
jmp r15
ret
jmp r15