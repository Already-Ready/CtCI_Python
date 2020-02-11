import unittest

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validate_node(node, left_bound, right_bound):
    # 리프 노드에서 더 넘어가면 True를 반환한다.
    if not node:
        return True
    # 차일드 노드가 왼쪽 트리에 있을 경우
    # --> 차일드 노드가 -inf <= 차일드 노드 값 < 차일드 노드.parent 를 만족하는가?
    # 차일드 노드가 오른쪽 트리에 있을 경우
    # --> 차일드 노드가 차일드노드.parent <= 차일드 노드 값 < +inf 를 만족하는가?
    # 리프 노드는 True를 반환하므로 하나라도 위의 조건에 맞지 않으면 False 를 최종적으로 반환
    return (node.data >= left_bound and node.data < right_bound) and \
            validate_node(node.left, left_bound, node.data) and \
            validate_node(node.right, node.data, right_bound)

def validate_tree(bst):
    return validate_node(bst, -float('inf'), float('inf'))

class Test(unittest.TestCase):
  def test_validate_tree(self):
    self.assertEqual(validate_tree(Node(3,Node(1),Node(8))), True)
    tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))
    self.assertEqual(validate_tree(tree1), True)
    tree2 = Node(7,Node(3,Node(1),Node(8)),Node(9,Node(8),Node(11)))
    self.assertEqual(validate_tree(tree2), False)

if __name__ == "__main__":
  unittest.main()