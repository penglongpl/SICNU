/*
����������������9��������a��n��Ҫ���д������a+aa+aaa++?+aa?a��n��a��֮�͡�
�����ʽ��
������һ���и���������9��������a��n��
�����ʽ��
��һ���а��ա�s = ��Ӧ�ĺ͡��ĸ�ʽ�����
*/
#include<stdio.h>
long long get_each(long long time)
{

	long long i, sum=1;
	for(i=0;i<time;i++)
		sum *= 10;
	sum = sum/10;
	return sum;
}

int main(void)
{
	long long a, i, n, sum=0, each, sum_a=0;
	scanf("%lld %lld", &a, &n);
	
	for(i=1;i<=n;i++)
	{
		each = get_each(i);
		sum += each*a;
		sum_a += sum;
	}
	printf("%lld\n",sum_a);
	return 0;
}
