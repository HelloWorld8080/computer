[org 0x7c00]
mov ax,3
int 0x10
xchg bx,bx
; mov word [0x80 * 4 ],print
; mov word[0x80 * 4 + 2],0
; int 0x80
mov word [0 * 4],div_error
mov word [0 * 4 + 2],0
mov ax,0xb800
mov es,ax
mov ax,1
mov dx,0
mov bx,0
div bx

; call 0:print
;call far print

halt:
	jmp halt
print:
	mov byte [es:bx],'.'
	add word [video],2
	mov bx,[video]
	; ret
	; retf
	iret
div_error:
	mov byte [es:bx],'.'
	add word [video],2
	mov bx,[video]
	; ret
	; retf
	iret
video:
	dw 0x0

times 510 - ($ - $$) db 0 
db 0x55, 0xaa
