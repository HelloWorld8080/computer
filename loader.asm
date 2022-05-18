[org 0x1000]
dw 0x55aa
xchg bx,bx
mov si,booting
call print
xchg bx,bx
detect_memery:
  xor ebx,ebx
  mov ax,0
  mov es,ax
  mov edi,ards_buffer
  mov edx,0x534d4150
.next:
  mov eax,0xe820
  mov ecx,20
  int 0x15
  jc error
  add di,cx
  inc word [ards_count]
  cmp ebx,0
  jnz .next
  mov si,detect_finish_m
  call print
  xchg bx,bx
  mov cx,[ards_count]
  mov si,0
  call show
  jmp $
show:
  mov eax,[ards_buffer+si]
  mov ebx,[ards_buffer+si+8]
  mov edx,[ards_buffer+si+16]
  add si,20
  xchg bx,bx
  loop show
  ret 
error:
  mov si,detect_memery_error
  call print
jmp $
print:
  mov ah,0x0e
  call .next
  ret
.next:
  mov al, [si]
  cmp al,0
  jz .done
  int 0x10
  inc si
  jmp .next
.done:
  ret
booting:
  db "booting loader....",10,13,0
detect_memery_error:
  db "error:detect_memery_error",10,13,0
detect_finish_m:
  db "detect_finish",10,13,0
ards_count:
  dw 0
ards_buffer:
