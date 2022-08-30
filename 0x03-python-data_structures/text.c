#include <stdio.h>
int main(void)
{
 int arr[] = {1,2,3,4,5, 4, 3, 2, 1};
 int i, j;
 i = 0;
 j = sizeof(arr)/sizeof(int);
 //for (j = 0; ar[j] != '\0'; j++)
//	 printf("%d is %d\n",j, ar[j]);
 
 printf("%d\n", j);
j--;
int k = j;

 printf("%d\n", j);
 while (i <= k)
 {
	 printf("i is %d and j is %d\n", arr[i], arr[j]);
	 i++;
	 j--;
 }

return (0);
}
