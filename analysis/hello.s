	.file	"hello.c"
	.intel_syntax noprefix
	.text
	.section	.rodata
.LC0:
	.string	"fdjfdsf"
	.text
	.globl	main
	.type	main, @function
main:
	push	ebp
	mov	ebp, esp
	push	OFFSET FLAT:.LC0
	call	printf
	add	esp, 4
	mov	eax, 0
	leave
	ret
	.size	main, .-main
	.ident	"GCC: (GNU) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
