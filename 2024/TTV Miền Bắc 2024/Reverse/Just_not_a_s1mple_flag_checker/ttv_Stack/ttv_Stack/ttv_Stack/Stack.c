#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define _CRT_SECURE_NO_WARNINGS

unsigned int _enc[] = { 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1 };
unsigned int unk[] = { 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 125, 103, 97, 108, 102, 32, 101, 107, 97, 102, 32, 97, 32, 116, 111, 110, 32, 116, 115, 117, 106, 32, 101, 114, 101, 104, 32, 103, 110, 105, 104, 116, 32, 116, 111, 110, 123, 67, 83, 67, 75 };
unsigned int fake[] = { 194, 61, 41, 207, 308, 222, 312, 272, 204, 117, 317, 340, 242, 71, 283, 181, 135, 280, 182, 167, 260, 1, 260, 308, 4, 296, 345, 240, 24, 247, 25, 67, 269, 0, 225, 140, 173, 354, 339, 235, 229, 218, 160, 216, 76, 104, 92, 160, 52, 200, 62, 102, 336 };

typedef struct node
{
    struct node* pNode; 
    unsigned __int8 data;
} node;

//node* head = NULL;
//node* cal = NULL;
//node* final = NULL;
__declspec(noinline) node* creatNode(unsigned __int8);
__declspec(noinline) unsigned __int8 seek(node*);
__declspec(noinline) void push(node**, node*);
__declspec(noinline) void pop(node**);
__declspec(noinline) void convertDecToX(node**, unsigned __int8, int);
__declspec(noinline) unsigned __int8 convertXToDec(unsigned __int8*, int);
__declspec(noinline) unsigned __int8 digitsToNum(unsigned __int8*);
__declspec(noinline) void convert(node**, node**, int, int);

int main()
{

    node* head = NULL;
    node* cal = NULL;
    node* final = NULL;
    for (int i = 423; i >= 0; --i)
        push(&final, creatNode(unk[i]));

    unsigned __int8 arr[100];
    printf("Show your skill: ");
    scanf("%s", arr);
    int len = strlen(arr);
    if (len == 0x35)
    {
        for (int i = 0; i < len; ++i)
            push(&head, creatNode(arr[i]));

        convert(&head, &cal, 10, 2);

        for (int i = len * 8 - 1; i >= 0; --i)
        {
            _enc[i] ^= seek(cal);
            pop(&cal);
        }

        for (int i = 0; i < len * 8; i += 2)
        {
            push(&cal, creatNode(_enc[i + 1]));
            push(&cal, creatNode(_enc[i]));
        }
        convert(&cal, &head, 2, 8);
        int cnt1 = 0;
        int cnt = 0;
        unsigned __int8 tmp[8];
        while (head != NULL)
        {
            int i = 0;
            while (i < 8)
            {
                tmp[i] = seek(head);
                pop(&head);
                i += 1;
            }
            push(&cal, creatNode(digitsToNum(tmp) ^ fake[cnt++]));
        }

        cnt = 0;
        while (cal != NULL)
        {
            if (seek(cal) == seek(final))
            {
                pop(&cal);
                pop(&final);
            }
            else
            {
                printf("Nope");
                return 0;
            }
        }
        printf("Correct\n");
    }
    else
        printf("Wrong input length\n");
    return 0;
}


__declspec(noinline) void convert(node** cur, node** _new, int _type, int k)
{
    if (_type == 10)
    {
        while (*cur != NULL)
        {
            convertDecToX(_new, seek(*cur), k);
            pop(*(&cur));
        }
    }
    else
    {
        while (*cur != NULL)
        {
            int cnt = 0;
            unsigned __int8 byte_comp[8];
            while (cnt < 8)
            {
                byte_comp[cnt++] = seek(*cur);
                pop(*(&cur));
            }
            convertDecToX(_new, convertXToDec(byte_comp, _type), k);
        }
    }
}
__declspec(noinline) unsigned __int8 digitsToNum(unsigned __int8 num[8])
{

    unsigned __int8 out = 0;
    for (int i = 0; i < 8; ++i)
        out += (num[i] * pow(10, 8 - i - 1));

    return out;
}

__declspec(noinline) unsigned __int8 convertXToDec(unsigned __int8 num[8], int type)
{
    unsigned __int8 out = 0;
    for (int i = 0; i < 8; ++i)
        out += (num[i] * pow(type, 8 - i - 1));

    return out;
}

__declspec(noinline) void convertDecToX(node** stack, unsigned __int8 n, int k)
{
    int cnt = 0;
    while (n != 0)
    {
        push(stack, creatNode(n % k));
        n /= k;
        cnt++;
    }
    while (cnt < 8)
    {
        push(stack, creatNode(0));
        cnt++;
    }
}

__declspec(noinline) node* creatNode(unsigned __int8 data)
{
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = data;
    newNode->pNode = NULL;
    return newNode;
}

__declspec(noinline) void push(node** h, node* Node)
{
    Node->pNode = *h;
    *h = Node;
}

__declspec(noinline) void pop(node** h)
{
    if (*h == NULL)
        return;
    node* n = *h;
    *h = (*h)->pNode;
    free(n);
}

__declspec(noinline) unsigned __int8 seek(node* h)
{
    if (h == NULL)
        return -1;
    return h->data;
}
