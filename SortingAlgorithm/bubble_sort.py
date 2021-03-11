import time

def is_sorted(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True

def bubble_sort(items):
    while is_sorted(items) == False:
        for i in range(len(items) - 1):
            if items[i] >= items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items

start_time = time.time()
print(bubble_sort([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time))

def bubble_sort_recursive(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]
            return bubble_sort_recursive(items)
    return items

start_time_recursive = time.time()
print(bubble_sort_recursive([9,4,17,2]))
print("%.10f seconds" % (time.time() - start_time_recursive))
