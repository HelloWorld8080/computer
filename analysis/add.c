#include<stdio.h>

int add(int a,int b){
  int c = a + b;
  return c;
}
int main(){
  int i = 2;
  int j = 3;
  int k = add(i, j);
  printf("%d + %d = %d",i,j,k);
}