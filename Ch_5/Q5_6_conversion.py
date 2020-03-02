
# 두 수의 비트값을 하나씩 비교해 나가는 방법
def flip(num1, num2):
    count = 0

    while (num1 != 0) or (num2 != 0):
        if (num1 & 1) != (num2 & 1):
            count += 1
        num1 >>= 1
        num2 >>= 1

    return count

# 두 수를 XOR 연산을 한 후 그 값이 1인 비트를 찾는 방법
# --> XOR 연산에서 1이 나왔다는것은 두 비트의 값이 달랐다는 뜻이기 때문이다.
def flip_XOR(num1, num2):
    count = 0
    com = (num1 ^ num2)
    while com != 0:
        if (com & 1) == 1:
            count += 1
        com >>= 1

    return count

print(flip(29,15))
print(flip_XOR(29,15))