[org 0x1000]
dw 0x55aa
xchg bx,bx
print:
  mov ah,0x0e
  mov si,booting
  call .next
  jmp $
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