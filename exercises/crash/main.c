#include <unistd.h> // for sleep(3)
#include <stdlib.h> // for EXIT_SUCCESS
#include <stdio.h> // for printf(3)

int main(int argc, char** argv, char** envp) {
	int counter=0;
	while(1) {
		printf("Hello from C in Docker (%d)\n", counter);
		sleep(1);
		counter++;
		if(counter==5) {
			*(char*)0=0;
		}
	}
	return EXIT_SUCCESS;
}
