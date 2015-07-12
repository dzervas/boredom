#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdint.h>

/*
f definition:
00000000004005e6 <f>:
	4005e6:		55			push   %rbp
	4005e7:		48 89 e5		mov    %rsp,%rbp
	4005ea:		be 01 00 00 00		mov    $0x1,%esi
			   ^^^^^^^^^^^ this is what i change
so it's f+5
*/
uint32_t f() {
	printf("%d\n", 1);
}

int main() {
	uint32_t *p;
	/* I found that ready */
	void *page = (void *) ((unsigned long) (&f) & ~(getpagesize() - 1));

	p = malloc(sizeof(uint32_t));

	/* mark the code section we are going to overwrite as writable. */
	mprotect(page, getpagesize(), PROT_READ | PROT_WRITE | PROT_EXEC);

	while (*p < 100) {
		f();
		memcpy(p, (f+5), sizeof(uint32_t));
		*p += 1;
		memcpy((f+5), p, sizeof(uint32_t));
	}

	return 0;
}
