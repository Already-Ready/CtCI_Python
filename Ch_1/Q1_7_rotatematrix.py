import unittest

def rotation(li):
    N = len(li[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = li[i][j]
            li[i][j] = li[N - 1 - j][i]
            li[N - 1 - j][i] = li[N - 1 - i][N - 1 - j]
            li[N - 1 - i][N - 1 - j] = li[j][N - 1 - i]
            li[j][N - 1 - i] = temp
    return li


class Test(unittest.TestCase):
    # 테스트 케이스
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_comp(self):
        for [li,expected] in self.data:
            result = rotation(li)
            self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()