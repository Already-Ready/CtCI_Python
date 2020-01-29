import unittest

def comp(string):
    new = ""

    start = 0

    for i in range(len(string)):
        if string[start] == string[i] and i != len(string)-1:
            pass
        # start지점의 문자열과 순차적으로 비교하는 string의 문자열이 다른 경우
        else:
            # 아직 문자열의 끝까지 오지 않은 경우
            if i != len(string)-1:
                new += string[start]
                new += str(i-start)
                start = i
            # 문자끝까지 왔으며, 입력받은 문자의 마지막도 start지점의 문자와 같은경우
            elif i == len(string)-1 and string[i] == string[start]:
                new += string[start]
                new += str(i-start+1)
            # 문자끝까지 왔으며, 입력받은 문자의 마지막이 바뀌어서 start지점의 문자와 다른경우
            # 예를들어 'aabcccccaaab' 를 입력받는 경우
            elif i == len(string)-1 and string[i] != string[start]:
                start = i
                new += string[start]
                new += str(1)

    if len(new) > len(string):
        return string
    else:
        return new


class Test(unittest.TestCase):
    # 테스트 케이스
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_comp(self):
        for [string,expected] in self.data:
            result = comp(string)
            self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()


