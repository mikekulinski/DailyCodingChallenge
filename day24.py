class BinaryTreeNode():
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.locked = False
        self.parent = None
        self.set_left(left)
        self.set_right(right)

    def __str__(self):
        return "<Name: " + self.name + ", Locked: " + str(self.locked) + ">"

    def set_left(self, other):
        if type(other) == BinaryTreeNode:
            self.left = other
            other.parent = self
        else:
            self.left = None

    def set_right(self, other):
        if type(other) == BinaryTreeNode:
            self.right = other
            other.parent = self
        else:
            self.right = None

    def is_locked(self):
        return self.locked

    def check_anscestors(self):
        if self.parent == None:
            return self.is_locked()
        else:
            return self.is_locked() or self.parent.check_anscestors()

    def check_descendents(self):
        if not self.left and not self.right:
            return self.is_locked()
        elif self.left:
            return self.is_locked() or self.left.check_descendents()
        elif self.right:
            return self.is_locked() or self.right.check_descendents()
        else:
            return self.is_locked() or self.left.check_descendents() \
                                    or self.right.check_descendents()

    def lock(self):
        if not self.check_anscestors() and not self.check_descendents():
            self.locked = True
            return True
        else:
            return False

    def unlock(self):
        if self.check_anscestors() and self.check_descendents():
            self.locked = False
            return True
        else:
            return False


if __name__ == "__main__":
    tree = BinaryTreeNode("A", 
                BinaryTreeNode("B", 
                    BinaryTreeNode("D"), 
                    BinaryTreeNode("E")), 
                BinaryTreeNode("C", 
                    None,
                    BinaryTreeNode("F",
                        None,
                        BinaryTreeNode('G'))))

    print(tree.lock())
    print(tree)
    print(tree.left.left.lock())
    print(tree.left.left)
    print(tree.lock())
    print(tree)
    print(tree.unlock())
    print(tree)
    print(tree.left.right.lock())
    print(tree.left.right)
