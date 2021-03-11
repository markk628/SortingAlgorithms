import time

def insertion_sort(items):
    for i in range(1, len(items)):
        second_value = items[i]
        second_index = i
        while second_index > 0 and items[second_index - 1] > second_value:
            items[second_index] = items[second_index - 1]
            second_index -= 1
        items[second_index] = second_value
    return items

start_time = time.time()
print(insertion_sort([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time))

def insertion_sort_recursive(items, n):
    if n <= 1:
        return

    insertion_sort_recursive(items, n - 1)

    second_value = items[n - 1]
    first_index = n-2
    while first_index >= 0 and items[first_index] > second_value:
        items[first_index + 1] = items[first_index]
        first_index -= 1
    items[first_index + 1] = second_value
    return items

start_time = time.time()
arr = [9,4,17,2]
n = len(arr)
print(insertion_sort_recursive(arr, n))
print("%.10f seconds" % (time.time() - start_time))
