; [org 0x7c00]
; mov ax,3
; int 0x10
; xchg bx,bx
; mov edi,0x1000
; mov ecx,2
; mov bl,4
; call read_disK

; xchg bx,bx
; jmp 0:0x1000
; jmp $
; read_disK:
; ;edi读取硬盘到内存的地址
; ;ecx 存读取扇区起始地址
; ;bl 存扇区数量
; 	push edi
; 	push ecx
; 	mov dx,0x1f2
; 	mov al,bl
; 	out dx,al;设置扇区数量

; 	mov al,cl
; 	inc dx;0x1f3
; 	out dx,al
; 	shr ecx,8

; 	mov al,cl
; 	inc dx;0x1f4
; 	out dx,al;除了al，out不支持别的寄存器
; 	shr ecx,8

; 	mov al,cl
; 	inc dx;0x1f5
; 	out dx,al
; 	shr ecx,8

; 	and cl,0b1111
; 	inc dx;0x1f6
; 	mov al,0b1110_0000;设置访问磁盘方式
; 	or al,cl
; 	out dx,al

; 	inc dx;0x1f7
; 	mov al,0x20;读硬盘
; 	out dx,al

; 	mov cl,bl
; 	call .read
; 	pop ecx
; 	pop edi
; 	ret

; .read:
; 	push cx
; 	call .waits
; 	call .reads
; 	pop cx
; 	loop .read
; 	ret

; .waits:
; 	mov dx,0x1f7
; 	mov al,0x20;
; 	.check:
; 		nop
; 		nop
; 		nop;加一点延迟

; 		in al,dx
; 		and al,0b1000_1000
; 		cmp al,0b0000_1000
; 		jnz .waits
; 	ret

; .reads:
; 	mov dx,0x1f0
; 	mov cx,256
; 	.readw:
; 		nop
; 		nop
; 		nop
		
; 		in ax,dx
; 		mov [edi],ax
; 		add edi,2
; 		loop .readw
; 	ret
; xchg bx,bx
; jmp $
; times 510 - ($ - $$) db 0 
; db 0x55, 0xaa

[org 0x1000]

xchg bx,bx
check_memory:
  mov ax,0
  mov es,ax
  xor ebx,ebx
  mov edx,0x534d4150
  mov di,ards_buffer

.next:
  mov eax,0xe820
  mov ecx,20
  int 0x15
  ; xchg bx,bx
  jc .error

  add di,cx
  inc word [ards_count]
  cmp ebx,0
  jnz .next
  ; xchg bx,bx
  mov cx,[ards_count]
  mov si,0

.show:
  mov eax, [si + ards_buffer]
  mov ebx, [si + ards_buffer + 8]
  mov edx, [si + ards_buffer + 16]
  add si,20
  xchg bx, bx
  loop .show

.error:
xchg bx,bx
jmp $

ards_count:
  dw 0
ards_buffer:
