#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <stdarg.h>
#include <sys/utsname.h>
#include <sys/stat.h>
#include <stdlib.h>

FILE* pFile2;
FILE* pShell;

long int ptrace(enum __ptrace_request __request, ...){
    pid_t caller = getpid();
    va_list list;
    va_start(list, __request);
    pid_t pid = va_arg(list, pid_t);
    void* addr = va_arg(list, void*);
    void* data = va_arg(list, void*);
    long int (*orig_ptrace)(enum __ptrace_request __request, pid_t pid, void *addr, void *data);
    orig_ptrace = dlsym(RTLD_NEXT, "ptrace");
    long int result = orig_ptrace(__request, pid, addr, data);
    if (__request == PTRACE_PEEKTEXT){
        fprintf(pFile2, "PEEK (0x%lx , 0x%lx),\n", (unsigned long)addr, (unsigned long)data);
    }
    else if (__request == PTRACE_POKETEXT){
        fprintf(pShell, "%lx\n", (unsigned long)data);  
        fprintf(pFile2, "POKE (0x%lx , 0x%lx),\n", (unsigned long)addr, (unsigned long)data);
    }
    else if (__request == PTRACE_GETREGS){
        unsigned long rip = *((unsigned long*)data + 16);
        fprintf(pFile2, "GETREGS: rip: 0x%lx\n", rip);
    }
    else if (__request == PTRACE_SETREGS){
        unsigned long rip = *((unsigned long*)data + 16);
        fprintf(pFile2, "SETREGS: rip: 0x%lx\n", rip);
    }
    
    return result;
}

__attribute__((constructor)) static void setup(void) {
    printf("hello\n");
    pFile2 = fopen("./log.txt", "w");
    pShell = fopen("./shell.bin", "wb+");
}

// gcc -shared -fPIC ptrace_hook.c -ldl -o ptrace_hook.so
// LD_PRELOAD=./ptrace_hook.so ./binary