def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify_search(index):
    if index is not None:
        print("value found at position", index)
    else:
        print("value not found")