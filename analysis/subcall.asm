[bits 32]
section .text
global sub
sub:
  push ebp
  mov ebp, esp
  mov eax, ecx
  sub eax, edx
  leave
  ret
section .data
  message db "add called!!!",10,0