[bits 32]
section .text
global _start
_start:
  xchg bx, bx
  mov eax, 0xb8000
  mov byte [eax],'S'