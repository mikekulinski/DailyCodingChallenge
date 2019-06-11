class Log:
    def __init__(self, max_length):
        self.head = None
        self.tail = None
        self.length = 0
        self.max_length = max_length

    def record(self, order_id):
        order = Order(order_id)
        if self.length == self.max_length:
            self.pop()
        
        self.push(order)

    def push(self, order):
        if self.head:
            self.head.prev = order
        else:
            self.tail = order
        order.next = self.head
        self.head = order 
        self.length += 1

    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def get_last(self, ith_last):
        current = self.tail
        for i in range(ith_last):
            current = current.prev
        return current.order_id

    def printLog(self):
        print("[")

        current = self.head
        for i in range(self.length):
            print(str(current.order_id) + ",")
            current = current.next

        print("]")


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.next = None
        self.prev = None

    
if __name__ == "__main__":
    log = Log(5)
    for i in range(7):
        log.record(i)

    print(log.get_last(3))