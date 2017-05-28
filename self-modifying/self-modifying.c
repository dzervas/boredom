#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdint.h>

/*
from readelf -a <executable>
f definition:
00000000004005e6 <f>:
	4005e6		55					push   %rbp
	4005e7		48 89 e5			mov    %rsp,%rbp
	4005ea		be 01 00 00 00		mov    $0x1,%esi
	4005ef		bf 04 07 40 00		mov    $0x400704,%edi
	4005f4		b8 00 00 00 00		mov    $0x0,%eax
	4005f9		e8 92 fe ff ff		callq  400490 <printf@plt>
	4005fe		90					nop
	4005ff		5d					pop    %rbp
	400600		c3					retq
*/
void f() {
	printf("%d\n", 1);
}

void g() {
	puts("Hello from G! :)\n");
}

void end() {
	puts("Hello World! :)\n");
	puts("Hello second line! :)\n");
}

int main() {
	unsigned long int *p;
	/* I found that ready */
	void *page = (void *) ((unsigned long) (&f) & ~(getpagesize() - 1));

	p = malloc(sizeof(unsigned int));
	*p = 0xe800000000 + (-1 * (0x000000000040083d - (unsigned long int) *g));

	/* Mark the code section we are going to overwrite as writable. */
	mprotect(page, getpagesize(), PROT_READ | PROT_WRITE | PROT_EXEC);
	mprotect(page, getpagesize(), PROT_READ | PROT_WRITE | PROT_EXEC);

	printf("F location: %zx\nG location: %zx\nend location: %zx\n", f, g, end);
	f();
	memcpy((f+10), g, sizeof(unsigned long int));
	f();

	return 0;
}
