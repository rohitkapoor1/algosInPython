#!/usr/bin/python
# Fibonacci series: 1,1,2,3,5,8,13
# nth Fibonacci -> fibo(3) = 2, fibo(5) = 5, fibo(6) = 8 and so on
import sys

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise Exception("provide one number")
    else:
        try:
            input = int(args[0])
            if input < 0:
                sys.exit("input cannot be negative")
        except ValueError:
            sys.exit("invalid input")

        print("nth fibonacci for n: %d is %d " %(input,fibo(input)))

if __name__ == '__main__':
    main()
