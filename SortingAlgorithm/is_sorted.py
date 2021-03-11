import time

def is_sorted(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True

start_time = time.time()
print(is_sorted([1,4,6,10]))
print("%.10f seconds" % (time.time() - start_time))