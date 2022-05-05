	.file	"variable.c"
	.text
	.globl	a
	.bss
	.align 4
	.type	a, @object
	.size	a, 4
a:
	.zero	4
	.globl	b
	.data
	.align 4
	.type	b, @object
	.size	b, 4
b:
	.long	5
	.align 4
	.type	c, @object
	.size	c, 4
c:
	.long	10
	.section	.rodata
	.align 4
	.type	d, @object
	.size	d, 4
d:
	.long	20
	.globl	array
	.bss
	.align 4
	.type	array, @object
	.size	array, 20
array:
	.zero	20
	.globl	array1
	.data
	.align 4
	.type	array1, @object
	.size	array1, 20
array1:
	.long	1
	.long	2
	.long	3
	.long	4
	.long	5
	.globl	message
	.align 4
	.type	message, @object
	.size	message, 13
message:
	.string	"hello world\n"
	.ident	"GCC: (GNU) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
