#include <curses.h>

int main() {
	SCREEN *stdterm;
	printf("Heyo! v0.1");

	initscr(); cbreak(); noecho();
	stdterm = newterm();
}
