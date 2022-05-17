[org 0x7c00]
xchg bx,bx
mov ax,3
int 0x10
xchg bx,bx
mov di,0x1000
mov ecx,0
mov bl,1
read_disK:
  
  mov dx, 0x1f2;设置扇区数量
  mov al,bl
  out dx,al

  inc dx ;0x1f3
  mov al,cl
  out dx,al

  shr ecx,8
  inc dx ;0x1f4
  mov al,cl
  out dx,al

  shr ecx,8
  inc dx ;0x1f5
  mov al,cl
  out dx,al
  
  shr ecx,8
  inc dx ;0x1f6
  and cl,0b1111
  or cl,0b1110_0000
  mov al,cl
  out dx,al
  
  inc dx ;0x1f7 读硬盘
  mov al,0x20
  out dx,al

  xor ecx,ecx
  mov cl,bl

  call .read

  xchg bx,bx
  jmp $
  
.read:
  push cx
  call .waits
  call .reads
  loop .read
  pop cx
.waits:
  mov dx,0x1f7
  .check:
    in al,dx
    jmp $+2
    jmp $+2
    jmp $+2
    and al,0b1000_1000
    cmp al,0b0000_1000
    jnz .check
  ret
.reads:
  mov dx, 0x1f0
  mov cx, 256
  .readw:
    in ax, dx
    jmp $+2
    jmp $+2
    jmp $+2
    mov [edi],ax
    add edi,2
    loop .readw
  ret


times 510 - ($ - $$) db 4

db 0x55, 0xaa