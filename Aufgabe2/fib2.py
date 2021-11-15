def main():
    amount = 20
    fib = 0
    lastNum = 1
    for num in range(amount):
        print(fib)
        fib, lastNum = fib+lastNum, fib 


if __name__ == "__main__":
    print("Printing Fibonacci numbers:")
    main()
