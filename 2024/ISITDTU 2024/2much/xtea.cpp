#include <stdio.h>
#include <stdint.h>
#include <stdint.h>

void encipher(unsigned int num_rounds, uint32_t v[2], uint32_t const key[4]) {
	unsigned int i;
	uint32_t v0=v[0], v1=v[1], sum=0, delta=0x9E3779B9;
	for (i=0; i < num_rounds; i++) {
		v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
		sum += delta;
		v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
	}
	v[0]=v0; v[1]=v1;
    printf("%x %x ",v[0],v[1]);
}


void decipher(unsigned int num_rounds, uint32_t v[2], uint32_t const key[4]) {
	unsigned int i;
	uint32_t v0=v[0], v1=v[1], delta=0x9E3779B9, sum=delta*num_rounds;
	for (i=0; i < num_rounds ; i++) {
		v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
		sum -= delta;
		v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
	}
	v[0]=v0; v[1]=v1;
    printf("%x %x ",v[0],v[1]);
}


int main(){
        uint32_t v1[2]={0x54495349,0x7B555444};
        uint32_t k[]={21, 21, 21, 21};
        encipher(32,v1,k);
        uint32_t v2[2]={0x24fd52d7,0x6d24a90c};
        decipher(32,v2,k);
        return 0;
}
