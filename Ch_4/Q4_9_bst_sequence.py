import unittest

class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bst_sequence(partial, subtrees):
    if not subtrees:
        return [partial]

    sequence = []

    for index, node in enumerate(subtrees):
        # 현재 노드를 포함해서 거쳐온 노드들을 저장해줘야한다.
        next_partial = partial + [node.data]
        # 다음에 들어갈 노드에서 다음으로 나올 수 있는 노드들을 나타내준다.
        next_subtrees = subtrees[:index] + subtrees[index+1:]
        if node.left:
           next_subtrees.append(node.left)
        if node.right:
            next_subtrees.append(node.right)
        sequence += bst_sequence(next_partial, next_subtrees)

    return sequence

def bst_sequence_startNode(node):
    return bst_sequence([], [node])



class Test(unittest.TestCase):
    def test_bst_sequences(self):
        self.assertEqual(bst_sequence_startNode(Node(7, Node(4, Node(5)), Node(9))), [
            [7, 4, 9, 5],
            [7, 4, 5, 9],
            [7, 9, 4, 5]])
        self.assertEqual(bst_sequence_startNode(Node(7, Node(4, Node(5), Node(6)), Node(9))), [
            [7, 4, 9, 5, 6],
            [7, 4, 9, 6, 5],
            [7, 4, 5, 9, 6],
            [7, 4, 5, 6, 9],
            [7, 4, 6, 9, 5],
            [7, 4, 6, 5, 9],
            [7, 9, 4, 5, 6],
            [7, 9, 4, 6, 5]])


if __name__ == "__main__":
    unittest.main()