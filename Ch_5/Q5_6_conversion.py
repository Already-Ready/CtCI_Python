
def flip(num1, num2):
    count = 0

    while (num1 != 0) or (num2 != 0):
        if (num1 & 1) != (num2 & 1):
            count += 1
        num1 >>= 1
        num2 >>= 1

    return count


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