import random
import sys
def partition(arr, start, end):
    rand = random.randrange(start, end)
    arr[rand], arr[end] = arr[end], arr[rand]
    pivot = arr[end]

    i = start - 1 #index of next element smaller than pivot
    for j in range(start, end):
        if(arr[j] < pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)


def main(argv):
    inputFile = open(argv[0], "r")
    length = inputFile.readline()
    rawNums = inputFile.readline().split()
    for idx in range(0, len(rawNums)):
        rawNums[idx] = int(rawNums[idx])
    nums = rawNums
    quicksort(nums)
    for i in nums:
        print(i, end = ' ')
    print()

    
if __name__ == "__main__":
    main(sys.argv[1:])


