#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist();

int main()
{
    struct ListNode *p, *head = NULL;

    head = createlist();
    for ( p = head; p != NULL; p = p->next )
        printf("%d ", p->data);
    printf("\n");
    return 0;
}

struct ListNode *createlist()
{
	int input;
	struct ListNode *head=NULL, *in=NULL;
	while(1)
	{
		scanf("%d", &input);
		if(input == -1)	
			return head;
		in = (struct ListNode *)malloc(sizeof(struct ListNode));
		in->data = input;
		in->next = head;
		head = in;
	}
}
//�����������Ϊ��ͷ��

 
/*
struct ListNode *createlist()
{
	int input;
	struct ListNode *head=NULL, *in=NULL;
	while(1)
	{
		scanf("%d", &input);
		if(input == -1)	
			return head;
		in = (struct ListNode *)malloc(sizeof(struct ListNode));
		in->data = input;
		in->next = head;
		head = in;
	}
}
*/

/* ��Ĵ��뽫��Ƕ������ */
