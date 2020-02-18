import random
import unittest

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.count = 1
        if self.left:
            self.count += self.left.count
        if self.right:
            self.count += self.right.count

    def number_node(self, num):
        if num == 0:
            return self
        if self.left:
            # 현재 노드 왼쪽에 주어진 num보다 많은 자식들이 있는지 확인
            if num - 1 < self.left.count:
                return self.left.number_node(num-1)
            # 현재 노드 왼쪽에 num보다 자식이 적으면 오른쪽 자식들로 진행
            elif self.right:
                return self.right.number_node(num - 1 - self.left.count)
        if self.right:
            return self.right.number_node(num-1)
        return None

    def random_node(self):
        return self.number_node(randint(0, self.count - 1))

fixed_num = False

def randint(start, end):
    if not fixed_num is False:
        return fixed_num
    return random.randint(start, end)

class Test(unittest.TestCase):
    def test_mock_randint(self):
        global fixed_num
        fixed_num = 12
        self.assertEqual(randint(0, 2000), 12)

    def test_get_random_value(self):
        global fixed_num
        tree = Node(11, Node(21, Node(31), Node(32, Node(41), Node(42, None, Node(51)))),
                    Node(22, Node(33), Node(34)))
        fixed_num = 0
        self.assertEqual(tree.random_node().data, 11)
        fixed_num = 4
        self.assertEqual(tree.random_node().data, 41)
        fixed_num = 8
        self.assertEqual(tree.random_node().data, 33)


if __name__ == "__main__":
    unittest.main()

