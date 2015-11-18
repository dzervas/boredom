/* LCD Settings */
#define LDDR  DDRC
#define LPORT PORTC

#define LRES  4
#define LSCE  3
#define LDC   2
#define LSDIN 1
#define LSCLK 0

/* Resolution */
#define LX    102 /* Default for nokia 3310: 102 */
#define LY    72  /* Default for nokia 3310: 72 */
#define LTRUX 96  /* Default for nokia 3310: 96 */
#define LTRUY 65  /* Default for nokia 3310: 65 */

/* End of settings */
/* Data/cmd select */
#define CMD   0
#define DATA  1

/* Macros */
/* Get <bit> value of the byte */
#define GB(byte, bit) ((byte << (7 - bit)) >> 7)
/* Litteral to screen glyph */
#define ASCII(litteral) (litteral - 0x20)

void lclear(void);
void lprint(unsigned char character);
void lsetup(void);
void lwrite(unsigned char dc, unsigned char data);
void lwarp(unsigned char newx, unsigned char newy);
