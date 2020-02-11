import unittest

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

# 중위 후속자란?
# --> 중위 순회를 진행할 때 다음에 탐색할 노드
# --> 중위 순회란?
    # --> 트리를 탐색할때, 왼쪽 하위 노드 --> 현재 노드 --> 오른쪽 하위 노드 순으로 탐색하는 방법

def successor(node):

    if not node:
        return None

    if node.right:
        child = node.right
        while child.left:
            child = child.left
        return child

    else:
        present_node = node
        parent_node = present_node.parent
        while (parent_node != None) and (parent_node.left != present_node):
            present_node = parent_node
            parent_node = parent_node.parent
        return parent_node


class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)
    test_tree1 = Node(22,Node(11,Node(1),Node(15))).left.right
    # test_tree1에서 Node(15)의 중위 순회자는 22이다.
    # --> 22의 왼쪽을 모두 순회한것이 15에서 끝이 나므로 다음 순회는 22이기 때문이다.
    self.assertEqual(successor(test_tree1).data,22)

if __name__ == "__main__":
  unittest.main()