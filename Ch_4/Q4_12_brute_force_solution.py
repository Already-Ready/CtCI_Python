import unittest

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def countPathsWithSumFromeNode(startNode, targetSum, currentSum):
    if not startNode:
        return 0
    currentSum += startNode.data
    totalpaths = 0
    if currentSum == targetSum:
        totalpaths += 1
    totalpaths += countPathsWithSumFromeNode(startNode.left, targetSum, currentSum)
    totalpaths += countPathsWithSumFromeNode(startNode.right, targetSum, currentSum)
    return totalpaths

def countPathsWithSum(root, targetSum):
    if not root:
        return 0
    pathsFromRoot = countPathsWithSumFromeNode(root, targetSum, 0)

    pathsOnLeft = countPathsWithSum(root.left, targetSum)
    pathsOnRight = countPathsWithSum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight

node1 = Node(5,Node(3, Node(3), Node(-2)),
               Node(1, Node(2), Node(2)))

print(countPathsWithSum(node1,6))