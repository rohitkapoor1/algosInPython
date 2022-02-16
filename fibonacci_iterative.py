#!/usr/bin/python
# Fibonacci series: 1,1,2,3,5,8,13
# nth Fibonacci -> fibo(3) = 2, fibo(5) = 5, fibo(6) = 8 and so on
import sys
def fibo(n):
    if n <= 2:
        return 1
    else:
        arr = [0]*n
        arr[0] = 1
        arr[1] = 1
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.exit("provide one number")
    else:
        try:
            n = int(args[0])
        except ValueError:
            sys.exit("invalid argument")
        if n < 0:
            sys.exit("input number cannot be negative")
        else:
            print("nth fibonacci for n: %d is %d " %(n,fibo(n)))

if __name__ == '__main__':
    main()
