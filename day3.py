class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right



def serialize(node):
  output = "Node('" + node.val + "'"
  if (node.left or node.right):
    output += ", "

  if (node.left):
    output += serialize(node.left)
    if (node.right):
      output += ", "
  if (node.right):
    if (not node.left):
      output += "None, "
    output += serialize(node.right)

  output += ")"
  return output

def deserialize(string):
  node = eval(string)

  return node

node = Node('root', Node('left', None, Node('left.right')), Node('right'))
newNode = serialize(node)
deserialize(newNode)
assert deserialize(serialize(node)).left.right.val == 'left.right'