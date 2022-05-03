[org 0x7c00]
xchg bx,bx

; mov ax,1
; mov bx,2
; add ax,bx

; mov ax,0xffff
; mov bx,1
; add ax,bx

; mov ax,5
; mov bx,7
; mul bx;dx : ax = bx * ax
; ; mul ax;dx : ax = ax *ax

; mov bx,4
; div bx;dx : ax /oper = ax 商 - dx 余数
;异常
;adc 借位加
;sbb 借位减
clc
mov ax,[number1]
mov bx,[number2]
add ax,bx
mov [sum],ax
mov ax,[number1+2]
mov bx,[number2+2]
adc ax,bx;进位加法将eflag的CF位为1,则ax=bx+1
mov [sum+2],ax


halt:
	jmp halt

number1:
	dd 0xcfff_ffff
number2:
	dd 4
sum:
	dd 0x0000_0000
times 510 - ($ - $$) db 0 
db 0x55, 0xaa
