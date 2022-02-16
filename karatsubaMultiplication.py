#!/usr/bin/python
import sys

# function to perform karatsuba multiplication
def karatsuba(x,y):
    # base case for recursion 
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        digit_len = max(len(str(x)), len(str(y)))
        len_by_2 = digit_len // 2
        # karatsuba multiplication of x and y can be represented as:
        # x * y = ((10**len_by_2) * a + b) * ((10**len_by_2)*c + d), where:
        # a = x // (10**len_by_2)
        # b = x % (10**len_by_2)
        # c = y // (10**len_by_2)
        # d = y % (10**len_by_2)
        # x * y  = 10**(2*len_by_2) ac + bd + 10**len_by_2 *(ad + bc)
        # ad + bc = (a+b)*(c+d) - ac - bd
        # x * y = 10**(2*len_by_2) ac + bd + 10**len_by_2 * ((a+b)*(c+d) - ac - bd)

        # calculate individual attributes
        a = x // (10**len_by_2)
        b = x % (10**len_by_2)
        c = y // (10**len_by_2)
        d = y % (10**len_by_2)

        # recursive calls to compute the products
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        prod = (10**(2*len_by_2) * ac) + bd + (10**len_by_2 *(ad_plus_bc))
        return prod

# function to test valid inputs to the program
# the inputs need to be integers
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# entry point
def main():
    # parse arguments
    args = sys.argv[1:]
    if len(args) != 2:
        raise Exception("please provide two numbers for multiplication")
    else:
        for arg in args:
            if not isInt(arg):
                sys.exit("Input arguments are not valid integers")
        x = int(args[0])
        y = int(args[1])
        minus_sign = -1

        # check for negative inputs
        if x < 0 and y < 0:
            minus_sign = 1
        elif x < 0 or y < 0:
            minus_sign = -1
        else:
            minus_sign = 1

        output = karatsuba(abs(x), abs(y)) * minus_sign

        # call karastuba multiplication method
        print("multiplication of %d and %d is %d " % (x,y,output))

if __name__ == '__main__':
    main()
