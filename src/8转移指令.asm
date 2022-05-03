[org 0x7c00]
xchg bx,bx

; mov ax,0
; mov cx,100
start:
	; jmp short start ;一个字节
	; jmp near start ;两字节
	; jmp 0x0:0x7c00 ;段寄存器<<4 + 偏移量
	; jmp far [goto]
	; add ax,cx
	; dec cx
	; jz end
	; jmp start
end:
xchg bx,bx
halt:
	jmp halt
goto:
	db 0x7c00,0x00	
times 510 - ($ - $$) db 0 
db 0x55, 0xaa
