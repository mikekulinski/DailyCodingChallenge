class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def kth_last_element(node, k):
    current = node
    while k >= 0:
        current = current.next
        k -= 1

    kth = node
    while current != None:
        current = current.next
        kth = kth.next 
    
    return kth.value


if __name__ == "__main__":
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(8)
    n.next.next.next = Node(3)
    n.next.next.next.next = Node(7)
    n.next.next.next.next.next = Node(0)
    n.next.next.next.next.next.next = Node(4)
    print(kth_last_element(n, 2))
