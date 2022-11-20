%define NEWLINE 0x0a
%define CARRIAGE_RETURN 0xd
%define BACKSPACE 0x8

%define UPPERLEFT_OUTPUT_WINDOW_COORD 0x0000  ; row 0, col 0
%define BOTTOMRIGHT_INPUT_WINDOW_COORD 0x184f  ; row 24, col 79
%define WHITE_ON_BLACK 0x0f

section .boot
bits 16
global boot
boot:
  jmp _start

; void set_cursor_pos(dx)
; args: 
;   dh - row
;   dl - col
set_cursor_pos:
  xor bh, bh
  mov ah, 2
  int 0x10
  ret

; void hash(ds:si, es:di)
; args:
;   - ds:si : src
;   - es:di : dst
; hash:
;  ret

; void putchar(al, bh)
; args:
;   - al : char
;   - bh : attrib
putchar:
  mov ah, 0x0e
  int 0x10
  ret  

; void print(ds:si)
print:
  lodsb ; load ds:si to al
  or al, al ; check for NULL byte
  jz _print_done
  xor bh, bh
  call putchar
  jmp print
_print_done:
  ret

; char(al) getchar()
; return char read from keyboard (al)
getchar:
  xor ah, ah
  int 0x16
  ret

; short read()
; args:
;   - di: es:buf
;   - si: n
read:
  xor cx, cx
  cld
_read_start:
  cmp cx, si
  jge _read_done
  call getchar

  ; enter?
  cmp al, CARRIAGE_RETURN
  je _read_done

  ; backspace?
  cmp al, 0x8 ; BACKSPACE
  jne _read_store_char

  dec cx
  dec di

  ; move back
  ; get cursor pos
  xor bh, bh
  mov ah, 3
  int 0x10

  or dl, dl ; collumn == 0?
  jz _read_move_back_one_row
  dec dl

_read_move_back_one_row:
  or dh, dh ; row == 0?
  jz _read_set_cursor_pos
  
  dec dh ; row--
  mov dl, 79 ; col = WIDTH - 1

_read_set_cursor_pos:
  call set_cursor_pos

  ; print blank char
  ; mov al, ' '
  ; call putchar

  jmp _read_start

_read_store_char:
  xor bh, bh
  call putchar

  stosb
  inc cx

  jmp _read_start

_read_done:
  xor al, al
  stosb

  mov ax, cx
  ret

reboot:
  mov si, rebootmsg       ; be polite, and say we're rebooting
  call print
  call getchar             ; and even wait for a key :)

  db 0EAh                 ; machine language to jump to FFFF:0000 (reboot)
  dw 0000h
  dw 0FFFFh

; _start
_start:
  mov ax, 0x2401
	int 0x15

  mov ax, 0x3
	int 0x10

  mov [disk], dl

  ; save es
  ; push es

  ; set ds to zero
  ; mov ax, 0x7c0
  ; mov ds, ax
  ; mov es, ax

  ; setup stack
  cli
  mov ax, 0x9000
  mov ss, ax
  mov sp, 0xffff
  sti

  ; clear screen
  mov dx, BOTTOMRIGHT_INPUT_WINDOW_COORD
  mov cx, UPPERLEFT_OUTPUT_WINDOW_COORD
  mov bh, WHITE_ON_BLACK
  mov ax, 0x0600
  int 0x10

  ; move cursor to top left window
  mov dx, 0x0000
  call set_cursor_pos

  lea si, [message]
  call print

  lea di, [buf]
  mov si, 16
  call read

  mov cx, 8
  lea si, [buf]
  lea di, [buf]
.loop:
  lodsw
  ror al, 5
  rol ah, 3
  xor ax, 0x1337
  stosw
  loop .loop

  ; memcmp(buf, payload, N)
  lea di, [buf]
  lea si, [payload]
  mov cx, 16
  repz cmpsb
  setb ah
  setb al
  sub al, ah
  jnz reboot

  mov dx, 0x0100
  call set_cursor_pos

  mov ah, 0x2    ;read sectors
	mov al, 6      ;sectors to read
	mov ch, 0      ;cylinder idx
	mov dh, 0      ;head idx
	mov cl, 2      ;sector idx
	mov dl, [disk] ;disk idx
	mov bx, kernel_stub;target pointer
	int 0x13
	cli
	lgdt [gdt_pointer]
	mov eax, cr0
	or eax,0x1
	mov cr0, eax
	mov ax, DATA_SEG
	mov ds, ax
	mov es, ax
	mov fs, ax
	mov gs, ax
	mov ss, ax
	jmp CODE_SEG:kernel_stub

message       db 'Password: ', 0
; payload       db 'redmask{realest_'
payload       db 0xa4,0x38,0x14,0x78,0x3c,0x88,0x6c,0xc8,0xa4,0x38,0x3c,0x70,0x1c,0x88,0x94,0xe9
rebootmsg     db 'Press any key to reboot', CARRIAGE_RETURN, NEWLINE, 0
buf           times 64 db 0

gdt_start:
	dq 0x0
gdt_code:
	dw 0xFFFF
	dw 0x0
	db 0x0
	db 10011010b
	db 11001111b
	db 0x0
gdt_data:
	dw 0xFFFF
	dw 0x0
	db 0x0
	db 10010010b
	db 11001111b
	db 0x0
gdt_end:
gdt_pointer:
	dw gdt_end - gdt_start
	dd gdt_start
disk:
	db 0x0
CODE_SEG equ gdt_code - gdt_start
DATA_SEG equ gdt_data - gdt_start

times 510-($-$$) db 0x58 ; 2 bytes less now
dw 0xAA55

kernel_stub:
bits 32
  mov esp, kernel_stack_top
  extern kmain
  call kmain
  cli
  hlt

section .bss
align 4
kernel_stack_bottom: equ $
	resb 16384 ; 16 KB
kernel_stack_top:

