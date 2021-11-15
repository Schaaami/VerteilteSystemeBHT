#include <iostream>

int main(){
        int fib = 0;
        int lastNum = 1;
	std::cout << ("Printing the Fibonacci numbers:") << std::endl;
        for(int i=0; i<20; i++){
		std::cout << fib << std::endl;
                fib = fib + lastNum;
                lastNum = fib - lastNum;
        }
        return 0;
}
