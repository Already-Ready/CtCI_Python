import unittest

class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def balanced(node):
    # 재귀로 트리를 탐색하다가 제일 끝에 None값에 도착했을때, 여기부터 거슬러 올라옴
    if not node:
        return (True, 0)

    (left_balanced, left_depth) = balanced(node.left)
    if not left_balanced:
        return (False, None)

    (right_balanced, right_depth) = balanced(node.right)
    if not right_balanced or (abs(left_depth - right_depth) > 1):
        return (False, None)

    depth = max(left_depth,right_depth) + 1

    return (True, depth)


class Test(unittest.TestCase):
  def test_is_balanced(self):
    self.assertEqual(balanced(Node(Node(),Node())), (True, 2))
    self.assertEqual(balanced(Node(Node(),Node(Node()))), (True, 3))
    self.assertEqual(balanced(Node(Node(),Node(Node(Node())))),
        (False, None))
    self.assertEqual(balanced(Node(Node(Node()),Node(Node(Node())))),(False,None))
    self.assertEqual(balanced(Node(Node(Node()),Node(Node(Node()),Node()))), (True, 4))

if __name__ == "__main__":
  unittest.main()