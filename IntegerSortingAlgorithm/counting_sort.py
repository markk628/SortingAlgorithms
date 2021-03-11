import time

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n + k) Why and under what conditions?
        Must iterate through numbers first to find max value (O(n)). Then a
        series of steps must be executed to find what value in the auxillary list 
        will be changed. Then after that iterating through the aux list and 
        adding the current index's value to the next index's value. Then using
        those values to find where in the sorted array are the values in numbers
        going (all k).
    TODO: Memory usage: O(k) Why and under what conditions?
        Must created an auxillary list (range(0, max value of numbers + 1)) 
        to sort the list"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    """
    find the max value of numbers
    make a list of counts with the range of 0 to max value of numbers plus 1
    for number in numbers
        add 1 to the count of index where it equals to number
    for index in range of length of list
        value of list at index plus 1 equals value of list at index plus the value of index plus 1
    for number in range of length of list
        add number to sorted list at index list at index number minus 1
    return list
    """

    max_value = max(numbers) + 1
    aux_list = []
    sorted_list = []

    for i in range(max_value):
        aux_list.append(0)
    
    for i in range(len(numbers)):
        sorted_list.append(0)
    
    for i in range(len(numbers)):
        aux_list[numbers[i]] += 1

    for i in range(len(aux_list)):
        if i < max_value - 1:
            aux_list[i + 1] += aux_list[i]
        else:
            break
    
    for i in range(len(numbers)):
        sorted_list[aux_list[numbers[i]] - 1] += numbers[i]
        
    return sorted_list

items = [18,24,12,4,9,44,32,50,36,25]
start = time.time()
print(counting_sort(items))
end = time.time()
print("%.10f" % (end - start))  