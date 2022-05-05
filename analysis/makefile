CFLAGS:=--static\
				-fno-asynchronous-unwind-tables\
				-fno-pic\
				-mpreferred-stack-boundary=2\
				-fno-stack-protector \
				-fno-builtin #提高代码执行效率
				# -fverbose-asm \ 在汇编语言中添加c的代码提示
				# -masm=intel

.PHONY: %.o
%.o:%.c
	gcc -m32 $(CFLAGS) -c $< -o $@ 

.PHONY: %.s
%.s:%.c
	gcc -m32 $(CFLAGS) -S $< -o $@ 

.PHONY: assembly
assembly:assembly.c
	gcc -m32 $(CFLAGS) $< -o $@ 

.PHONY: hello.s
hello.s:hello.c
	gcc -m32 $(CFLAGS) -S $< -o $@ 