
offset equ 0x0000
data equ 0x1000
mov ax,1
mov ds,ax
mov ax,0x2000
mov ss,ax
int 0x10

xchg bx,bx
mov byte [offset],0x10 ;1字节
mov word [offset],0x1010 ;2字节
mov dword [offset],0x55aaeebb ;4字节

;bx bp si di
mov ax,[bx];[ds * 16 + bx]
mov ax,[bp];[ss * 16 + bp]
mov ax,[si];[ds * 16 + si]
mov ax,[di];[ds * 16 + di]

mov ax,[bx + si + 0x100];ds
mov ax,[bp + si + 0x100];ss


;[org 0x7c00]

; xchg bx,bx
; mov ax,0xb800
; mov es,ax
; mov ax,0
; mov si,message
; mov di,0
; mov cx, (message_end - message)
; loop1:

;   mov al,[ds:si]
;   mov [es:di],al
;   inc si
;   add di,2
;   loop loop1

halt:
	jmp halt
; message:
;   db "hello, world!!!",10
; message_end:

times 510 - ($ - $$) db 0 
db 0x55, 0xaa
