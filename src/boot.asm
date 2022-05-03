[org 0x7c00]
mov ax,3
int 0x10
mov ax,0
mov es,ax
; xchg bx,bx
mov edi,0x1000
mov ecx,2
mov bl,4
call read_disK

; xchg bx,bx
jmp 0:0x1000
jmp $
read_disK:
;edi读取硬盘到内存的地址
;ecx 存读取扇区起始地址
;bl 存扇区数量
	push edi
	push ecx
	mov dx,0x1f2
	mov al,bl
	out dx,al;设置扇区数量

	mov al,cl
	inc dx;0x1f3
	out dx,al
	shr ecx,8

	mov al,cl
	inc dx;0x1f4
	out dx,al;除了al，out不支持别的寄存器
	shr ecx,8

	mov al,cl
	inc dx;0x1f5
	out dx,al
	shr ecx,8

	and cl,0b1111
	inc dx;0x1f6
	mov al,0b1110_0000;设置访问磁盘方式
	or al,cl
	out dx,al

	inc dx;0x1f7
	mov al,0x20;读硬盘
	out dx,al

	mov cl,bl
	call .read
	pop ecx
	pop edi
	ret

.read:
	push cx
	call .waits
	call .reads
	pop cx
	loop .read
	ret

.waits:
	mov dx,0x1f7
	mov al,0x20;
	.check:
		nop
		nop
		nop;加一点延迟

		in al,dx
		and al,0b1000_1000
		cmp al,0b0000_1000
		jnz .waits
	ret

.reads:
	mov dx,0x1f0
	mov cx,256
	.readw:
		nop
		nop
		nop
		
		in ax,dx
		mov [edi],ax
		add edi,2
		loop .readw
	ret
; xchg bx,bx
jmp $
times 510 - ($ - $$) db 0 
db 0x55, 0xaa
