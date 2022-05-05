#include<stdio.h>

// extern int add(int a,int b);
extern int __attribute__((fastcall)) sub(int a,int b);

int main(){
  int i = 2;
  int j = 3;
  int k = sub(i, j);
  printf("%d - %d = %d",i,j,k);
}