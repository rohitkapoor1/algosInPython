#!/usr/bin/python
import sys

# binary search implementation - split the list into two halves
# and based on the value in the median, decide to scan the left or
# right half
def binarySearch(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        median = (low + high)//2
        if sorted_list[median] == item:
            print("found item in position %d in the list" % (median+1))
            return True
        elif item > sorted_list[median]:
            low = median + 1
        else:
            high = median - 1
    print("item not found in the list")
    return False

def main():
    args = sys.argv[1:]
    try:
        input_list = [int(x) for x in args[0].split(",")]
    except ValueError:
        sys.exit("invalid list element(s)")

    if len(args) < 2:
        raise Exception("provide a sorted list and an item to search")
    else:
        if len(input_list) == 0:
            raise Exception("the input sorted list is empty")
        else:
            binarySearch(input_list,int(args[1]))

if __name__ == '__main__':
    main()
