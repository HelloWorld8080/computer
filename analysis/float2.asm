[bits 32]

section .data
value:
  dd 0
  dd 43.65
  dd 22
  dd 76.34
  dd 3.1
  dd 12.43
  dd 6
  dd 140.2
  dd 94.21
output:
  db "result = %f",10,0
section .text

extern printf
global main
main:
  finit
  fld dword [value + 4 * 1]
  fidiv dword [value + 4 * 2]

  fld dword [value + 4 * 3]
  fld dword [value + 4 * 4]
  fmul st0, st1
  fadd st0, st2
  
  fld dword [value + 4 * 5]
  fimul dword [value + 4 * 6]

  fld dword [value + 4 * 7]
  fld dword [value + 4 * 8]
  fdivp

  fsubr st0, st1
  fdivr st0, st2

  sub esp,8
  fstp qword [esp]
  push output
  call printf

  ret