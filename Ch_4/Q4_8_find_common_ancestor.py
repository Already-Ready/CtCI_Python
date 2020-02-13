import unittest

class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def find_ancestor(node1, node2):
    hash1 = {}
    hash2 = {}
    first = node1
    second = node2
    while first or second:
        if first:
            if first in hash2:
                return first
            else:
                hash1[first] = True
                first = first.parent
        if second:
            if second in hash1:
                return second
            else:
                hash2[second] = True
                second = second.parent

    return None

class Test(unittest.TestCase):
  def test_find_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(find_ancestor(node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(find_ancestor(node1, node2), node3)

if __name__ == "__main__":
  unittest.main()

