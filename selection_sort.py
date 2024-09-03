#moves through the list, assigning new minimums until it finds the actual min
#moves min value to sorted list
#repeats the process with the other values in the list

def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(int(values.pop(index_to_move)))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
        return min_index

numbers = [77, 91, 45, 101, 190, 2, 4, 68]
print(selection_sort(numbers))