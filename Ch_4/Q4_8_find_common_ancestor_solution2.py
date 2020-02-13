import unittest

# 1번 solution과 다르게 hash table을 사용하지 않는 해법

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

def depth(node):
    depth = 0
    while node != None:
        node = node.parent
        depth += 1
    return depth

def goUpBy(node, delta):
    while (delta > 0 and node != None):
        node = node.parent
        delta -= 1
    return node

def find_ancestor(node1, node2):
    delta = depth(node1) - depth(node2)
    # node2가 더 깊이 있는 경우
    if delta < 0:
        first = node1
        second = node2
    # node1이 더 깊이 있는 경우
    else:
        first = node2
        second = node1
    # 더 깊이 있는 노드를 얕은 노드와 같은 높이로 끌여올려준다.
    second = goUpBy(second, abs(delta))

    # 같은 높이의 두 노드에서 parent를 찾아 같아지는 순간에 빠져나오자.
    while (first != second and first != None and second != None):
        first = first.parent
        second = second.parent

    return first

class Test(unittest.TestCase):
  def test_find_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(find_ancestor(node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(find_ancestor(node1, node2).data, node3.data)

if __name__ == "__main__":
  unittest.main()
