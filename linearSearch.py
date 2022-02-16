#!/usr/bin/python
import sys

# function for linear scan for search
def linearSearch(list, item):
    for i in range(0, len(list)-1):
        if list[i] == item:
            print("item found in position %d in the list" %(i+1))
            return True
    print("item not found")
    return False

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        raise Exception("provide an list and item to search")
    else:
        try:
            input_list = [int(x) for x in args[0].split(",")]
            input_item = int(args[1])
        except ValueError:
            sys.exit("invalid list element(s)")

        linearSearch(input_list,input_item)

if __name__ == '__main__':
    main()
