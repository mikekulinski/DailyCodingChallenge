# class List:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self, value):
#         node = Node(value)

#         if self.head == None and self.tail == None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.length += 1

#     def pop(self):
#         self.head = self.head.next

#         if (self.length == 1):
#             self.tail = None

#         self.length -= 1

#     def printList(self):
#         print("[")
#         current = self.head
#         while current != None:
#             print(current.value)
#             current = current.next
#         print("]")

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


def largest_non_adj_sum(array):
    # Array where each index contains highest 
    # non-adj sum including that value
    best = []

    for i in range(len(array)):
        if (i < 2):
            best.append(array[i])
        else:
            best.append(max(best[:-1]) + array[i])

            if (len(best) > 4):
                best = best[1:]

    return max(best)

def test1():
    print("Test 1:")
    result = largest_non_adj_sum([2, 4, 6, 2, 5, 1])
    assert(result == 13)
    print("PASSED")

def test2():
    print("Test 2:")
    result = largest_non_adj_sum([5, 1, 1, 5])
    assert(result == 10)
    print("PASSED")

if __name__ == "__main__":
    test1()
    test2()