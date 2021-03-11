import time

def merge(items1, items2):
    merged_list = []
    left = 0
    right = 0

    while left < len(items1) and right < len(items2):
        if items1[left] < items2[right]:
            merged_list.append(items1[left])
            left += 1
        else:
            merged_list.append(items2[right])
            right += 1
    merged_list.extend(items1[left:])
    merged_list.extend(items2[right:])
    return merged_list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log(n)) Why and under what conditions?
    merging two lists is linear time and the recursion it log
    TODO: Memory usage: O(n) Why and under what conditions?
    Every value in list must be accessed
    """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    """
    if the len of the items is 1:
        return items
    else:
        items divided by 2
        return merge(merge sort(left items), merge sort(right items)
    """

    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]
    print(middle, left, right)
    return merge(merge_sort(left), merge_sort(right))

items = [18,24,12,4,9,44,32]
start = time.time()
print(merge_sort(items))
end = time.time()
print("%.10f" % (end - start))        