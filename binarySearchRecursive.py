#!usr/bin/python
# [1,2,3,4, 5] - input has to be sorted
# median = 2 (4/2)


def binarySearch(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    if high >= low:
        median = (low + high) // 2
        if sorted_list[median] == item:
            print("found as the %d element in the sorted input list" % (median))
            return True
        elif item < sorted_list[median]:
            binarySearch(sorted_list[:median],item)
        else:
            binarySearch(sorted_list[median+1:], item)
    else:
        print("not found")
        return False
