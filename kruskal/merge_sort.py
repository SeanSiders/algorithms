''' -----------------------------------------------------------------------------------
Merge sort is a divide and conquer problem commonly solved using recursive techniques.
The algorithm will take a list of items, and recursively split the list in half until
there are n lists (n being the number of items in the original list). Upon
returning from the calling routine, these sublists are compared, and merged into
a composite of those sublists. The result is a completely sorted list.

Time Complexity : O(N log N)

For each item in the list, the problem is divided in half, until items are
sorted and merged one by one. This results in a log base 2 time complexity for
each item itself.
----------------------------------------------------------------------------------  '''


def sort(array:list):
    mergeSort(array, 0, len(array) - 1)


def mergeSort(array:list, start:int, end:int):
    if start >= end: return

    mid:int = (start + end) // 2
    # Partition in the array by recursively splitting the array into 2 subarrays
    mergeSort(array, start, mid)
    mergeSort(array, mid + 1, end)
    
    # Merge the sorted items 
    merge(array, start, mid, end)


def merge(array:list, start:int, mid:int, end:int):
    leftSize = (mid - start) + 1
    rightSize = (end - mid)

    left = subarray(array, start, leftSize)
    right = subarray(array, mid + 1, rightSize)

    i = 0
    j = 0
    k = start

    while i < leftSize and j < rightSize:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < leftSize:
        array[k] = left[i]
        i += 1
        k += 1

    while j < rightSize:
        array[k] = right[j]
        j += 1
        k += 1


# Copy subarray from the given array given a start and end index, then return it
def subarray(array:list, start:int, size:int) -> list:
    sub = list(range(size))

    j = 0
    for i in range(start, start + size):
        sub[j] = array[i]
        j += 1

    return sub
