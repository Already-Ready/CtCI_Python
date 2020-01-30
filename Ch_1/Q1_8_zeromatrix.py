import unittest

def matrix(li):
    n = len(li)
    if n == 0:
        return li
    m = len(li[0])


    zero_rows = []
    zero_cols = []

    for x in range(n):
        for y in range(m):
            if li[x][y] == 0:
                zero_rows.append(x)
                zero_cols.append(y)

    for x in zero_rows:
        for y in range(m):
            li[x][y] = 0

    for y in zero_cols:
        for x in range(n):
            li[x][y] = 0

    return li

class Test(unittest.TestCase):
    # 테스트 케이스
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_comp(self):
        for [li,expected] in self.data:
            result = matrix(li)
            self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()
