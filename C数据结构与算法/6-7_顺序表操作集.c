#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 5
#define ERROR -1
typedef enum {false, true} bool;
typedef int ElementType;
typedef int Position;
typedef struct LNode *List;
struct LNode {
    ElementType Data[MAXSIZE];
    Position Last; /* �������Ա������һ��Ԫ�ص�λ�� */
};

List MakeEmpty(); 
Position Find( List L, ElementType X );
bool Insert( List L, ElementType X, Position P );
bool Delete( List L, Position P );

int main()
{
    List L;
    ElementType X;
    Position P;
    int N;

    L = MakeEmpty();
    scanf("%d", &N);
    while ( N-- ) {
        scanf("%d", &X);
        if ( Insert(L, X, 0)==false )
            printf(" Insertion Error: %d is not in.\n", X);
    }

    scanf("%d", &N);
    while ( N-- ) {
        scanf("%d", &X);
        P = Find(L, X);
        if ( P == ERROR )
            printf("Finding Error: %d is not in.\n", X);
        else
            printf("%d is at position %d.\n", X, P);
    }
    scanf("%d", &N);
    while ( N-- ) {
        scanf("%d", &P);
        if ( Delete(L, P)==false )
            printf(" Deletion Error.\n");
        if ( Insert(L, 0, P)==false )
            printf(" Insertion Error: 0 is not in.\n");
    }
    return 0;
}

/* ��Ĵ��뽫��Ƕ������ */

List MakeEmpty()
{
	struct LNode *list;
	list = (struct LNode *)malloc(sizeof(struct LNode));
	list->Last = -1;
	return list;
}


bool Insert( List L, ElementType X, Position P )
{
	printf();
	int pos=0;
	if(L->Last == MAXSIZE-1)	//��
	{
		printf("FULL");
		return false;
	}
	
	else if(P<0 || P > (L->Last+1))				//�Ƿ�
	{
		printf("ILLEGAL POSITION");
		return false;
	}
		
	for(pos = L->Last+1; pos >= P; pos--){ //��pos��λ��P; 
        L->Data[pos] = L->Data[pos-1];
    }  
    L->Data[pos] = X;
    L->Last++;
    return true;  
}

Position Find( List L, ElementType X )
{
	int pos=0;
	while(pos <= L->Last)
	{
	//	printf("#%d#%d|",pos, L->Data[pos]);
		if (X == L->Data[pos])
			return pos;
		pos++;
	}
	return ERROR;
}

bool Delete( List L, Position P )
{
	int pos;
//	printf("#%d��Ӧ��%d|", L->Data[P], P);
	if(P <0 || P > L->Last)
	{
		printf("POSITION %d EMPTY",P);
		return false;
	}
	for(pos=P; pos < L->Last; pos++)
			L->Data[pos] = L->Data[pos+1];

	L->Last--;
	return true;
}




