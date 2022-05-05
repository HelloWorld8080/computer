	.file	"call.c"
	.text
	.section	.rodata
.LC0:
	.string	"%d + %d = %d"
	.text
	.globl	main
	.type	main, @function
main:
	subl	$12, %esp
	movl	$2, 8(%esp)
	movl	$3, 4(%esp)
	pushl	4(%esp)
	pushl	12(%esp)
	call	add
	addl	$8, %esp
	movl	%eax, (%esp)
	pushl	(%esp)
	pushl	8(%esp)
	pushl	16(%esp)
	pushl	$.LC0
	call	printf
	addl	$16, %esp
	movl	$0, %eax
	addl	$12, %esp
	ret
	.size	main, .-main
	.ident	"GCC: (GNU) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
