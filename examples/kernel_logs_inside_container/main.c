#include <unistd.h>	// for sleep(3)
#include <stdio.h>	// for printf(3)
#include <sys/mman.h>	// for mmap(2), MAP_FAILED
#include <stdlib.h>	// for EXIT_SUCCESS
#include <assert.h>	// for assert(3) 

/*
 * This is a program that allocates lots of memory and will eventually be killed
 * by the OOM
 */

int main(int argc, char** argv, char** envp) {
	size_t size=1024*1024*1024; // 1 GIG
	while(1) {
		printf("Allocating...\n");
		void* p=mmap(
			NULL,
			size,
			PROT_EXEC|PROT_READ|PROT_WRITE,
			MAP_ANONYMOUS|MAP_PRIVATE|MAP_POPULATE,
			-1,
			0
		);
		assert(p!=MAP_FAILED);
		sleep(1);
	}
	return EXIT_SUCCESS;
}
