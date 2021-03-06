#include <stdio.h>
#include <stdlib.h>

typedef struct Node *PtrToNode;
struct Node {
    int Data; /* 真真真 */
    PtrToNode Next; /* 真真真真真 */
};
typedef PtrToNode List; /* 真真真� */

int FactorialSum( List L );

int main()
{
    int N, i;
    List L, p;

    scanf("%d", &N);
    L = NULL;
    for ( i=0; i<N; i++ ) {
        p = (List)malloc(sizeof(struct Node));
        scanf("%d", &p->Data);
        p->Next = L;  L = p;
    }
    printf("%d\n", FactorialSum(L));

    return 0;
}

/* 真真真真真 */
int FactorialSum( List L )
{
    int sum = 0;
    while(L)
    {
        printf("%d ",L->Data);
        sum += get(L->Data);
        L = L->Next;
    }
    return sum;
}

int get(int i)
{
    int j, sum=1;
    for(j=1;j<=i;j++)
        sum *= j;
    return sum;
}
