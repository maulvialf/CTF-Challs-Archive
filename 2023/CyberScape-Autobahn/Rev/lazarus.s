	.file "lazarus.pas"
	.abiversion 2
	.set	r0,0
	.set	r1,1
	.set	r2,2
	.set	r3,3
	.set	r4,4
	.set	r5,5
	.set	r6,6
	.set	r7,7
	.set	r8,8
	.set	r9,9
	.set	r10,10
	.set	r11,11
	.set	r12,12
	.set	r13,13
	.set	r14,14
	.set	r15,15
	.set	r16,16
	.set	r17,17
	.set	r18,18
	.set	r19,19
	.set	r20,20
	.set	r21,21
	.set	r22,22
	.set	r23,23
	.set	r24,24
	.set	r25,25
	.set	r26,26
	.set	r27,27
	.set	r28,28
	.set	r29,29
	.set	r30,30
	.set	r31,31
	.set	f0,0
	.set	f1,1
	.set	f2,2
	.set	f3,3
	.set	f4,4
	.set	f5,5
	.set	f6,6
	.set	f7,7
	.set	f8,8
	.set	f9,9
	.set	f10,10
	.set	f11,11
	.set	f12,12
	.set	f13,13
	.set	f14,14
	.set	f15,15
	.set	f16,16
	.set	f17,17
	.set	f18,18
	.set	f19,19
	.set	f20,20
	.set	f21,21
	.set	f22,22
	.set	f23,23
	.set	f24,24
	.set	f25,25
	.set	f26,26
	.set	f27,27
	.set	f28,28
	.set	f29,29
	.set	f30,30
	.set	f31,31
# Begin asmlist al_begin

.section .debug_line
	.type	.Ldebug_linesection0,@object
.Ldebug_linesection0:
	.type	.Ldebug_line0,@object
.Ldebug_line0:

.section .debug_abbrev
	.type	.Ldebug_abbrevsection0,@object
.Ldebug_abbrevsection0:
	.type	.Ldebug_abbrev0,@object
.Ldebug_abbrev0:

.section .text.b_DEBUGSTART_$P$LAZARUS
.globl	DEBUGSTART_$P$LAZARUS
	.type	DEBUGSTART_$P$LAZARUS,@object
DEBUGSTART_$P$LAZARUS:
# End asmlist al_begin
# Begin asmlist al_procedures

.section .text.n_p$lazarus_$$_scape$array_of_byte$byte$byte
	.balign 8
.globl	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	.type	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE,@function
P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE:
.La1:
.Ll1:
	addis	r2,r12,(.TOC.-.La1)@ha
	addi	r2,r2,(.TOC.-.La1)@l
	.localentry P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE, .-P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	mflr	r0
	std	r0,16(r1)
	stdu	r1,-144(r1)
	std	r3,96(r1)
	std	r4,120(r1)
	stb	r5,104(r1)
	stb	r6,112(r1)
.Ll2:
	lbz	r3,104(r1)
	sldi	r3,r3,1
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	stb	r3,128(r1)
.Ll3:
	lbz	r3,104(r1)
	sldi	r3,r3,1
	addi	r3,r3,2
	rldicl	r3,r3,0,56
	stb	r3,129(r1)
.Ll4:
	lbz	r3,128(r1)
	lbz	r4,112(r1)
	cmplw	r3,r4
	blt	cr0,.Lj5
	b	.Lj6
.Lj5:
	ld	r3,96(r1)
	lbz	r4,128(r1)
	ld	r5,96(r1)
	lbz	r6,104(r1)
	lbzx	r3,r3,r4
	lbzx	r4,r5,r6
	cmplw	r3,r4
	bgt	cr0,.Lj7
	b	.Lj6
.Lj7:
.Ll5:
	lbz	r3,128(r1)
	stb	r3,130(r1)
	b	.Lj8
.Lj6:
.Ll6:
	lbz	r3,104(r1)
	stb	r3,130(r1)
.Lj8:
.Ll7:
	lbz	r3,129(r1)
	lbz	r4,112(r1)
	cmplw	r3,r4
	blt	cr0,.Lj9
	b	.Lj10
.Lj9:
	ld	r3,96(r1)
	lbz	r4,129(r1)
	ld	r5,96(r1)
	lbz	r6,130(r1)
	lbzx	r3,r3,r4
	lbzx	r4,r5,r6
	cmplw	r3,r4
	bgt	cr0,.Lj11
	b	.Lj10
.Lj11:
.Ll8:
	lbz	r3,129(r1)
	stb	r3,130(r1)
.Lj10:
.Ll9:
	lbz	r3,130(r1)
	lbz	r4,104(r1)
	cmplw	r3,r4
	bne	cr0,.Lj12
	b	.Lj13
.Lj12:
.Ll10:
	ld	r4,96(r1)
	lbz	r3,104(r1)
	lbzx	r3,r4,r3
	stb	r3,131(r1)
.Ll11:
	ld	r5,96(r1)
	lbz	r6,104(r1)
	ld	r3,96(r1)
	lbz	r4,130(r1)
	lbzx	r3,r3,r4
	stbx	r3,r5,r6
.Ll12:
	ld	r3,96(r1)
	lbz	r4,130(r1)
	lbz	r5,131(r1)
	stbx	r5,r3,r4
.Ll13:
	ld	r3,96(r1)
	lbz	r6,112(r1)
	lbz	r5,130(r1)
	ld	r4,120(r1)
	bl	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	nop
.Lj13:
.Ll14:
	addi	r1,r1,144
	ld	r0,16(r1)
	mtlr	r0
	blr
.Lt2:
.Le0:
	.size	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE, .Le0 - P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
.Ll15:

.section .text.n_p$lazarus_$$_cyber$array_of_byte
	.balign 8
.globl	P$LAZARUS_$$_CYBER$array_of_BYTE
	.type	P$LAZARUS_$$_CYBER$array_of_BYTE,@function
P$LAZARUS_$$_CYBER$array_of_BYTE:
.La2:
.Ll16:
	addis	r2,r12,(.TOC.-.La2)@ha
	addi	r2,r2,(.TOC.-.La2)@l
	.localentry P$LAZARUS_$$_CYBER$array_of_BYTE, .-P$LAZARUS_$$_CYBER$array_of_BYTE
	mflr	r0
	std	r0,16(r1)
	stdu	r1,-128(r1)
	std	r3,96(r1)
	std	r4,104(r1)
.Ll17:
	ld	r3,104(r1)
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	stb	r3,113(r1)
.Ll18:
	lbz	r3,113(r1)
	li	r4,2
	divd	r3,r3,r4
	addi	r3,r3,-1
	rldicl	r3,r3,0,56
	stb	r3,112(r1)
	lbz	r3,112(r1)
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	stb	r3,112(r1)
	.balign 4
.Lj16:
	lbz	r3,112(r1)
	addi	r3,r3,-1
	rldicl	r3,r3,0,56
	stb	r3,112(r1)
.Ll19:
	ld	r3,96(r1)
	lbz	r6,113(r1)
	lbz	r5,112(r1)
	ld	r4,104(r1)
	bl	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	nop
.Ll20:
	lbz	r3,112(r1)
	cmplwi	r3,0
	ble	cr0,.Lj18
	b	.Lj16
.Lj18:
.Ll21:
	lbz	r3,113(r1)
	addi	r3,r3,-1
	rldicl	r3,r3,0,56
	cmplwi	r3,1
	bge	cr0,.Lj19
	b	.Lj20
.Lj19:
	stb	r3,112(r1)
	lbz	r3,112(r1)
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	stb	r3,112(r1)
	.balign 4
.Lj21:
	lbz	r3,112(r1)
	addi	r3,r3,-1
	rldicl	r3,r3,0,56
	stb	r3,112(r1)
.Ll22:
	ld	r4,96(r1)
	lbz	r3,112(r1)
	lbzx	r3,r4,r3
	stb	r3,114(r1)
.Ll23:
	ld	r4,96(r1)
	lbz	r5,112(r1)
	ld	r3,96(r1)
	lbz	r3,0(r3)
	stbx	r3,r4,r5
.Ll24:
	ld	r3,96(r1)
	lbz	r4,114(r1)
	stb	r4,0(r3)
.Ll25:
	ld	r3,96(r1)
	lbz	r6,112(r1)
	ld	r4,104(r1)
	li	r5,0
	bl	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	nop
.Ll26:
	lbz	r3,112(r1)
	cmplwi	r3,1
	ble	cr0,.Lj23
	b	.Lj21
.Lj23:
.Lj20:
.Ll27:
	addi	r1,r1,128
	ld	r0,16(r1)
	mtlr	r0
	blr
.Lt3:
.Le1:
	.size	P$LAZARUS_$$_CYBER$array_of_BYTE, .Le1 - P$LAZARUS_$$_CYBER$array_of_BYTE
.Ll28:

.section .text.n_main
	.balign 8
.globl	PASCALMAIN
	.type	PASCALMAIN,@function
PASCALMAIN:
.globl	main
	.type	main,@function
main:
.La3:
.Ll29:
	addis	r2,r12,(.TOC.-.La3)@ha
	addi	r2,r2,(.TOC.-.La3)@l
	.localentry main, .-main
	mflr	r0
	std	r31,-8(r1)
	std	r0,16(r1)
	stdu	r1,-112(r1)
	bl	fpc_initializeunits
	nop
.Ll30:
	bl	SYSTEM_$$_RANDOMIZE
	nop
.Ll31:
	li	r3,0
	lis	r4,(U_$SYSTEM_$$_RANDSEED)@highesta
	ori	r4,r4,(U_$SYSTEM_$$_RANDSEED)@highera
	sldi	r4,r4,32
	oris	r4,r4,(U_$SYSTEM_$$_RANDSEED)@ha
	stw	r3,(U_$SYSTEM_$$_RANDSEED)@l(r4)
.Ll32:
	li	r3,0
	lis	r4,(U_$P$LAZARUS_$$_I)@highesta
	ori	r4,r4,(U_$P$LAZARUS_$$_I)@highera
	sldi	r4,r4,32
	oris	r4,r4,(U_$P$LAZARUS_$$_I)@ha
	stb	r3,(U_$P$LAZARUS_$$_I)@l(r4)
	.balign 4
.Lj24:
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r3,(U_$P$LAZARUS_$$_I)@l(r3)
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	lis	r4,(U_$P$LAZARUS_$$_I)@highesta
	ori	r4,r4,(U_$P$LAZARUS_$$_I)@highera
	sldi	r4,r4,32
	oris	r4,r4,(U_$P$LAZARUS_$$_I)@ha
	stb	r3,(U_$P$LAZARUS_$$_I)@l(r4)
.Ll33:
	li	r3,256
	bl	SYSTEM_$$_RANDOM$LONGINT$$LONGINT
	nop
	rldicl	r3,r3,0,56
	lis	r4,(U_$P$LAZARUS_$$_I)@highesta
	ori	r4,r4,(U_$P$LAZARUS_$$_I)@highera
	sldi	r4,r4,32
	oris	r4,r4,(U_$P$LAZARUS_$$_I)@ha
	lbz	r5,(U_$P$LAZARUS_$$_I)@l(r4)
	lis	r4,(U_$P$LAZARUS_$$_A-1)@highest
	ori	r4,r4,(U_$P$LAZARUS_$$_A-1)@higher
	lis	r6,(U_$P$LAZARUS_$$_A-1)@h
	ori	r6,r6,(U_$P$LAZARUS_$$_A-1)@l
	rldimi	r6,r4,32,0
	stbx	r3,r5,r6
.Ll34:
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r3,(U_$P$LAZARUS_$$_I)@l(r3)
	cmplwi	r3,37
	bge	cr0,.Lj26
	b	.Lj24
.Lj26:
.Ll35:
	lis	r3,(U_$P$LAZARUS_$$_A)@highest
	ori	r3,r3,(U_$P$LAZARUS_$$_A)@higher
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_A)@h
	ori	r3,r3,(U_$P$LAZARUS_$$_A)@l
	li	r4,36
	bl	P$LAZARUS_$$_CYBER$array_of_BYTE
	nop
.Ll36:
	li	r4,0
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	stb	r4,(U_$P$LAZARUS_$$_I)@l(r3)
	.balign 4
.Lj27:
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r3,(U_$P$LAZARUS_$$_I)@l(r3)
	addi	r3,r3,1
	rldicl	r3,r3,0,56
	lis	r4,(U_$P$LAZARUS_$$_I)@highesta
	ori	r4,r4,(U_$P$LAZARUS_$$_I)@highera
	sldi	r4,r4,32
	oris	r4,r4,(U_$P$LAZARUS_$$_I)@ha
	stb	r3,(U_$P$LAZARUS_$$_I)@l(r4)
.Ll37:
	bl	fpc_get_output
	nop
	mr	r31,r3
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r5,(U_$P$LAZARUS_$$_I)@l(r3)
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r6,(U_$P$LAZARUS_$$_I)@l(r3)
	lis	r4,(U_$P$LAZARUS_$$_A-1)@highest
	ori	r4,r4,(U_$P$LAZARUS_$$_A-1)@higher
	lis	r3,(U_$P$LAZARUS_$$_A-1)@h
	ori	r3,r3,(U_$P$LAZARUS_$$_A-1)@l
	rldimi	r3,r4,32,0
	lbzx	r5,r5,r3
	lis	r3,(TC_$P$LAZARUS_$$_B-1)@highest
	ori	r3,r3,(TC_$P$LAZARUS_$$_B-1)@higher
	lis	r4,(TC_$P$LAZARUS_$$_B-1)@h
	ori	r4,r4,(TC_$P$LAZARUS_$$_B-1)@l
	rldimi	r4,r3,32,0
	lbzx	r3,r6,r4
	xor	r5,r3,r5
	mr	r4,r31
	li	r3,0
	bl	fpc_write_text_char
	nop
	bl	fpc_iocheck
	nop
	mr	r3,r31
	bl	fpc_write_end
	nop
	bl	fpc_iocheck
	nop
.Ll38:
	lis	r3,(U_$P$LAZARUS_$$_I)@highesta
	ori	r3,r3,(U_$P$LAZARUS_$$_I)@highera
	sldi	r3,r3,32
	oris	r3,r3,(U_$P$LAZARUS_$$_I)@ha
	lbz	r3,(U_$P$LAZARUS_$$_I)@l(r3)
	cmplwi	r3,37
	bge	cr0,.Lj29
	b	.Lj27
.Lj29:
.Ll39:
	bl	fpc_get_output
	nop
	mr	r31,r3
	mr	r3,r31
	bl	fpc_writeln_end
	nop
	bl	fpc_iocheck
	nop
.Ll40:
	bl	fpc_do_exit
	nop
	addi	r1,r1,112
	ld	r31,-8(r1)
	ld	r0,16(r1)
	mtlr	r0
	blr
.Lt1:
.Le2:
	.size	main, .Le2 - main
.Ll41:

.section .text

.section .fpc.n_links
	.quad	DEBUGSTART_$P$LAZARUS
	.quad	DEBUGEND_$P$LAZARUS
	.quad	DEBUGSTART_$SYSTEM
	.quad	DEBUGEND_$SYSTEM
	.quad	DEBUGSTART_$SI_PRC
	.quad	DEBUGEND_$SI_PRC
# End asmlist al_procedures
# Begin asmlist al_globals

.section .bss
	.balign 4
	.type U_$P$LAZARUS_$$_A,@object
	.size U_$P$LAZARUS_$$_A,37
U_$P$LAZARUS_$$_A:
	.zero 37

.section .bss
	.balign 4
	.type U_$P$LAZARUS_$$_C,@object
	.size U_$P$LAZARUS_$$_C,37
U_$P$LAZARUS_$$_C:
	.zero 37

.section .bss
	.balign 4
	.type U_$P$LAZARUS_$$_D,@object
	.size U_$P$LAZARUS_$$_D,256
U_$P$LAZARUS_$$_D:
	.zero 256

.section .bss
	.balign 4
	.type U_$P$LAZARUS_$$_I,@object
	.size U_$P$LAZARUS_$$_I,1
U_$P$LAZARUS_$$_I:
	.zero 1

.section .data.n_INITFINAL
	.balign 8
.globl	INITFINAL
	.type	INITFINAL,@object
INITFINAL:
	.quad	1,0
	.quad	INIT$_$SYSTEM
	.quad	0
.Le3:
	.size	INITFINAL, .Le3 - INITFINAL

.section .data.n_FPC_THREADVARTABLES
	.balign 8
.globl	FPC_THREADVARTABLES
	.type	FPC_THREADVARTABLES,@object
FPC_THREADVARTABLES:
	.long	1
	.quad	THREADVARLIST_$SYSTEM$indirect
.Le4:
	.size	FPC_THREADVARTABLES, .Le4 - FPC_THREADVARTABLES

.section .data.n_FPC_RESOURCESTRINGTABLES
	.balign 8
.globl	FPC_RESOURCESTRINGTABLES
	.type	FPC_RESOURCESTRINGTABLES,@object
FPC_RESOURCESTRINGTABLES:
	.quad	0
.Le5:
	.size	FPC_RESOURCESTRINGTABLES, .Le5 - FPC_RESOURCESTRINGTABLES

.section .data.n_FPC_WIDEINITTABLES
	.balign 8
.globl	FPC_WIDEINITTABLES
	.type	FPC_WIDEINITTABLES,@object
FPC_WIDEINITTABLES:
	.quad	0
.Le6:
	.size	FPC_WIDEINITTABLES, .Le6 - FPC_WIDEINITTABLES

.section .data.n_FPC_RESSTRINITTABLES
	.balign 8
.globl	FPC_RESSTRINITTABLES
	.type	FPC_RESSTRINITTABLES,@object
FPC_RESSTRINITTABLES:
	.quad	0
.Le7:
	.size	FPC_RESSTRINITTABLES, .Le7 - FPC_RESSTRINITTABLES

.section .fpc.n_version
	.balign 16
	.type	__fpc_ident,@object
__fpc_ident:
	.ascii	"FPC 3.2.2 [2021/05/23] for powerpc64 - Linux"
.Le8:
	.size	__fpc_ident, .Le8 - __fpc_ident

.section .data.n___stklen
	.balign 8
.globl	__stklen
	.type	__stklen,@object
__stklen:
	.quad	10485760
.Le9:
	.size	__stklen, .Le9 - __stklen

.section .data.n___heapsize
	.balign 8
.globl	__heapsize
	.type	__heapsize,@object
__heapsize:
	.quad	0
.Le10:
	.size	__heapsize, .Le10 - __heapsize

.section .data.n___fpc_valgrind
	.balign 8
.globl	__fpc_valgrind
	.type	__fpc_valgrind,@object
__fpc_valgrind:
	.byte	0
.Le11:
	.size	__fpc_valgrind, .Le11 - __fpc_valgrind

.section .data.n_FPC_RESLOCATION
	.balign 8
.globl	FPC_RESLOCATION
	.type	FPC_RESLOCATION,@object
FPC_RESLOCATION:
	.quad	0
.Le12:
	.size	FPC_RESLOCATION, .Le12 - FPC_RESLOCATION
# End asmlist al_globals
# Begin asmlist al_typedconsts

.section .data.n_TC_$P$LAZARUS_$$_B
	.balign 4
	.type	TC_$P$LAZARUS_$$_B,@object
TC_$P$LAZARUS_$$_B:
	.byte	68,76,81,109,36,40,51,60,91,1,85,14,68,24,79,228,191,238,167,243,162,252,146,193,143,162,243,169,229
	.byte	183,233,186,233,135,223,145,139
.Le13:
	.size	TC_$P$LAZARUS_$$_B, .Le13 - TC_$P$LAZARUS_$$_B
# End asmlist al_typedconsts
# Begin asmlist al_dwarf_info

.section .debug_info
	.type	.Ldebug_info0,@object
.Ldebug_info0:
	.long	.Ledebug_info0-.Lf2
.Lf2:
	.short	2
	.long	.Ldebug_abbrev0
	.byte	8
	.uleb128	1
	.ascii	"lazarus.pas\000"
	.ascii	"Free Pascal 3.2.2 2021/05/23\000"
	.ascii	"/vidner/CTF/cyber-scape/2023/qualification/reverse/"
	.ascii	"lazarus/\000"
	.byte	9
	.byte	3
	.long	.Ldebug_line0
	.quad	DEBUGSTART_$P$LAZARUS
	.quad	DEBUGEND_$P$LAZARUS
# Syms - Begin Staticsymtable
# Symbol SYSTEM
# Symbol FPINTRES
# Symbol LAZARUS
# Symbol main
# Symbol SCAPE
# Symbol CYBER
# Symbol A
	.uleb128	2
	.ascii	"A\000"
	.byte	9
	.byte	3
	.quad	U_$P$LAZARUS_$$_A
	.quad	_$LAZARUS$_Ld1
# Symbol B
	.uleb128	2
	.ascii	"B\000"
	.byte	9
	.byte	3
	.quad	TC_$P$LAZARUS_$$_B
	.quad	_$LAZARUS$_Ld3
# Symbol C
	.uleb128	2
	.ascii	"C\000"
	.byte	9
	.byte	3
	.quad	U_$P$LAZARUS_$$_C
	.quad	_$LAZARUS$_Ld5
# Symbol D
	.uleb128	2
	.ascii	"D\000"
	.byte	9
	.byte	3
	.quad	U_$P$LAZARUS_$$_D
	.quad	DBG_$SYSTEM_$$_SHORTSTRING
# Symbol I
	.uleb128	2
	.ascii	"I\000"
	.byte	9
	.byte	3
	.quad	U_$P$LAZARUS_$$_I
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol SI_PRC
# Syms - End Staticsymtable
# Procdef $main; StdCall;
	.uleb128	3
	.ascii	"main\000"
	.byte	1
	.byte	1
	.quad	main
	.quad	.Lt1
	.byte	0
# Procdef scape(var {Open} Array Of Byte;<const Int64>;Byte;Byte);
	.uleb128	3
	.ascii	"SCAPE\000"
	.byte	1
	.byte	1
	.quad	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	.quad	.Lt2
# Symbol A
	.uleb128	4
	.ascii	"A\000"
	.byte	4
	.byte	113
	.sleb128	96
	.byte	6
	.quad	_$LAZARUS$_Ld7
# Symbol highA
	.uleb128	4
	.ascii	"highA\000"
	.byte	3
	.byte	113
	.sleb128	120
	.quad	DBG_$SYSTEM_$$_INT64
# Symbol I
	.uleb128	4
	.ascii	"I\000"
	.byte	3
	.byte	113
	.sleb128	104
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol N
	.uleb128	4
	.ascii	"N\000"
	.byte	3
	.byte	113
	.sleb128	112
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol L
	.uleb128	2
	.ascii	"L\000"
	.byte	3
	.byte	113
	.sleb128	128
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol R
	.uleb128	2
	.ascii	"R\000"
	.byte	3
	.byte	113
	.sleb128	129
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol LARGEST
	.uleb128	2
	.ascii	"LARGEST\000"
	.byte	3
	.byte	113
	.sleb128	130
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol TEMP
	.uleb128	2
	.ascii	"TEMP\000"
	.byte	3
	.byte	113
	.sleb128	131
	.quad	DBG_$SYSTEM_$$_BYTE
# Definition {Open} Array Of Byte
.globl	_$LAZARUS$_Ld7
	.type	_$LAZARUS$_Ld7,@object
_$LAZARUS$_Ld7:
	.uleb128	5
	.quad	DBG_$SYSTEM_$$_BYTE
	.uleb128	6
	.sleb128	0
	.uleb128	1
	.quad	DBG_$SYSTEM_$$_INT64
	.byte	0
.globl	_$LAZARUS$_Ld8
	.type	_$LAZARUS$_Ld8,@object
_$LAZARUS$_Ld8:
	.uleb128	7
	.quad	_$LAZARUS$_Ld7
	.byte	0
# Procdef cyber(var {Open} Array Of Byte;<const Int64>);
	.uleb128	3
	.ascii	"CYBER\000"
	.byte	1
	.byte	1
	.quad	P$LAZARUS_$$_CYBER$array_of_BYTE
	.quad	.Lt3
# Symbol A
	.uleb128	4
	.ascii	"A\000"
	.byte	4
	.byte	113
	.sleb128	96
	.byte	6
	.quad	_$LAZARUS$_Ld9
# Symbol highA
	.uleb128	4
	.ascii	"highA\000"
	.byte	3
	.byte	113
	.sleb128	104
	.quad	DBG_$SYSTEM_$$_INT64
# Symbol I
	.uleb128	2
	.ascii	"I\000"
	.byte	3
	.byte	113
	.sleb128	112
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol N
	.uleb128	2
	.ascii	"N\000"
	.byte	3
	.byte	113
	.sleb128	113
	.quad	DBG_$SYSTEM_$$_BYTE
# Symbol TEMP
	.uleb128	2
	.ascii	"TEMP\000"
	.byte	3
	.byte	113
	.sleb128	114
	.quad	DBG_$SYSTEM_$$_BYTE
# Definition {Open} Array Of Byte
.globl	_$LAZARUS$_Ld9
	.type	_$LAZARUS$_Ld9,@object
_$LAZARUS$_Ld9:
	.uleb128	5
	.quad	DBG_$SYSTEM_$$_BYTE
	.uleb128	6
	.sleb128	0
	.uleb128	1
	.quad	DBG_$SYSTEM_$$_INT64
	.byte	0
.globl	_$LAZARUS$_Ld10
	.type	_$LAZARUS$_Ld10,@object
_$LAZARUS$_Ld10:
	.uleb128	7
	.quad	_$LAZARUS$_Ld9
	.byte	0
# Defs - Begin unit SYSTEM has index 1
# Defs - End unit SYSTEM has index 1
# Defs - Begin unit FPINTRES has index 2
# Defs - End unit FPINTRES has index 2
# Defs - Begin unit SI_PRC has index 2
# Defs - End unit SI_PRC has index 2
# Defs - Begin Staticsymtable
# Definition Array[1..37] Of Byte
.globl	_$LAZARUS$_Ld1
	.type	_$LAZARUS$_Ld1,@object
_$LAZARUS$_Ld1:
	.uleb128	8
	.uleb128	37
	.quad	DBG_$SYSTEM_$$_BYTE
	.uleb128	9
	.sleb128	1
	.sleb128	37
	.uleb128	1
	.quad	DBG_$SYSTEM_$$_SHORTINT
	.byte	0
.globl	_$LAZARUS$_Ld2
	.type	_$LAZARUS$_Ld2,@object
_$LAZARUS$_Ld2:
	.uleb128	7
	.quad	_$LAZARUS$_Ld1
# Definition Array[1..37] Of Byte
.globl	_$LAZARUS$_Ld3
	.type	_$LAZARUS$_Ld3,@object
_$LAZARUS$_Ld3:
	.uleb128	8
	.uleb128	37
	.quad	DBG_$SYSTEM_$$_BYTE
	.uleb128	9
	.sleb128	1
	.sleb128	37
	.uleb128	1
	.quad	DBG_$SYSTEM_$$_SHORTINT
	.byte	0
.globl	_$LAZARUS$_Ld4
	.type	_$LAZARUS$_Ld4,@object
_$LAZARUS$_Ld4:
	.uleb128	7
	.quad	_$LAZARUS$_Ld3
# Definition Array[1..37] Of Byte
.globl	_$LAZARUS$_Ld5
	.type	_$LAZARUS$_Ld5,@object
_$LAZARUS$_Ld5:
	.uleb128	8
	.uleb128	37
	.quad	DBG_$SYSTEM_$$_BYTE
	.uleb128	9
	.sleb128	1
	.sleb128	37
	.uleb128	1
	.quad	DBG_$SYSTEM_$$_SHORTINT
	.byte	0
.globl	_$LAZARUS$_Ld6
	.type	_$LAZARUS$_Ld6,@object
_$LAZARUS$_Ld6:
	.uleb128	7
	.quad	_$LAZARUS$_Ld5
# Defs - End Staticsymtable
	.byte	0
	.type	.Ledebug_info0,@object
.Ledebug_info0:
# End asmlist al_dwarf_info
# Begin asmlist al_dwarf_abbrev

.section .debug_abbrev
# Abbrev 1
	.uleb128	1
	.uleb128	17
	.byte	1
	.uleb128	3
	.uleb128	8
	.uleb128	37
	.uleb128	8
	.uleb128	27
	.uleb128	8
	.uleb128	19
	.uleb128	11
	.uleb128	66
	.uleb128	11
	.uleb128	16
	.uleb128	6
	.uleb128	17
	.uleb128	1
	.uleb128	18
	.uleb128	1
	.byte	0
	.byte	0
# Abbrev 2
	.uleb128	2
	.uleb128	52
	.byte	0
	.uleb128	3
	.uleb128	8
	.uleb128	2
	.uleb128	10
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 3
	.uleb128	3
	.uleb128	46
	.byte	1
	.uleb128	3
	.uleb128	8
	.uleb128	39
	.uleb128	12
	.uleb128	63
	.uleb128	12
	.uleb128	17
	.uleb128	1
	.uleb128	18
	.uleb128	1
	.byte	0
	.byte	0
# Abbrev 4
	.uleb128	4
	.uleb128	5
	.byte	0
	.uleb128	3
	.uleb128	8
	.uleb128	2
	.uleb128	10
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 5
	.uleb128	5
	.uleb128	1
	.byte	1
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 6
	.uleb128	6
	.uleb128	33
	.byte	0
	.uleb128	34
	.uleb128	13
	.uleb128	81
	.uleb128	15
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 7
	.uleb128	7
	.uleb128	16
	.byte	0
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 8
	.uleb128	8
	.uleb128	1
	.byte	1
	.uleb128	11
	.uleb128	15
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
# Abbrev 9
	.uleb128	9
	.uleb128	33
	.byte	0
	.uleb128	34
	.uleb128	13
	.uleb128	47
	.uleb128	13
	.uleb128	81
	.uleb128	15
	.uleb128	73
	.uleb128	16
	.byte	0
	.byte	0
	.byte	0
# End asmlist al_dwarf_abbrev
# Begin asmlist al_dwarf_line

.section .debug_line
# === header start ===
	.long	.Ledebug_line0-.Lf3
.Lf3:
	.short	2
	.long	.Lehdebug_line0-.Lf4
.Lf4:
	.byte	1
	.byte	1
	.byte	1
	.byte	255
	.byte	13
	.byte	0
	.byte	1
	.byte	1
	.byte	1
	.byte	1
	.byte	0
	.byte	0
	.byte	0
	.byte	1
	.byte	0
	.byte	0
	.byte	1
# include_directories
	.byte	0
# file_names
	.ascii	"lazarus.pas\000"
	.uleb128	0
	.uleb128	0
	.uleb128	0
	.byte	0
	.type	.Lehdebug_line0,@object
.Lehdebug_line0:
# === header end ===
# function: P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
# [6:1]
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll1
	.byte	5
	.uleb128	1
	.byte	17
# [7:10]
	.byte	2
	.uleb128	.Ll2-.Ll1
	.byte	5
	.uleb128	10
	.byte	13
# [8:10]
	.byte	2
	.uleb128	.Ll3-.Ll2
	.byte	13
# [9:6]
	.byte	2
	.uleb128	.Ll4-.Ll3
	.byte	5
	.uleb128	6
	.byte	13
# [10:5]
	.byte	2
	.uleb128	.Ll5-.Ll4
	.byte	5
	.uleb128	5
	.byte	13
# [12:5]
	.byte	2
	.uleb128	.Ll6-.Ll5
	.byte	14
# [13:6]
	.byte	2
	.uleb128	.Ll7-.Ll6
	.byte	5
	.uleb128	6
	.byte	13
# [14:5]
	.byte	2
	.uleb128	.Ll8-.Ll7
	.byte	5
	.uleb128	5
	.byte	13
# [15:14]
	.byte	2
	.uleb128	.Ll9-.Ll8
	.byte	5
	.uleb128	14
	.byte	13
# [17:13]
	.byte	2
	.uleb128	.Ll10-.Ll9
	.byte	5
	.uleb128	13
	.byte	14
# [18:5]
	.byte	2
	.uleb128	.Ll11-.Ll10
	.byte	5
	.uleb128	5
	.byte	13
# [19:5]
	.byte	2
	.uleb128	.Ll12-.Ll11
	.byte	13
# [21:12]
	.byte	2
	.uleb128	.Ll13-.Ll12
	.byte	5
	.uleb128	12
	.byte	14
# [23:1]
	.byte	2
	.uleb128	.Ll14-.Ll13
	.byte	5
	.uleb128	1
	.byte	14
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll15
	.byte	0
	.byte	1
	.byte	1
# ###################
# function: P$LAZARUS_$$_CYBER$array_of_BYTE
# [28:1]
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll16
	.byte	5
	.uleb128	1
	.byte	39
# [29:17]
	.byte	2
	.uleb128	.Ll17-.Ll16
	.byte	5
	.uleb128	17
	.byte	13
# [30:12]
	.byte	2
	.uleb128	.Ll18-.Ll17
	.byte	5
	.uleb128	12
	.byte	13
# [31:12]
	.byte	2
	.uleb128	.Ll19-.Ll18
	.byte	13
# [30:3]
	.byte	2
	.uleb128	.Ll20-.Ll19
	.byte	5
	.uleb128	3
	.byte	3
	.sleb128	-1
	.byte	1
# [32:12]
	.byte	2
	.uleb128	.Ll21-.Ll20
	.byte	5
	.uleb128	12
	.byte	14
# [34:13]
	.byte	2
	.uleb128	.Ll22-.Ll21
	.byte	5
	.uleb128	13
	.byte	14
# [35:5]
	.byte	2
	.uleb128	.Ll23-.Ll22
	.byte	5
	.uleb128	5
	.byte	13
# [36:5]
	.byte	2
	.uleb128	.Ll24-.Ll23
	.byte	13
# [38:12]
	.byte	2
	.uleb128	.Ll25-.Ll24
	.byte	5
	.uleb128	12
	.byte	14
# [32:3]
	.byte	2
	.uleb128	.Ll26-.Ll25
	.byte	5
	.uleb128	3
	.byte	3
	.sleb128	-6
	.byte	1
# [40:1]
	.byte	2
	.uleb128	.Ll27-.Ll26
	.byte	5
	.uleb128	1
	.byte	20
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll28
	.byte	0
	.byte	1
	.byte	1
# ###################
# function: PASCALMAIN
# function: main
# [48:1]
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll29
	.byte	5
	.uleb128	1
	.byte	59
# [49:5]
	.byte	2
	.uleb128	.Ll30-.Ll29
	.byte	5
	.uleb128	5
	.byte	13
# [50:5]
	.byte	2
	.uleb128	.Ll31-.Ll30
	.byte	13
# [51:5]
	.byte	2
	.uleb128	.Ll32-.Ll31
	.byte	13
# [52:17]
	.byte	2
	.uleb128	.Ll33-.Ll32
	.byte	5
	.uleb128	17
	.byte	13
# [51:5]
	.byte	2
	.uleb128	.Ll34-.Ll33
	.byte	5
	.uleb128	5
	.byte	3
	.sleb128	-1
	.byte	1
# [53:5]
	.byte	2
	.uleb128	.Ll35-.Ll34
	.byte	14
# [54:5]
	.byte	2
	.uleb128	.Ll36-.Ll35
	.byte	13
# [55:9]
	.byte	2
	.uleb128	.Ll37-.Ll36
	.byte	5
	.uleb128	9
	.byte	13
# [54:5]
	.byte	2
	.uleb128	.Ll38-.Ll37
	.byte	5
	.uleb128	5
	.byte	3
	.sleb128	-1
	.byte	1
# [56:5]
	.byte	2
	.uleb128	.Ll39-.Ll38
	.byte	14
# [57:1]
	.byte	2
	.uleb128	.Ll40-.Ll39
	.byte	5
	.uleb128	1
	.byte	13
	.byte	0
	.uleb128	9
	.byte	2
	.quad	.Ll41
	.byte	0
	.byte	1
	.byte	1
# ###################
	.type	.Ledebug_line0,@object
.Ledebug_line0:
# End asmlist al_dwarf_line
# Begin asmlist al_dwarf_aranges

.section .debug_aranges
	.long	.Learanges0-.Lf1
.Lf1:
	.short	2
	.long	.Ldebug_info0
	.byte	8
	.byte	0
	.long	0
	.quad	main
	.quad	.Lt1-main
	.quad	P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	.quad	.Lt2-P$LAZARUS_$$_SCAPE$array_of_BYTE$BYTE$BYTE
	.quad	P$LAZARUS_$$_CYBER$array_of_BYTE
	.quad	.Lt3-P$LAZARUS_$$_CYBER$array_of_BYTE
	.quad	0
	.quad	0
	.type	.Learanges0,@object
.Learanges0:
# End asmlist al_dwarf_aranges
# Begin asmlist al_dwarf_ranges

.section .debug_ranges
# End asmlist al_dwarf_ranges
# Begin asmlist al_end

.section .text.z_DEBUGEND_$P$LAZARUS
.globl	DEBUGEND_$P$LAZARUS
	.type	DEBUGEND_$P$LAZARUS,@object
DEBUGEND_$P$LAZARUS:
# End asmlist al_end
.section .note.GNU-stack,"",%progbits

