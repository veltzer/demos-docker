#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
	int i=0;
	while(1) {
		printf("hello from docker, i is %d...\n", i);
		i++;
		sleep(1);
	}
}
