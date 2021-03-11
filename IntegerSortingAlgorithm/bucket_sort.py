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
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]
    print(middle, left, right)
    return merge(merge_sort(left), merge_sort(right))


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n + k) Why and under what conditions?
        Must iterate through numbers first to find max value (O(n)). Then for 
        each value is run through sort of a hash function to determine where in
        the bucket list it will go (k)
    TODO: Memory usage: O(n) Why and under what conditions?
        A bucket must be created for each value in numbers"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    """
    iterate through the array and find the max value of the array
    create an empty list
    create a list of buckets with the amount of buckets being the same as the amount of items in array
    for item in array
        make a variable that equals to item times the number of items divided by max value plus 1
        insert this item into the bucket list where index equals the variable
    sort the buckets in bucket list
    append values of bucket list into empty list
    return empty list
    """

    max_value = max(numbers)
    bucket_list = []
    sorted_list = []

    for i in range(len(numbers)):
        bucket_list.append([])

    for i in range(len(numbers)):
        bucket_list_index = int(numbers[i] * num_buckets / (max_value + 1))
        bucket_list[bucket_list_index].append(numbers[i])
        merge_sort(bucket_list[bucket_list_index])
        
    # for i in range(len(numbers)):
    #     merge_sort(bucket_list[i])

    for i in range(len(numbers)):
        sorted_list += bucket_list[i]
    
    return sorted_list

items = [18,24,12,4,9,44,32,50,36,25]
start = time.time()
print(bucket_sort(items))
end = time.time()
print("%.10f" % (end - start))   