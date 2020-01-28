import unittest
from collections import Counter


def permutation(string1,string2):
    counter = Counter()

    for s1 in string1:
        # counter 로 처음 입력받은 문자열의 딕셔너리를 만들어준다.
        counter[s1] += 1

    for s2 in string2:
        # Counter 에서 키로 존재하지 않는 값을 찾으면 0 을 출력한다. 이 점을 활용
        if counter[s2] == 0:
            return False
        else:
            counter[s2] -= 1
    # 두번째 문자열 전부 탐색을 했다면 True 반환
    return True

class Test(unittest.TestCase):

    # True를 반환할 테스트 케이스
    test_T = [('abcd','bacd'),
              ('a1b2c3','abc123')]
    # False를 반환할 테스트 케이스
    test_F = [('abcd','aabcd'),
              ('test_t','test_f')]

    def test_permutation(self):
        for t in self.test_T:
            checker = permutation(*t)
            self.assertTrue(checker)
        for t in self.test_F:
            checker = permutation(*t)
            self.assertFalse(checker)

if __name__ == "__main__":
    unittest.main()

