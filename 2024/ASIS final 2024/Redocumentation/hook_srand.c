#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

typedef void (*srand_t)(unsigned int seed);

// Define a pointer to the original srand function
srand_t original_srand = NULL;

// Our hooked version of srand
void srand(unsigned int seed) {
    if (!original_srand) {
        // Lazy load the original srand function using dlsym
        original_srand = (srand_t)dlsym(RTLD_NEXT, "srand");
    }

    // Log or modify the seed
    printf("srand called with seed: 0x%llx\n", seed);

    // Call the original srand function
    original_srand(seed);
}

// LD_PRELOAD=./hook_srand.so ./MAIN