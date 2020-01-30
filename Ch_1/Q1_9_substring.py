import unittest

def substring(string1, string2):
    return string1.find(string2) != -1
    # 일치하는 부분을 찾았다면 find는 인덱스값을 리턴하므로 결과적으로 True를 반환할것

def rotation(string1, string2):
    length = len(string1)
    if length == len(string2) and length > 0:
        ## xy를 회전하여 yx로 나타낸 문자열은 언제나 xyxy의 부분 문자열이라는 사실을 이용
        string11 = string1 + string1
        return substring(string11,string2)
    else:
        return False


class Test(unittest.TestCase):
    # 테스트 케이스
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [string1, string2, expected] in self.data:
            result = rotation(string1, string2)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()