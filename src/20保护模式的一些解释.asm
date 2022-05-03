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
  xchg bx,bx
  jmp prepare_protect_mode
;   mov cx,[ards_count]
;   mov si,0
; .show:
;   mov eax, [si + ards_buffer]
;   mov ebx, [si + ards_buffer + 8]
;   mov edx, [si + ards_buffer + 16]
;   add si,20
;   ;xchg bx, bx
;   loop .show

.error:
  mov ax,0xb800
  mov es,ax
  mov byte [es:0],'E'
  jmp $
prepare_protect_mode:
  cli
  mov al,0
  in al, 0x92
  or al, 0b10
  out 0x92,al
  lgdt [gdt_ptr]
  mov eax,cr0
  or eax,1
  mov cr0,eax
  jmp dword code_selector:protect_enable
  ud2

[bits 32]
protect_enable:
  mov ax,data_selector
  mov ds,ax
  mov es,ax
  mov ss,ax
  mov fs,ax
  mov gs,ax;初始化数据段
  mov esp,0x10000
  
  mov ax,test_selector
  mov gs,ax

  xchg bx,bx
  mov word [gs:0],0x55aa
  xchg bx,bx
  mov word [gs:0x2000],0x55aa

  xchg bx,bx
  mov byte [0xb8000],'P'
  xchg bx,bx
  mov byte [0x200000],'P'
  jmp $
code_selector equ (1 << 3)
data_selector equ (2 << 3)
test_selector equ (3 << 3)
gdt_ptr:
  dw (gdt_end - gdt_base - 1)
  dd gdt_base

;保护和全局描述符
base equ 0
limit equ 0xfffff
gdt_base:
  dd 0,0
gdt_code:
  dw 0xffff ;(16位)limit_low
  dw 0 ;（8位）base_low 与24
  db 0 ;（8位）base_low
  db 0b1001_1110 ;（8位）type段类型-present
  db 0b1100_1111;(8位) limit_hight
  db 0;(8位) base_hight
gdt_data:
  dw 0xffff
  dw 0
  db 0
  db 0b1001_0010 
  db 0b1100_1111
  db 0
gdt_test:
  dw 0xfff
  dw 0x0
  db 0x1
  db 0x92
  db 0x40
  db 0x0
gdt_end:

ards_count:
  dw 0
ards_buffer: