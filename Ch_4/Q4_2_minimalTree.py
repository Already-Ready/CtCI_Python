from math import floor

class Node():

    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.val) + " R:" + str(self.right) + ')'


def minimalTree(array, start, end):
    # 오름차순의 array를 입력받을것
    if start > end:
        return ""
    mid = floor((start + end) / 2)
    root = Node(array[mid])
    root.left = minimalTree(array, start, mid-1)
    root.right = minimalTree(array, mid+1, end)
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(minimalTree(testArray,0,len(testArray)-1))
