from merge_sort import merge_sort

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    #sets the index values of the first and last terms to identify them

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [65, 22, 37, 89, 200]

new_list = merge_sort(numbers)
print(new_list)
result = binary_search(new_list, 89)
print(result)
verify(result)

#verify(result)

#result = binary_search(numbers,37)
#verify(result)
