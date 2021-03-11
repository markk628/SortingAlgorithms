import time

def selection_sort(items):
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[min_index] > items[j]:
                min_index = j
        items[i], items[min_index]  = items[min_index], items[i]
    return items

start_time = time.time()
print(selection_sort([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time))

def selection_sort_recursive(items, index = 0):
    min_index = index
    for i in range(index + 1, len(items)):
        if items[i] < items[min_index]:
            min_index = i
    items[index], items[min_index] = items[min_index], items[index]

    if index + 1 < len(items):
        selection_sort_recursive(items, index + 1)
    return items

start_time_recursive = time.time()
print(selection_sort_recursive([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time_recursive))