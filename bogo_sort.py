import random

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

numbers = [77, 91, 45, 101, 190, 2, 4, 68]

print(bogo_sort(numbers))



#luck --> randomizes the list to see if it is sorted
#each time it goes through, it could have all but one value right
#or all values wrong


