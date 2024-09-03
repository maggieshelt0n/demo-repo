def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists created in previous step
    Combine: merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    """
    Right list shorter than left list
    """

    while i < len(left):
        l.append(left[i])
        i+=1

    """
    Left list shorter than right list
    """

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

"""
alist = [54, 62, 93, 76, 45, 22, 1, 100, 81, 34]
l = merge_sort(alist)
print(l)
"""

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

"""
iterative solution with for loop
"""

alist = [91, 25, 34, 76, 99, 26, 61, 11, 2]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
print(l)

"""
Checks whether the original list is sorted and finds that it is not
Moves to sorted list to verify it

Time complexity:
- split function splits the list at the midpoint --> called as many times as needed
- overall, runs in logarithmic time --> O(k log n) time
- much more expensive because of slicing operation (lines 27, 28)
- merge step has to make an n number of merge operations
- overall, runs in linear time but you have to multiply the first two

OVERALL SORTING PROCESS = O(kn log n) time

Space complexity:
- not every sublist is created simultaneously
- delete old split sublists as you go
- circles back to old n/2 sublist
- only the last step matters, where the two lists are combined
- at most, additional space required at a given time is n
- linear space complexity
"""