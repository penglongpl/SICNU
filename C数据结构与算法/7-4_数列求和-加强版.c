/*
����������������9��������a��n��Ҫ���д������a+aa+aaa++?+aa?a��n��a��֮�͡�
�����ʽ��
������һ���и���������9��������a��n��
�����ʽ��
��һ���а��ա�s = ��Ӧ�ĺ͡��ĸ�ʽ�����
*/

#include<stdio.h> 
int main()
{
    int i,a,x;
    int b[100005];
    long long d = 0;
	scanf("%d %d", &a, &x);
	
	
    for(i=0;i<x;i++)
    {
        d += (x-i)*a;
        b[i]=d%10;
        d/=10;
    }
    if(d)
		printf("%d", d);
	//cout<<d;
    for(i=x-1;i>=0;i--)
		printf("%d", b[i]);
	
    if(x==0)
		printf("0");
}
