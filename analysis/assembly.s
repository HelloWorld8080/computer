	.file	"assembly.c"
	.text
	.section	.rodata
.LC0:
	.string	"%d + %d = %d"
	.text
	.globl	main
	.type	main, @function
main:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$12, %esp
	movl	$1, -4(%ebp)
	movl	$2, -8(%ebp)
	movl	-4(%ebp), %eax
	movl	-8(%ebp), %edx
#APP
# 6 "assembly.c" 1
	addl %eax,%edx
movl %edx,%eax

# 0 "" 2
#NO_APP
	movl	%eax, -12(%ebp)
	pushl	-12(%ebp)
	pushl	-8(%ebp)
	pushl	-4(%ebp)
	pushl	$.LC0
	call	printf
	addl	$16, %esp
	movl	$0, %eax
	leave
	ret
	.size	main, .-main
	.ident	"GCC: (GNU) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
