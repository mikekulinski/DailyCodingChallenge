class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def num_unival(self):
        """
        Recursively searches the tree for univality and the number of unival subtrees
        Returns ((bool) if_unival, (int) number of unival subtrees)
        """
        # If has both children
        if (self.left and self.right):
            left_results = self.left.num_unival()
            right_results = self.right.num_unival()
            left_and_right = left_results[0] and right_results[0]
            same_as_both = self.value == self.left.value and self.value == self.right.value

            total = left_results[1] + right_results[1]
            if (left_and_right and same_as_both):
                return (True, total + 1)
            else:
                return (False, total)
        # If has just left child
        elif (self.left):
            left_results = self.left.num_unival()
            if (left_results[0] and self.value == self.left.value):
                return (True, left_results[1] + 1)
            else:
                return (False, left_results[1])
        # If has just right child
        elif (self.right):
            right_results = self.right.num_unival()
            if (right_results[0] and self.value == self.right.value):
                return (True, right_results[1] + 1)
            else:
                return (False, right_results[1])
        # If has no children
        else:
            return (True, 1)


def test1():
    print("Test 1:")
    tree = Tree(0, Tree(1), Tree(0, Tree(1, Tree(1), Tree(1)), Tree(0)))
    results = tree.num_unival()
    assert(results[0] == False and results[1] == 5)
    print("Passed")

def test2():
    print("Test 2:")
    tree = Tree(0, Tree(0), Tree(0, Tree(0, Tree(0), Tree(0)), Tree(0)))

    results = tree.num_unival()
    assert(results[0] == True and results[1] == 7)
    print("Passed")
    


if __name__ == "__main__":
    test1()
    test2()