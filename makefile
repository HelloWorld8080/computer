CFLAGS:=-static \
				-m32 \
				-fno-asynchronous-unwind-tables\
				-fno-pic\
				-mpreferred-stack-boundary=2\
				-fno-stack-protector \
				-fno-builtin \
				-fomit-frame-pointer \
				-nostdlib \
				-nodefaultlibs \
				-nostdinc \
				-nostartfiles \
				# -fverbose-asm 在汇编语言中添加c的代码提示 
				#-fno-builtin 提高代码执行效率
				#-fomit-frame-pointer 不保存栈顶指针。执行效率较高。
				# -masm=intel intel格式编译
ENTRYINPUT:= 0x11000

build/%.o: src/%.c
	gcc $(CFLAGS) -c $< -o $@
build/%.o: src/%.asm
	nasm -f elf32 $< -o $@

build/start.bin: build/start.o build/main.o
	ld -m elf_i386 -static $^ -o $@ -Ttext $(ENTRYINPUT)

build/boot.bin: src/boot.asm
	nasm $< -o $@
build/loader.bin: src/loader.asm
	nasm $< -o $@

build/master.img: build/boot.bin build/loader.bin build/start.bin
ifeq ("$(wildcard build/master.img)", "")
	bximage -q -hd=16 -func=create -sectsize=512 -imgmode=flat $@
endif
	dd if=build/boot.bin of=$@ bs=512 count=1 conv=notrunc
	dd if=build/loader.bin of=$@ bs=512 count=4 seek=2 conv=notrunc
	dd if=build/start.bin of=$@ bs=512 count=100 seek=10 conv=notrunc

.PHONY: bochs
bochs: build/master.img
	rm -rf build/bx_enh_dbg_ini
	cd build && bochs -q -unlock
.PHONY: clean
clean:
	rm -rf build/bx_enh_dbg.ini
	rm -rf build/master.img
	rm -rf build/*.bin