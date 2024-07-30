def linear_search(list, target):
    for i, element in enumerate(list):
        print("position:", i, "value:", element)
        if element == target:
            return i
    return None

def verify_search(index):
    if index is not None:
        print("Value found in list at position", index)
    else:
        print("Value not in list")

set = [12, 14, 22, 7, 30]

result = linear_search(set, 30)
verify_search(result)


