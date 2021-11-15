#include <stdlib.h>
#include <stdio.h>

int main(){
	int fib = 0;
	int lastNum = 1;
	printf("Printing the Fibonacci numbers:\n");
	for(int i=0; i<20; i++){
		printf("%d\n", fib);
		fib = fib + lastNum;
		lastNum = fib - lastNum;
	}
	return 0;
}
	
