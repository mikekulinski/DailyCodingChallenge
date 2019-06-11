# class List:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __iter__(self):
#         current = self.head
#         while current is not None:
#             yield current
#             current = current.next

#     def add_node(self, node):
#         if self.length == 0:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.length += 1

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

def find_intersection(list1, list2):
    d_length = abs(len(list1) - len(list2))
    list1_longer = len(list1) > len(list2)

    if list1_longer:
        list1 = list1[d_length:]
    else:
        list2 = list2[d_length:]

    for i in range(len(list1)):
        first = list1[i]
        second = list2[i]

        if first == second:
            return first
    return None


        
    
    



if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [0, 5, 6, 7, 8]
    print(find_intersection(list1, list2))

    