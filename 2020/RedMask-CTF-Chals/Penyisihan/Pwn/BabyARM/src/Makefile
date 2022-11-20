CC=arm-linux-gnueabihf-gcc
CFLAGS=-Wall -static -no-pie -fno-stack-protector
OBJ=main.o

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
	cp $@ ../docker/$@
	cp $@ ../peserta/$@

.PHONY: clean

clean:
	rm -f *.o main