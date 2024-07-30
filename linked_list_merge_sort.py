from linked_list import LinkedList

def merge_sort(linked_list):
    """
    sorts a linked list in ascending order
    recursively divide the linked list into sublists containing a single node
    repeatedly merge the sublists to produce sorted sublists until one remains

    returns a sorted linked list

    runs in O(k log n)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    #if the list is only one term or if it's empty, returns the same list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    divide the unsorted list at midpoint into sublists (sub linked-lists)
    """

    #if linked list is none or empty, assign the terms to left

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)
        #actually splitting the list

        #node at midpoint of list; size always returns value greater than index

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

    #assign node after midpoint as the new head of the other list

    #summary: start with a list and find midpoint
    #node after midpoint is assigned as the new head
    #connection between the two halves is severed
    #results in two distinct linked lists

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    New linked list with nodes where the data is sorted
    runs in O(n) time
    """

    #Create a new linked list that contains nodes from
    #merging left and right
    merged = LinkedList()

    #"fake head", can later assign the first sorted node as head
    #fake is discarded
    merged.add(0)

    #set current to the head of the linked list
    current = merged.head

    #get head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right until tail node of either is reached
    #traversing the list
    while left_head or right_head:
        #if head node of left is None, we're past tail
        #add the node from the right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to false
            right_head = right_head.next_node
            #if the head node of right is none, past tail
            #add tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            #call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            #not at either tail node
            #obtain node data to compare
            left_data = left_head.data
            right_data = right_head.data
            # if left data is less than right, set current to left node
            if left_data < right_data:
                #move left head to next node
                current.next_node = left_head
                left_head = left_head.next_node
                #sets as the next node in the sorted list
            #if data on left is greater, set current to right node
            else:
                #assign right node to be next in the list
                current.next_node = right_head
                #move right head to next node
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node

    #discard fake head
    #set first merged node as the head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
merged_linked_list = merge_sort(l)
print(merged_linked_list)









