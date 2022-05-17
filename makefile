%.bin: %.asm
	nasm  -f bin $< -o $@
master.img: boot.bin
	yes | bximage -q -hd=16 -func=create -sectsize=512 -imgmode=flat $@
	dd if=$< of=$@ bs=512 count=1 conv=notrunc
usb: boot.bin /dev/sdb
	sudo dd if=/dev/sdb of=tmp.bin bs=512 count=1 conv=notrunc
	cp tmp.bin usb.bin
	dd if=boot.bin of=usb.bin bs=446 count=1 conv=notrunc
	sudo dd if=usb.bin of=/dev/sdb bs=512 count=1 conv=notrunc
	rm usb.bin
	sudo dd if=/dev/sdb of=tmp.bin bs=512 count=1 conv=notrunc
.PHONY: clean
clean:
	rm -rf *.bin
	rm -rf *.img
	rm -rf *.ini
.PHONY: bochs
bochs:
	bochs -q -unlock