CFLAGS:=-static \
				-m32 \
				-fno-asynchronous-unwind-tables\
				-fno-pic\
				-mpreferred-stack-boundary=2\
				-fno-stack-protector \
				-fno-builtin \
				-fomit-frame-pointer \
				# -fverbose-asm 在汇编语言中添加c的代码提示 
				#-fno-builtin 提高代码执行效率
				#-fomit-frame-pointer 不保存栈顶指针。执行效率较高。
				# -masm=intel intel格式编译
DEBUG:= -g

# %.pre:%.c
# 	gcc $(CFLAGS) -E $< -o $@
%.out:%.c
	gcc $(CFLAGS) $(DEBUG) $< -o $@ 

%.o:%.c
	gcc $(CFLAGS) $(DEBUG) -c $< -o $@ 

%.o:%.asm
	nasm -f elf32 $(DEBUG) $< -o $@ 

# call.out: call.o addcall.o
# 	gcc $(CFLAGS) $(DEBUG) $^ -o $@
cstring.out: astring.o cstring.o
	gcc $(CFLAGS) $(DEBUG) $^ -o $@

call.out: call.o subcall.o
	gcc $(CFLAGS) $(DEBUG) $^ -o $@
.PHONY: %.s
%.s:%.c
	gcc  $(CFLAGS) -S $< -o $@ 

.PHONY: assembly
assembly:assembly.c
	gcc  $(CFLAGS) $< -o $@ 

.PHONY: hello.s
hello.s:hello.c
	gcc  $(CFLAGS) -S $< -o $@ 
	