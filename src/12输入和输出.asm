[org 0x7c00]
mov ax,3
int 0x10
xchg bx,bx

CRT_ADDR_REG equ 0x3D4
CRT_DATA_REG equ 0x3D5
CRT_CURSOR_LOW equ 0x0F
CRT_CURSOR_HIGH equ 0x0E
; mov cx,10
mov ax,0xb800
mov es,ax
mov si,HELLO_WORLD
mov di,0

loop1:
	call print
	mov al,[si]
	cmp al,0
	jz loop1_end
	jmp loop1
loop1_end:
halt:
	jmp halt
print:
	call get_cursor
	mov di,ax
	xchg bx,bx
	mov bl,[si]
	mov byte [es:di],bl;移动至内存必须指明字节大小以及寄存器需与字节大小对应。
	inc si
	add di,2
	mov ax,di
	call set_cursor
	ret
set_cursor:
	push dx
	push bx
	
	shr ax,1
	mov bx,ax
	mov dx,CRT_ADDR_REG
	mov al,CRT_CURSOR_LOW
	out dx,al;相当于把CRT_CURSOR_LOW移动到CRT_ADDR_REG寄存器中
	mov dx,CRT_DATA_REG
	mov al,bl
	out dx,al

	mov dx,CRT_ADDR_REG
	mov al,CRT_CURSOR_HIGH
	out dx,al
	mov dx,CRT_DATA_REG 
	mov al,bh 
	out dx,al
	pop bx
	pop dx
	ret

get_cursor:
	push dx

	xor ax,ax
	mov dx,CRT_ADDR_REG
	mov al,CRT_CURSOR_HIGH
	out dx,al
	mov dx,CRT_DATA_REG
	in al,dx

	shl ax,8

	mov dx,CRT_ADDR_REG
	mov al,CRT_CURSOR_LOW 
	out dx,al 
	mov dx,CRT_DATA_REG 
	in al,dx 

	shl ax,1
	pop dx
	ret
HELLO_WORLD:
	db "hello,world",0
times 510 - ($ - $$) db 0 
db 0x55, 0xaa
