[org 0x7c00]
mov ax,3
int 0x10
xchg bx,bx
call print

jmp $
print:
  mov ah,0x0e
  mov si,booting
  call .next
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
  db "booting Olinux....",10,13,0
times 510 - ($ - $$) db 4

db 0x55, 0xaa