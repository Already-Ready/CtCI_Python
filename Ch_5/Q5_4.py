# getNext --> 주어진 num 보다 크고 1의 비트 개수가 같은 첫번째 숫자
# getPrev --> 주어진 num 보다 작고 1의 비트 개수가 같은 첫번째 숫자

def getNext(num):
    originLength = len(bin(num))-2
    shiftedNum = num
    zeroCount = 0
    oneCount = 0

    while (((shiftedNum & 1) == 0) and (shiftedNum != 0)):
        zeroCount += 1
        shiftedNum >>= 1

    while ((shiftedNum & 1) == 1):
        oneCount += 1
        shiftedNum >>= 1

    if (zeroCount + oneCount == 32) or (zeroCount + oneCount == 0):
        return -1

    changedPosition = zeroCount + oneCount


    num |= (1 << changedPosition) # 1로 바꿔줘야되는 위치만 1로 바꿔준다
    num &= (((1 << changedPosition) - 1) << changedPosition) # changedPosition 이하 위치를 모두 0으로 바꾼다.
    num |= ((1 << (oneCount-1)) - 1)

    return num

def getPrev(num):
    originLength = len(bin(num))-2
    shiftedNum = num
    zeroCount = 0
    oneCount = 0

    while ((shiftedNum & 1) == 1):
        oneCount += 1
        shiftedNum >>= 1

    while (((shiftedNum & 1) == 0) and (shiftedNum != 0)):
        zeroCount += 1
        shiftedNum >>= 1

    changedPosition = zeroCount + oneCount

    num &= (((1 << (originLength - (changedPosition+1))) - 1) << (changedPosition+1))
    num |= (((1 << oneCount+1) - 1) << (zeroCount-1))
    return num

print(bin(13948))
print(bin(getNext(13948)))
print(bin(getPrev(13948)))
print("-"*20)
print(bin(8))
print(getNext(8))
print(getPrev(8))
