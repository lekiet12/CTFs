#include<iostream>
#include<stdio.h>
#include<string.h>
#include "defs.h"
#include "array.h"
uint32_t v20 = 0;
uint32_t v19 = 0;
uint32_t idx, v6, v3, a3, v7, v4, v5;
uint32_t *v13;
uint32_t array[33554432];
uint32_t box[8];
uint32_t enc[1600];
unsigned char v12;

int main(){
  for (int n = 0; n < 100; n++){
    for(int m1 = 0; m1 < 0x3A2E*4 ; m1++){
      mem1[m1] = mem1[n*(0x3A2E*4)+m1];
    }
    for(int m2 = 0; m2 < 0x886*4 ; m2++){
      mem2[m2] = mem2[n*(0x886*4)+m2];
    }
    for(int m3 = 0; m3 < 0x3A2E*4 ; m3++){
      mem3[m3] = mem3[n*(0x3A2E*4)+m3];
    }
      v19 = 0;
      v20 = 0;
      v6 = 0; v3 = 0; a3 = 0; v7 = 0; v4 = 0; v5 = 0;
      int k = 0;
      idx = 0;
      memset(box, 0, 8*4);
      memset(array, 0, 33554432*4);
      memset(enc, 0, 1600*4);
      for (int j = 0; j < 0x886; ++j )
      {
        a3 = (unsigned int)mem2[j];
        array[j] = a3;
      }
      while ( idx < 0x3A2E )
      {
        v13 = &mem1[4 * idx++];
        switch ( *v13 )
        {
          case 0:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[1] >> 2;
              idx = mem3[box[a3]];
            }
            else
            {
              idx = mem3[v13[1] >> 2];
            }
            break;
          case 1:
            if ( (v13[1] & 1) != 0 )
              a3 = (int)box[v13[3]] < (int)box[v13[2]];
            else
              a3 = (int)box[v13[3]] < v13[2];
            box[v13[3]] = a3;
            break;
          case 2:
            if ( (v13[1] & 1) != 0 )
              v6 = box[v13[2]];
            else
              v6 = v13[2];
            
            box[v13[3]] += v6;
            v7 = v13[3];
            a3 = box[v7] & 0xFFFFFF;
            box[v7] = a3;
            break;
          case 3:
            if ( (v13[1] & 1) != 0 )
              v3 = box[v13[2]];
            else
              v3 = v13[2];
            box[v13[3]] -= v3;
            v4 = v13[3];
            a3 = box[v4] & 0xFFFFFF;
            box[v4] = a3;
            break;
          case 4:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              if ( (int)box[v13[3]] <= (int)box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( (int)box[v13[3]] <= v13[2] )
            {
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 5:
            // if ( (v13[1] & 1) != 0 ){
            //   putchar((unsigned __int8)box[v13[2]]);
            // }
            // else
            //   putchar((unsigned __int8)v13[2]);
            break;
          case 6:
            v12 = getchar();
            // v12 = 10;
            if ( v12 == -1 )
            {
              box[v13[3]] = 0;
            }
            else
            {
              a3 = v12;
              box[v13[3]] = v12;
              // printf("box[%d] = %c ", v13[3], v12);
            }
            LOBYTE(a3) = v12;
            enc[v19++] = v12;
            break;
          case 7:
            if ( (v13[1] & 1) != 0 )
              a3 = array[box[v13[2]]];
            else
              a3 = array[v13[2]];
            box[v13[3]] = a3;
            break;
          case 8:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              if ( (int)box[v13[3]] < (int)box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( (int)box[v13[3]] < v13[2] )
            {
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 9:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              if ( box[v13[3]] != box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( box[v13[3]] != v13[2] )
            {
              // printf("box[%d] = %d != v13[2] = %d\n", v13[3], box[v13[3]], v13[2]);
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 10:
            if ( (v13[1] & 1) != 0 )
              a3 = (int)box[v13[3]] >= (int)box[v13[2]];
            else
              a3 = (int)box[v13[3]] >= v13[2];
            box[v13[3]] = a3;
            break;
          case 11:
            idx = 14894;
            break;
          case 12:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              // printf("box[%d] = %d == box[%d] = %d\n", v13[3], box[v13[3]], a3, box[a3]);
              if ( box[v13[3]] == box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( box[v13[3]] == v13[2] )
            {
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 13:
            if ( (v13[1] & 1) != 0 )
              a3 = box[v13[2]];
            else
              a3 = (unsigned int)v13[2];
            box[v13[3]] = a3;
            break;
          case 14:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              if ( (int)box[v13[3]] >= (int)box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( (int)box[v13[3]] >= v13[2] )
            {
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 15:
            if ( (v13[1] & 1) != 0 )
              a3 = (int)box[v13[3]] > (int)box[v13[2]];
            else
              a3 = (int)box[v13[3]] > v13[2];
            box[v13[3]] = a3;
            break;
          case 16:
            if ( (v13[1] & 2) != 0 )
            {
              a3 = v13[2];
              if ( (int)box[v13[3]] > (int)box[a3] )
              {
                if ( (v13[1] & 1) != 0 )
                {
                  a3 = v13[1] >> 2;
                  idx = mem3[box[a3]];
                }
                else
                {
                  idx = mem3[v13[1] >> 2];
                }
              }
            }
            else if ( (int)box[v13[3]] > v13[2] )
            {
              if ( (v13[1] & 1) != 0 )
              {
                a3 = v13[1] >> 2;
                idx = mem3[box[a3]];
              }
              else
              {
                idx = mem3[v13[1] >> 2];
              }
            }
            break;
          case 17:
            if ( (v13[1] & 1) != 0 ){
              a3 = box[v13[3]] == box[v13[2]];
            }
            else{
              a3 = box[v13[3]] == v13[2];
            }
            box[v13[3]] = a3;
            break;
          case 18:
            a3 = box[v13[3]];
            if ( (v13[1] & 1) != 0 )
              v5 = (int)box[v13[2]];
            else
              v5 = v13[2];
            array[v5] = a3;
            break;
          case 19:
            if ( (v13[1] & 1) != 0 ){
              // printf("box[%d] = %d != box[%d] = %d\n", v13[3], box[v13[3]], v13[2], box[v13[2]]);
              // if (k > 47 && k < 64){
                printf("%d,", (box[v13[2]] - box[v13[3]]));
                // k++;
              // }
              // else{
                // k++;
              // }
              a3 = box[v13[3]] != box[v13[2]];
            }
            else{
              a3 = box[v13[3]] != v13[2];
            }
            box[v13[3]] = a3;
            break;
          case 20:
            if ( (v13[1] & 1) != 0 )
              a3 = (int)box[v13[3]] <= (int)box[v13[2]];
            else
              a3 = (int)box[v13[3]] <= v13[2];
            box[v13[3]] = a3;
            break;
          default:
            continue;
        }
      }
  }
}