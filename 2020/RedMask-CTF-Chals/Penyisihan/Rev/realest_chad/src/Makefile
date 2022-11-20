all:
	yasm -f elf32 booty.asm -o booty.o
	g++ -m32 kmain.cpp booty.o -o kernel.bin -I . -nostdlib -ffreestanding \
		-std=c++11 -mno-red-zone -fno-exceptions -nostdlib -fno-rtti -Wall \
		-Wextra -Werror -T linker.ld -fno-pie
test: all
	qemu-system-i386 -fda kernel.bin
debug: all
	qemu-system-i386 -fda kernel.bin -s -S
clean:
	rm *.o kernel.bin