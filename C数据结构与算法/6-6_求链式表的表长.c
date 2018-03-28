#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct LNode *PtrToLNode;
struct LNode {
    ElementType Data;
    PtrToLNode Next;
};
typedef PtrToLNode List;

List Read(); /* ϸ���ڴ˲��� */

int Length( List L );

int main()
{
    List L = Read();
    printf("%d\n", Length(L));
    return 0;
}

List Read()
{
    int input;
    struct LNode *head=NULL, *in=NULL, *node=NULL;

    scanf("%d", &input);
    in = (struct LNode *)malloc(sizeof(struct LNode));
    in->Data = input;
    in->Next = NULL;
    head = in;
        
    while(input != -1)
    {
        scanf("%d", &input);
        if(input == -1)
            return head;
        node = (struct LNode *)malloc(sizeof(struct LNode));
        node->Data = input;
        node->Next = NULL;
        in->Next = node;
        in = node;
    }
    return head;
}
/* ��Ĵ��뽫��Ƕ������ */
int Length( List L )
{
	List temp=L;
	int count=0;
	while(temp)
	{
		count++;
		temp = temp->Next;
	}
	return count;
	
}

