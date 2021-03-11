import time

def partition(items, low, high):
    pivot = items[low]
    left = low + 1
    right = high

    while True:
        while left <= right and items[right] >= pivot:
            right -= 1
        while left <= right and items[left] <= pivot:
            left += 1
        if left <= right:
            items[left], items[right] = items[right], items[left]
        else:
            break
    items[low], items[right] = items[right], items[low]
    return right

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: Θ(n log(n)) Why and under what conditions?
    TODO: Worst case running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: Θ(n log(n)) Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    """
    if low is greater than or equal to high
        return 
    make a variable for partition(items, low, high)
    quick_sort(items, low, part - 1)
    quck_sort(items, part + 1, high)
    """
    
    if low >= high:
        return
    part = partition(items, low, high)
    quick_sort(items, low, part - 1)
    quick_sort(items, part + 1, high)
    return items

items = [18,24,12,4,9,44,32]
length_of_items = len(items) - 1
start = time.time()
print(quick_sort(items, 0, length_of_items))
end = time.time()
print("%.10f" % (end - start))     