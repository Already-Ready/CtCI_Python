
def toBinary(num):
    if num <= 0 or num >= 1:
        return "ERROR"

    binaryString = "0."

    while num > 0:

        if len(binaryString) >= 32:
            return "ERROR : This num is too Long Binary"

        double = num * 2

        if double >= 1:
            binaryString += "1"
            num = double - 1
        else:
            binaryString += "0"
            num = double

    return binaryString

print(toBinary(0.625))