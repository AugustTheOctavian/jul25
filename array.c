#include <stdio.h>
int main(void)
{
  int array[10];

  printf("read and write into array. enter 10 values\n");
  for (int i = 0; i < 10; i++)
  {
    printf("enter %d element : \n", i+1);
    scanf("%d", &array[i]);
  }
  // read the numbers
  printf("------------------------------\n");
  for (int i = 0; i < 10; i++)
  {
    printf("%d\n", array[i]);
  }

  return 0;
}