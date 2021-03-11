import time

# def merge(items1, items2, mergedList=[]):
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n log(n)) n being the sum of items1 and items2 Why and under what conditions? 
    Comparing the first value of items2 to the values in item1
    TODO: Memory usage: O(1) Why and under what conditions?
    No new variables were created"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    """
    base case is when both lists are empty
    if arr1.count == 0 and arr2.count == 0
        return mergedList:
    else:
        if arr1[0] is greater than arr2[0]
            mergedList.append(arr2[0])
            arr2.pop(0)
        elif arr1[0] is less than arr2[0]
            mergedList.append(arr1[0])
            arr1.pop(0)
        return function with new parameters
    """

    # if len(items1) == 0 and len(items2) == 0:
    #     return mergedList
    # elif len(items1) == 0 and len(items2) > 0:
    #     mergedList.extend(items2)
    #     return mergedList
    # elif len(items2) == 0 and len(items1) > 0:
    #     mergedList.extend(items1)
    #     return mergedList
    # else:
    #     if items1[0] > items2[0]:
    #         mergedList.append(items2[0])
    #         items2.pop(0)
    #     elif items1[0] < items2[0]:
    #         mergedList.append(items1[0])
    #         items1.pop(0)
    #     else:
    #         mergedList.append(items1[0])
    #         mergedList.append(items2[0])
    #         items1.pop(0)
    #         items2.pop(0)
    #     return merge(items1, items2, mergedList)

    """
    base case is when list 2 is empty
    if length of list 2 is 0
        return list 1
    else
        for index in range(len(list 1)-1)
            if index of list 1 is greater than or equal to index 0 of list 2
                prepend index 0 of list 2 to list 1
                return merge function with list 1 and list 2[1:]
    """
    
    if len(items2) == 0:
        return items1
    for index in range(len(items1) - 1):
        if items1[index] >= items2[0]:
            items1.insert(index, items2[0])
            return merge(items1, items2[1:])
    if len(items1) > len(items2):
        items1.extend(items2)
        return items1


items1 = [1,5,7,10,18]
items2 = [2,5,6,8]
start = time.time()
print(merge(items1, items2))
end = time.time()
print("%.10f" % (end - start))