#include<stdio.h>

void pp(int *p, int end)
//�����ǰ�����˳��endΪ���ڳ���
{
    int i;
        for(i=0;i<end;i++)
             printf("%d",p[i]);
      printf("\n");
}

void swap(int *a, int *b)
//����a,b
{  
    int temp;  
  
    temp = *a;  
    *a = *b;  
    *b = temp;
}

void print(int *li, int start, int end)
//�ݹ���ã����ȫ����
{
    int i, j;
    int lis[end];
    for(i=0;i<end;i++)
        lis[i] = li[i];
    if(start >= end)
         pp(lis, end);
   
    else
    {
        i = start;
        for(j=start;j<end;j++)
        {
            sort(&lis, j, end);
            swap(&lis[i], &lis[j]);
            print(&lis, start+1, end);
            swap(&lis[j], &lis[i]);
        }
    }
}


void sort(int a[], int s, int n) {
    //ָ��a�У�s-n֮������ݽ��п������򣬴�С����
   int i,j,min,temp;
   for (i=s; i<n; i++)   {
        min = i;  //ȡ����ʼ�±�
        for (j=min; j<n ;j++)
            if (a[j] <= a[min])
                min = j;
    temp = a[min];
    a[min] = a[i];
    a[i] = temp;
   }
}


int main(void)
{
    int list[9];
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        list[i] = i+1;
        print(&list, 0, n);
    return 0;
}
