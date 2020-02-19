import unittest

class Node():
    def __init__(self, name, value, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

class ListDict(dict):
    def __missing__(self, key):
        return []

def paths_sum_nodes(node, target_sum, partial_paths):
    if not node:
        return []
    next_partial_paths = ListDict({target_sum:[[]]})
    for paths_sum, paths in partial_paths.items():
        for path in paths:
            next_partial_paths[paths_sum - node.value] += [path + [node.name]]
    paths = next_partial_paths[0]
    for child in [node.left, node.right]:
        paths += paths_sum_nodes(child, target_sum, next_partial_paths)
    return paths

def paths_with_sum(binary_tree, target_sum):
    partial_paths = ListDict({target_sum: [[]]})
    return paths_sum_nodes(binary_tree, target_sum, partial_paths)


class Test(unittest.TestCase):
    def test_paths_with_sum(self):
        bt = Node("A", 4, Node("B", -2, Node("D", 7), Node("E", 4)),
                  Node("C", 7, Node("F", -1, Node("H", -1), Node("I", 2, Node("K", 1))),
                       Node("G", 0, None, Node("J", -2))))
        self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
        self.assertEqual(paths_with_sum(bt, 2), [["A", "B"], ["B", "E"], ["I"],
                                                 ["F", "I", "K"]])
        self.assertEqual(paths_with_sum(bt, 9), [["A", "B", "D"], ["A", "C", "F", "H"],
                                                 ["C", "F", "I", "K"], ["A", "C", "G", "J"]])


if __name__ == "__main__":
    unittest.main()