import unittest

class Node():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def equal_trees(node1, node2):
    # node1에서의 파생은 끊겼을때 --> 1. node2가 있다면 False를 내야됨 2. node2도 비었다면 True 를 냄(둘다 없으므로)
    if not node1:
        return not node2
    # node1의 파생은 있는데 node2의 파생은 없다? --> 두 트리의 모형이 다르다
    if not node2:
        return False
    # 두 노드의 데이터가 다르면 같은 노드를 찾을때까지 False
    if node1.data != node2.data:
        return False
    return equal_trees(node1.left, node2.left) and equal_trees(node1.right, node2.right)

def tree_generator(node):
    if not node: return None
    yield node
    for child in tree_generator(node.left):
        yield child
    for child in tree_generator(node.right):
        yield child


def compare_trees(node1,node2):
    for node in tree_generator(node1):
        if equal_trees(node, node2):
            return True
    return False


class Test(unittest.TestCase):
    def test_subtrees(self):
        tree1 = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7, Node(9)), Node(1)))
        tree2 = Node(8, Node(7), Node(1))
        self.assertEqual(compare_trees(tree1, tree2), False)
        tree3 = Node(8, Node(7, Node(9)), Node(1))
        self.assertEqual(compare_trees(tree1, tree3), True)


if __name__ == "__main__":
    unittest.main()
