/*
����������������9��������a��n��Ҫ���д������a+aa+aaa++?+aa?a��n��a��֮�͡�
�����ʽ��
������һ���и���������9��������a��n��
�����ʽ��
��һ���а��ա�s = ��Ӧ�ĺ͡��ĸ�ʽ�����
*/
#include<stdio.h>
int get_each(int time,int value)
{
	int i,sum=1;
	//printf("time=%d,value=%d\n",time,value);
	for(i=0;i<time;i++)
		sum *= 10;
	sum = sum/10;
	//printf("\n");
	return sum;
}
int main(void)
{
	int a, n, i, sum=0, each,sum_a=0;
	scanf("%d %d", &a, &n);
	
	for(i=1;i<=n;i++)
	{
		each = get_each(i, a);
		sum += each*a;
		sum_a += sum;
	}
	printf("s = %d\n",sum_a);
	return 0;
}
