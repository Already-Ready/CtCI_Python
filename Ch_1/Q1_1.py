import unittest

# 문자열을 입력받고 True,False 를 반환하는 함수
def unique(string):
    #ASCII 문자열 (총 128개의 문자열) 기준

    # 문자열에 ASCII 테이블에 없는 값이 존재하는지 판단
    if len(set(string)) > 128:
        return False

    unique_list = [False for _ in range(128)]

    for s in string:
        ascii_index = ord(s)

        # 만약 해당 문자열에 해당하는 인덱스값이 True 라면 겹치는 값이 존재한다는 뜻이므로 False 반환
        if unique_list[ascii_index]:
            return False
        # 처음 등장한 문자열의 인덱스값을 True로 바꿔준다.
        unique_list[ascii_index] = True

    # 문자열을 전부 확인했는데 겹치는 값이 없다는 뜻이므로 --> True 반환
    return True

# unittest 작성

class Test(unittest.TestCase):

    # True를 반환할 테스트 케이스
    test_T = [('abcd'),('123qwer'),('')]
    # False를 반환할 테스트 케이스
    test_F = [('2abcd2'),('ab bc1 2cd3 (4)')]

    def test_unique(self):
        # True 반환 체크
        for t in self.test_T:
            checker = unique(t)
            # assertTure를 통해 unique 함수에서 받은 값이 True 인지 확인
            self.assertTrue(checker)

        # Flase 반환 체크
        for f in self.test_F:
            checker = unique(f)
            self.assertFalse(checker)

if __name__ == "__main__":
    unittest.main()





