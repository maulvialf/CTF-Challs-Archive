/*
 *                 Text Buffer on VGA
 * ---------------------------------------------------
 * |      attrib            |       character        |
 * ---------------------------------------------------
 * | 7  6  5  4 |3  2  1  0 | 7  6  5  4  3  2  1  0 |
 * ---------------------------------------------------
 * |   bg col   |  fg col   | code point             |
 * ---------------------------------------------------
 * no blink(?)
 * 
 **/

#define BLACK_ATTR	    0
#define BLUE_ATTR	    1
#define GREEN_ATTR	    2
#define CYAN_ATTR	    3
#define RED_ATTR	    4
#define PURPLE_ATTR	    5
#define ORANGE_ATTR	    6
#define GRAY_ATTR	    7
#define LBLUE_ATTR	    8
#define LGRENN_ATTR	    9
#define LCYAN_ATTR	    10
#define LRED_ATTR	    11
#define LPURPLE_ATTR	12
#define LORANGE_ATTR	13
#define LGRAY_ATTR	    14
#define WHITE_ATTR	    15

#define VGA_BUFFER(bg, fg, cp) ((((bg << 4) | fg) << 8) | (cp))

short* VGA_MEM = (short*) 0xb8000;

/* ================ static data ========================= */
static unsigned char flag[] = {55, 14, 231, 104, 112, 164, 148, 203, 139, 243, 47, 122, 146, 71, 20, 100, 94, 12, 159, 33, 122, 19, 144, 88, 61, 24, 168, 71, 228, 91, 215, 63};

static int val[] = {187, 119, 198, 42, 192, 31, 24, 252, 99, 84, 234, 102, 12, 134, 20, 152, 136, 204, 245, 125, 34, 70, 66, 80, 174, 47, 10, 4, 7, 114, 230, 83};
static int pos[] = {19, 22, 5, 31, 29, 27, 13, 25, 30, 0, 8, 1, 3, 2, 11, 9, 17, 21, 12, 14, 20, 10, 16, 23, 7, 4, 15, 18, 24, 26, 6, 28};

static unsigned long int next = 0x1337;

/* ================ funcs ========================= */
int rand() {
	next = next * 1103515245 + 12345;
	return (next >> 16) & 0x7FFFFFFFu;
}

unsigned int abs(int a) {
	return (a >= 0) ? a : -a;
}

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void pepega() { for (unsigned int i = 1; i; ++i); }

bool check() {
    if (pos[0] != 0 || pos[31] != 16)
        return 0;
    for (int i = 0; i < 15; ++i) {
        if (pos[i] != pos[i + 1] - 1)
            return 0;
    }
    for (int i = 16; i < 31; ++i) {
        if (pos[i] != pos[i + 1] + 1)
            return 0;
    }
    return 1;
}

/* ================ main ========================= */
extern "C" void kmain() {
	int r1, r2;
	while (!check()) {
		pepega(); /* :pepega: */
		r1 = rand();
		r2 = rand();
		swap(&val[r1], &val[r2]);
		swap(&pos[r1], &pos[r2]);
		pepega(); /* :pepega: */
	}
	for (unsigned int i = 0; i < sizeof(flag); ++i)
		VGA_MEM[i+80] = VGA_BUFFER(RED_ATTR, WHITE_ATTR, flag[i] ^ val[i]);
}
