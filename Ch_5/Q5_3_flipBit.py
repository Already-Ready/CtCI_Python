import numpy


def bitLongestOne(num):
    bi = bin(num)[2:]
    if "0" not in bi:
        return len(bi)

    currentLength = 0
    previousLength = 0
    maxLength = 1

    while (num != 0):
        print(maxLength)
        if (num & 1) == 1: # --> 가장 오른쪽 비트가 1인 경우
            currentLength += 1
        elif (num & 1) == 0: # --> 가장 오른쪽 비트가 0 인 경우
            if (num & 2) == 0: # --> 0이 연달아서 두개 나오는 경우
                previousLength = 0
            else:
                previousLength = currentLength
            currentLength = 0

        maxLength = max(previousLength + currentLength + 1, maxLength)
        num = numpy.right_shift(num,1)

    return maxLength


print(bitLongestOne(1775))

