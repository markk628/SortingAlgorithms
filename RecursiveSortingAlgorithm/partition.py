def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    """
    set pivot as last element in items
    set left pointer equal to low + 1
    set right pointer equal to high
    inside a while loop
        while left is less than or equal to right and items at index right is greater than or equal to pivot
            decrement right
        while left is less than or equal to right and items at index left is less than or equal to pivot
            increment left
        if left is less than or equal to right
            swap values of items at index left and items at index right
        else
            break the while loop
    swap values of items at index low and items at index right
    return right
    """
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