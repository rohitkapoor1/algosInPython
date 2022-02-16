#!/usr/bin/python
# Fibonacci series: 1,1,2,3,5,8,13
# nth Fibonacci -> fibo(3) = 2, fibo(5) = 5, fibo(6) = 8 and so on
import sys
def fibo(n):
    if n <= 2:
        return 1
    else:
        #initialize last two numbers
        i = 1
        j = 1

        for x in range(3, n+1):
            sum = i + j
            i = j
            j = sum
        return sum

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.exit("provide one number")
    else:
        try:
            n = int(args[0])
        except ValueError:
            sys.exit("invalid arguments")
        if n < 0:
            sys.exit("input number cannot be negative")
        else:
            print("nth fibonacci for n: %d is %d " %(n,fibo(n)))

if __name__ == '__main__':
    main()
