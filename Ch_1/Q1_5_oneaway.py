

def oneaway(string1,string2):

    # case1. 문자열 길이 차이가 1 이상인 경우
    if abs(len(string1) - len(string2)) > 1:
        return False

    # case2. 문자열 길이 차이가 0 인 경우
    elif abs(len(string1) - len(string2)) == 0:
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
                if count > 1:
                    return False
                else: continue
            else: continue
        return True

    # case3. 문자열 길이 차이가 1인 경우
    else:
        # 둘 중 어느 문자열이 긴것인지 짧은것인지 판단
        if len(string1)>len(string2):
            long = string1
            short = string2
        else:
            long = string2
            short = string1

        shift = 0

        for i in range(len(short)):
            if short[i] != long[i + shift]:
                # 처음부터 연달아 일치하지 않는 문자열이 나오는 경우 혹은 일치하지 않는 첫번째 값을 찾아 쉬프트 된 상태에서 또 다른 일치하지 않는 값을 찾아낸 경우
                if shift or short[i] != long[i+1]:
                    return False
                else:
                    shift = 1
        return True


import unittest


class Test(unittest.TestCase):
    # 테스트 케이스
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_oneaway(self):

        for [string1,string2,boolean] in self.data:
            result = oneaway(string1,string2)
            self.assertEqual(result,boolean)


if __name__ == "__main__":
    unittest.main()