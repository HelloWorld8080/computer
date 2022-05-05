[bits 32]
extern printf
section .text
global add
add:
  push ebp
  mov ebp,esp
  push message
  call printf
  ;ebp 0
  ;eip 4
  ;a 8
  ;b 12
  mov eax, [ebp + 8]
  add eax, [ebp + 12]
  leave
  ret
section .data
  message db "add called!!!",10,0