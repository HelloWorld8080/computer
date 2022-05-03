[bits 32]
extern exit

section .text
global main
main:
  mov eax,cr0
  push 0
  call exit