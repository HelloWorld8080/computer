[org 0x7c00]
mov ax,3
int 0x10
xchg bx,bx
mov ax,0
mov ss,ax
mov ax,0x7c00
mov sp,ax
mov cx,25
mov bx,0
loop1:
	mov ax,0xb800
	mov es,ax
	call print
	loop loop1
halt:
	jmp halt
print:
	mov byte [es:bx],'.'
	add word [video],2
	mov bx,[video]
	ret
video:
	dw 0x0

times 510 - ($ - $$) db 0 
db 0x55, 0xaa
