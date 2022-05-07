
global amemcpy
amemcpy:
  push ebp
  mov ebp,esp 
  ;ebp 
  ;eip 4
  ;dest 8
  ;src 12
  ;count 16
  mov ecx,[ebp + 16]
  mov esi,[ebp + 12]
  mov edi,[ebp + 8]

  cld; df=0
  ;std df = 1
  rep movsb 
  ; movsw
  ; movsd

  leave
  ret
;section .text
; global main
; main:
;   push ebp
;   mov ebp, esp

;   push message.size
;   push message
;   push buffer

;   call amemcpy
;   add esp,12

;   leave
;   ret

; section .data
;   message db "hello world!!!",10,0
;   message.size equ ($ - message)
; section .bss
;   buffer resb message.size

