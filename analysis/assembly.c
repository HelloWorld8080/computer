#include<stdio.h>
int main(){
  int a = 1;
  int b = 2;
  int result = 30 ;
  asm volatile(
    "addl %1,%2\n"
    "movl %2,%0\n"
    : "=r"(result)
    : "r"(a), "r"(result));
  printf("%d + %d = %d", a, b, result);
}