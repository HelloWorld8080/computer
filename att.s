.section .text
.global main
main:
  
  movl $4, %eax #write
  movl $1, %ebx #stdout
  movl $message, %ecx
  movb $'A', message
  movb $'B', 1(%ecx)
  movb $'C', (%ecx,%ebx, 2)
  movb $'D', message - 1(, %ebx,4)
  movb $'E', message(, %ebx, 4)
  
  movl $(message), %ecx
  movl $(message_end - message), %edx
  int $0x80

  movl $1, %eax #exit
  movl $0, %ebx #status
  int $0x80
.section .data
message:
  .asciz "hello world!!!\n"
message_end:


.section .bss
  .lcomm buffer 256