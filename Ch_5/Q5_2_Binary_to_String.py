import unittest

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

class Test(unittest.TestCase):
    def test_binary_to_string(self):
        self.assertEqual(toBinary(0.75), "0.11")
        self.assertEqual(toBinary(0.625), "0.101")
        self.assertEqual(toBinary(0.3), "ERROR : This num is too Long Binary")

if __name__ == "__main__":
  unittest.main()