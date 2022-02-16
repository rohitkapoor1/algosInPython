#!/usr/bin/python
import sys
# Selection Sort sorts an array by repeatedly finding the
# minimum element from unsorted part and putting it at the beginning.
def find_smallest_item_index(arr):
    smallest_item_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_item_index]:
            smallest_item_index = i
    return smallest_item_index

def selectionSort(arr):
    sorted_arr = []
    for i in range(0, len(arr)):
        sorted_arr.append(arr.pop(find_smallest_item_index(arr)))
    return sorted_arr

def main():
    args = sys.argv[1:]
    if len(args[0]) == 0:
        sys.exit("input is empty")
    else:
        try:
            input_list = [int(x) for x in args[0].split(",")]
            if len(input_list) == 1:
                print(input_list)
            else:
                print(selectionSort(input_list))
        except ValueError:
            sys.exit("invalid arguments")

if __name__ == '__main__':
    main()
