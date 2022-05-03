[org 0x7c00]
mov ax,3
int 0x10
xchg bx,bx
mov edi,0x1000
mov ecx,0
mov bl,1
xchg bx,bx
jmp $
read_disK:
;edi读取硬盘
;ecx 存读取扇区起始地址
;bl 存扇区数量
	pusha;压入ax,bx,cx,dx,sp,bp,si,di
	pushab;压入eax,ebx,ecx,edx,esp,ebp,esi,edi
	mov dx,0x1f2
	mov al,dl
	out dx,al;设置扇区数量
	mov al,cl
	inc dx;0x1f3
	shr ecx,8
	out dx,cl
	shr ecx,8
	inc dx;0x1f4
	out dx,cl
	shr ecx,8
	inc dx;0x1f5
	out dx,cl

	shr ecx,8
	and cl,0b1111
	inc dx;0x1f6
	mov al,0b1110_0000;设置访问磁盘方式
	or al,cl
	out dx,al

	inc dx;0x1f7
	mov al,0x20;读硬盘
	out dx,al
	.check:
		nop
		nop
		nop;加一点延迟

		in al,dx
		and al,0b1000_1000
		cmp al,0b0000_1000
		jnz .check

	xor eax,eax
	mov al,bl
	mov dx,256
	mul dx
	mov dx,0x1f0
	mov cx,ax;cx = dx*ax

	.readw:
		nop
		nop
		nop

		in ax,dx
		mov [edi],ax
		add edi,2
		loop .readw
	
	popab

	ret
;将内存中的数据写入磁盘
xchg bx,bx
mov dx,0x1f2
mov al,1
out dx,al;设置扇区数量
mov al,2
inc dx;0x1f3
out dx,al
mov al,0
inc dx;0x1f4
out dx,al
inc dx;0x1f5
out dx,al
inc dx;0x1f6
mov al,0b1110_0000
out dx,al
inc dx;0x1f7
mov al,0x30;写硬盘
out dx,al
mov ax, 0x100
mov es,ax
mov di,0
mov dx,0x1f0
write_loop:
	nop
	nop
	nop

	mov ax,[es:di]
	out dx,ax
	add di,2
	cmp di,512
	jnz write_loop
mov dx,0x1f7
.check_write_state:
	nop
	nop
	nop;加一点延迟

	in al,dx
	and al,0b1000_0000
	cmp al,0b0000_0000
	jz .check_write_state
xchg bx,bx
jmp $
times 510 - ($ - $$) db 0 
db 0x55, 0xaa
