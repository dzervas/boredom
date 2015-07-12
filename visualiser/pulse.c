#include <stdio.h>
#include <stdlib.h>
#include <pulse/simple.h>

int main() {
	pa_simple *s;
	pa_sample_spec ss;
	uint32_t *buff;

	buff = malloc(sizeof(uint32_t));
	ss.format = PA_SAMPLE_S16NE;
	ss.channels = 1;
	ss.rate = 44100;

	s = pa_simple_new(NULL,               // Use the default server.
			"visualiser",           // Our application's name.
			PA_STREAM_PLAYBACK,
			"alsa_output.pci-0000_00_1b.0.analog-stereo",               // Use the default device.
			"Music",            // Description of our stream.
			&ss,                // Our sample format.
			NULL,               // Use default channel map
			NULL,               // Use default buffering attributes.
			NULL               // Ignore error code.
			);

	if (s == NULL) {
		printf("Oops, I failed to create a pulse connection!");
		return 1;
	}

	for (;;) {
		pa_simple_read(s, buff, 1, NULL);
		printf("%u\n", buff);
	}

	return 0;
}
