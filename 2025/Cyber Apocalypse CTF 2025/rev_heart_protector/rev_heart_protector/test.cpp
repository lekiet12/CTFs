#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "defs.h"
using namespace std;
struct vm{
    unsigned char* size;                
    val* value;             
    unsigned char stack[128];
    unsigned int memory[12];
    unsigned char regs[3];
    unsigned short counter;     
    unsigned char index;            
    unsigned char key[16];        
    unsigned char padding[14];        
};

struct val {
unsigned long capacity;
unsigned char data[16];
};
vm * X5BX5D___vm_u700(vm *a1, BYTE *a2, __int64 a3, unsigned __int64 a4)
{
  __int64 v4; // rbx
  __int64 v8; // r13
  unsigned __int8 *size; // rdx
  __int64 v10; // rcx
  __int64 i; // r9
  __int64 v12; // rdx
  unsigned __int8 v13; // r8

  v4 = (unsigned int)a4;
  v8 = HIDWORD(a4) - (unsigned int)a4 + 1;
  size = a1->size;
  v10 = v4;
  for ( i = 0LL; i < v8; ++i )
  {
    if ( v10 >= a3 )
    {
      v12 = a3 - 1;
    }
    v13 = a2[v10++];
    a1->value->data[i] = v13;
  }
  return a1;
}
__int64 u32__vm_u22(unsigned int *a1, __int64 a2)
{
  return *a1;
}
bool  runVM__vm_u53(vm *a1)
{
  __int64 counter; // rcx
  unsigned __int8 v3; // di
  unsigned __int16 cnt; // cx
  __int64 v5; // rcx
  __int64 index; // rcx
  __int64 v7; // rdi
  unsigned __int8 v8; // al
  __int64 v9; // rcx
  int v10; // ecx
  unsigned __int16 v11; // ax
  __int64 v12; // rcx
  __int64 v13; // rdi
  __int64 v14; // rbp
  unsigned int v15; // eax
  __int64 v16; // rcx
  __int64 v17; // rdi
  __int64 v18; // rcx
  __int64 v19; // rdi
  __int64 v20; // rcx
  int v21; // ecx
  unsigned __int16 v22; // ax
  __int64 v23; // rcx
  __int64 v24; // rdi
  __int64 v25; // rbp
  __int64 v26; // rcx
  int v27; // r9d
  unsigned __int8 *data; // rdx
  __int64 v29; // rdi
  unsigned int *v30; // rbp
  int *v31; // r13
  unsigned int *v32; // rcx
  int v33; // r14d
  __int64 v34; // rcx
  int v35; // r9d
  unsigned __int8 *v36; // rdx
  unsigned int *v37; // rcx
  __int64 v38; // rcx
  int v39; // r9d
  unsigned __int8 *v40; // rdx
  __int64 v41; // rdi
  unsigned int *v42; // rcx
  int v43; // r14d
  __int64 v44; // rcx
  int v45; // r9d
  unsigned __int8 *v46; // rdx
  __int64 v47; // rdi
  unsigned int *v48; // r12
  int *v49; // r13
  unsigned int *v50; // rcx
  char v51; // bp
  __int64 v52; // rcx
  int v53; // r9d
  unsigned __int8 *v54; // rdx
  __int64 v55; // rdi
  unsigned int *v56; // rcx
  char v57; // r12
  __int64 v58; // rcx
  int v59; // ecx
  unsigned __int16 v60; // ax
  __int64 v61; // rcx
  __int64 v62; // rbp
  __int64 v63; // rcx
  int v64; // r9d
  unsigned __int8 *v65; // rdx
  __int64 v66; // rdi
  unsigned int *v67; // rcx
  unsigned int v68; // r12d
  __int64 v69; // rcx
  unsigned int v70; // r9d
  unsigned __int8 *v71; // rdx
  unsigned __int8 v72; // di
  unsigned int *v73; // rcx
  unsigned int v74; // r12d
  bool v75; // cc
  __int64 v76; // rcx
  int v77; // ecx
  unsigned __int16 v78; // ax
  __int64 v79; // rcx
  unsigned __int8 v80; // di
  unsigned __int8 v81; // r12
  bool v82; // cf
  __int64 v83; // rcx
  __int64 v84; // rdi
  BYTE *value; // rdx
  int *v86; // r13
  unsigned int *v87; // r12
  unsigned __int16 *v88; // rcx
  BYTE *v89; // rdx
  int *v90; // r13
  unsigned int *v91; // r12
  unsigned __int16 *v92; // rcx
  int *v93; // rdi
  unsigned int *v94; // rbp
  unsigned __int16 v95; // ax
  BYTE *v96; // rdx
  unsigned __int16 *v97; // rcx
  int *v98; // rbp
  unsigned int *v99; // rdi
  BYTE *v100; // rdx
  unsigned __int16 *v101; // rcx
  int *v102; // rbp
  unsigned int *v103; // rdi
  BYTE *v104; // rdx
  unsigned __int16 *v105; // rcx
  int *v106; // rbp
  unsigned int *v107; // rdi
  BYTE *v108; // rdx
  unsigned __int16 *v109; // rcx
  int *v110; // rdi
  unsigned int *v111; // rbp
  BYTE *v112; // rdx
  unsigned __int16 *v113; // rcx
  int *v114; // rdi
  unsigned int *v115; // rbp
  __int64 v116; // rdi
  BYTE *v117; // rdx
  unsigned int *v118; // rdi
  int *v119; // r12
  unsigned __int16 *v120; // rcx
  unsigned __int16 v121; // bp
  int v122; // eax
  __int64 v123; // rcx
  unsigned __int8 v124; // cl
  unsigned __int8 v125; // al
  __int64 v126; // rcx
  int v127; // r9d
  unsigned __int8 *v128; // rdx
  __int64 v129; // rdi
  unsigned int *v130; // r13
  int *v131; // r12
  unsigned int *v132; // rcx
  int v133; // ebp
  __int64 v134; // rcx
  int v135; // ecx
  unsigned __int16 v136; // ax
  __int64 v137; // rcx
  __int64 v138; // rdi
  __int64 v139; // rbp
  __int64 v140; // rdi
  unsigned int v141; // eax
  __int64 v142; // rcx
  int v143; // ecx
  unsigned __int16 v144; // ax
  __int64 v145; // rcx
  __int64 v146; // rdi
  __int64 v147; // rbp
  _QWORD *v148; // rax
  __int64 v149; // rcx
  int v150; // ecx
  unsigned __int16 v151; // ax
  __int64 v152; // rcx
  __int64 v153; // r12
  __int64 v154; // rdi
  unsigned int v155; // edi
  BYTE *v156; // rdx
  unsigned int *v157; // rdi
  int *v158; // rbp
  unsigned int *v159; // rcx
  __int64 v160; // rdx
  int v161; // edi
  int *v163; // [rsp+30h] [rbp-58h] BYREF
  unsigned int *v164; // [rsp+38h] [rbp-50h]
  __int64 v165; // [rsp+40h] [rbp-48h] BYREF
  _BYTE v166[64]; // [rsp+48h] [rbp-40h] BYREF

  a1->counter = 5;
  a1->index = 0;
  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        while ( 1 )
        {
          while ( 1 )
          {
            while ( 1 )
            {
              while ( 1 )
              {
                counter = a1->counter;
                v3 = a1->value->data[a1->counter];
                cnt = a1->counter;
                if ( v3 )
                  break;
                v5 = (unsigned __int16)(cnt + 1);
                index = a1->index;
                v7 = a1->value->data[a1->counter + 1];
                v8 = a1->index;
                a1->stack[v8] = a1->memory[v7];
                a1->index = v8 + 1;
LABEL_32:
                a1->counter += 2;
              }
              switch ( v3 )
              {
                case 1u:
                  v9 = (unsigned __int16)(cnt + 1);
                  v10 = a1->counter;
                  v11 = v10 + 1;
                  v12 = (unsigned __int16)(v10 + 2);
                  v13 = a1->value->data[v11];
                  v14 = a1->value->data[a1->counter + 2];
                  v15 = a1->stack[a1->memory[v14] & 0x7F];
LABEL_106:
                  a1->memory[v13] = v15;
                  goto LABEL_289;
                case 2u:
                  v16 = (unsigned __int16)(cnt + 1);
                  v17 = a1->value->data[a1->counter + 1];
                  ++a1->memory[v17];
                  goto LABEL_32;
                case 3u:
                  v18 = (unsigned __int16)(cnt + 1);
                  v19 = a1->value->data[a1->counter + 1];
                  --a1->memory[v19];
                  goto LABEL_32;
                case 4u:
                  v20 = (unsigned __int16)(cnt + 1);
                  v21 = a1->counter;
                  v22 = v21 + 1;
                  v23 = (unsigned __int16)(v21 + 2);
                  v24 = a1->value->data[v22];
                  v25 = a1->value->data[a1->counter + 2];
                  a1->memory[v24] += a1->memory[v25];
                  goto LABEL_289;
                case 5u:
                  v26 = (unsigned __int16)(cnt + 1);
                  v27 = a1->counter;
                  data = a1->value->data;
                  v29 = data[(unsigned __int16)(v27 + 1)];
                  v30 = v164;
                  v31 = v163;
                  goto LABEL_65;
                case 6u:
                  v34 = (unsigned __int16)(cnt + 1);
                  v35 = a1->counter;
                  v36 = a1->value->data;
                  v29 = v36[(unsigned __int16)(v35 + 1)];
                  v30 = v164;
                  v31 = v163;
                  v37 = v164;
                  if ( v164 )
                    v37 = v164 + 2;
                  if ( a1->regs[0] )
                  {
LABEL_65:
                    a1->memory[v29] += v33;
                  }
                  goto LABEL_129;
                case 7u:
                  v38 = (unsigned __int16)(cnt + 1);
                  v39 = a1->counter;
                  v40 = a1->value->data;
                  v41 = v40[(unsigned __int16)(v39 + 1)];
                  v43 = (v39 + 2) | ((v39 + 5) << 16);
                  a1->memory[v41] -= v43;
                  goto LABEL_129;
                case 8u:
                  v44 = (unsigned __int16)(cnt + 1);
                  v45 = a1->counter;
                  v46 = a1->value->data;
                  v47 = v46[(unsigned __int16)(v45 + 1)];
                  v51 = (unsigned __int16)(v45 + 2) | ((v45 + 5) << 16);
                  a1->memory[v47] = __ROR4__(a1->memory[v47], 32 - (v51 & 0x1F));
                  a1->counter += 6;
                  v163 = v49;
                  v164 = v48;
                  goto LABEL_249;
                case 9u:
                  v52 = (unsigned __int16)(cnt + 1);
                  v53 = a1->counter;
                  v54 = a1->value->data;
                  v55 = v54[(unsigned __int16)(v53 + 1)];
                  v57 = (unsigned __int16)(v53 + 2) | ((v53 + 5) << 16);
                  a1->memory[v55] = __ROR4__(a1->memory[v55], v57);
                  goto LABEL_129;
                case 0xAu:
                  v58 = (unsigned __int16)(cnt + 1);
                  v59 = a1->counter;
                  v60 = v59 + 1;
                  v61 = (unsigned __int16)(v59 + 2);
                  v13 = a1->value->data[v60];
                  v62 = a1->value->data[a1->counter + 2];
                  v15 = a1->memory[v62];
                  goto LABEL_106;
                case 0xBu:
                  v63 = (unsigned __int16)(cnt + 1);
                  v64 = a1->counter;
                  v65 = a1->value->data;
                  v66 = v65[(unsigned __int16)(v64 + 1)];
                  v68 = (unsigned __int16)(v64 + 2) | ((v64 + 5) << 16);
                  a1->memory[v66] = v68;
                  goto LABEL_129;
                case 0xCu:
                  v69 = (unsigned __int16)(cnt + 1);
                  v70 = a1->counter;
                  v71 = a1->value->data;
                  v72 = v71[(unsigned __int16)(v70 + 1)];
                  v74 = (__int64)a1->size, (unsigned __int16)(v70 + 2) | ((v70 + 5) << 16);
                  if ( a1->memory[v72] == v74 )
                  {
                    a1->regs[0] = 1;
                    goto LABEL_128;
                  }
                  v75 = a1->memory[v72] <= v74;
                  a1->regs[0] = 0;
                  if ( v75 )
                    a1->regs[2] = 1;
                  else
LABEL_128:
                    a1->regs[2] = 0;
LABEL_129:
                  a1->counter += 6;
                  v163 = v31;
                  v164 = v30;
                  goto LABEL_249;
              }
              if ( v3 != 13 )
                break;
              v76 = (unsigned __int16)(cnt + 1);
              v77 = a1->counter;
              v78 = v77 + 1;
              v79 = (unsigned __int16)(v77 + 2);
              v80 = a1->value->data[v78];
              v81 = a1->value->data[a1->counter + 2];
              if ( a1->memory[v80] == a1->memory[v81] )
              {
                a1->regs[0] = 1;
              }
              else
              {
                v82 = a1->memory[v81] < a1->memory[v80];
                a1->regs[0] = 0;
                if ( !v82 )
                {
                  a1->regs[2] = 1;
                  goto LABEL_289;
                }
              }
              a1->regs[2] = 0;
LABEL_289:
              a1->counter += 3;
            }
            if ( v3 == 14 )
            {
              v83 = (unsigned __int16)(cnt + 1);
              v84 = a1->value->data[a1->counter + 1];
              a1->regs[0] = a1->memory[v84] == 0;
              goto LABEL_32;
            }
            if ( v3 == 15 )
            {
              value = (BYTE *)a1->value;
              if ( value )
                value += 8;
              v78 = (a1->counter + 1) | ((a1->counter + 2) << 16);
              a1->counter = v78;
              goto LABEL_224;
            }
            if ( v3 != 16 )
              break;
            v89 = (BYTE *)a1->value;
            if ( v89 )
              v89 += 8;
            v95 = ((a1->counter + 1) | ((a1->counter + 2) << 16));
            if ( a1->regs[0] )
            {
LABEL_223:
              a1->counter = v95;
              goto LABEL_224;
            }
            a1->counter += 3;
LABEL_224:
          if ( v3 == 17 )
          {
            v96 = (BYTE *)a1->value;
            if ( v96 )
              v96 += 8;
            v95 =  (a1->counter + 1) | ((a1->counter + 2) << 16);
            if ( a1->regs[0] || a1->regs[2] )
              goto LABEL_223;
            a1->counter += 3;
            goto LABEL_224;
          }
          if ( v3 == 18 )
          {
            v100 = (BYTE *)a1->value;
            if ( v100 )
              v100 += 8;
            v95 = (a1->counter + 1) | ((a1->counter + 2) << 16);
            if ( !a1->regs[2] )
              goto LABEL_223;
            a1->counter += 3;
            v163 = v102;
            v164 = v103;
          if ( v3 == 19 )
          {
            v104 = (BYTE *)a1->value;
            if ( v104 )
              v104 += 8;
            v95 = (a1->counter + 1) | ((a1->counter + 2) << 16);
            if ( !a1->regs[0] )
              goto LABEL_223;
            a1->counter += 3;
            v163 = v106;
            v164 = v107;
          if ( v3 == 20 )
          {
            v108 = (BYTE *)a1->value;
            if ( v108 )
              v108 += 8;
            v95 = (a1->counter + 1) | ((a1->counter + 2) << 16);
            if ( a1->regs[0] )
              goto LABEL_223;
            a1->counter += 3;
            goto LABEL_224;
          }
          if ( v3 == 21 )
          {
            v112 = (BYTE *)a1->value;
            if ( v112 )
              v112 += 8;
            v95 = (a1->counter + 1) | ((a1->counter + 2) << 16);
            if ( !a1->regs[0] )
              goto LABEL_223;
            a1->counter += 3;
            goto LABEL_224;
          }
          if ( v3 == 22 )
          {
            v117 = (BYTE *)a1->value;
            if ( v117 )
              v117 += 8;
            v121 = (a1->counter + 1) | ((a1->counter + 2) << 16);
            v122 = a1->counter;
            a1->counter = v122 + 3;
            a1->counter = v121;
            v163 = v119;
            v164 = v118;
            goto LABEL_249;
          }
          if ( v3 != 23 )
            break;
          v116 = 0LL;
          do
          {
            v123 = a1->index;
            v124 = a1->key[v116++];
            v125 = a1->index;
            a1->stack[v125] = v124;
            a1->index = v125 + 1;
          }
          while ( v116 != 16 );
          ++a1->counter;
        }
        if ( v3 != 24 )
          break;
        v126 = a1->counter + 1;
        v127 = a1->counter;
        v128 = a1->value->data;
        v129 = v128[(unsigned __int16)(v127 + 1)];
        v133 = (__int64)a1->size, (unsigned __int16)(v127 + 2) | ((v127 + 5) << 16);
        a1->memory[v129] *= v133;               // imul
        a1->counter += 6;
LABEL_249:
      }
      switch ( v3 )
      {
        case 0x19u:
          v134 = a1->counter + 1;
          v135 = a1->counter;
          v136 = v135 + 1;
          v137 = (unsigned __int16)(v135 + 2);
          v138 = a1->value->data[v136];
          v139 = a1->value->data[a1->counter + 2];
          v140 = v138 + 36;
          v141 = a1->memory[v139] * *((_DWORD *)&a1->size + v140);
LABEL_272:
          *((_DWORD *)&a1->size + v140) = v141;
          goto LABEL_289;
        case 0x1Au:
          v142 = a1->counter + 1;
          v143 = a1->counter;
          v144 = v143 + 1;
          v145 = (unsigned __int16)(v143 + 2);
          v146 = a1->value->data[v144];
          v147 = a1->value->data[a1->counter + 2];
          v140 = v146 + 36;
          v141 = a1->memory[v147] ^ *((_DWORD *)&a1->size + v140);// xor
          goto LABEL_272;
        case 0x1Bu:
          v149 = a1->counter + 1;
          v150 = a1->counter;
          v151 = v150 + 1;
          v152 = (unsigned __int16)(v150 + 2);
          v153 = a1->value->data[v151];
          v154 = a1->value->data[a1->counter + 2];
          v155 = a1->memory[v154];
          if ( v155 + 4 <= LODWORD(a1->size) )
          {
            v156 = (BYTE *)a1->value;
            if ( v156 )
              v156 += 8;
            v78 = (((unsigned __int64)(v155 + 3) << 32) | v155);
            a1->memory[v153] = v78;
          }
          goto LABEL_289;
      }
      if ( v3 == 28 )
        break;
    }
    v160 = *(_QWORD *)&a1->memory[8];
    if ( !v160 )
      return a1->memory[0] == 1;
    v161 = *(_DWORD *)(*(_QWORD *)&a1->memory[10] + 8);
    a1->counter = v161;
    }
    }
  }
}