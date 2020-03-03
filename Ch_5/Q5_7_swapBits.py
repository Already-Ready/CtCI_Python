import unittest

def swapOddEvenBits(num):
   return (((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1))

# hexademical(16진수)에서 a 는 2진수로 1010
# 5는 2진수로 0101 로 나타난다는 점을 이용한것.


class Test(unittest.TestCase):
  def test_swap_odd_even_bits(self):
    self.assertEqual(swapOddEvenBits(42), 21)
    self.assertEqual(swapOddEvenBits(21), 42)
    self.assertEqual(swapOddEvenBits(43), 23)
    self.assertEqual(swapOddEvenBits(511), 767)
    self.assertEqual(swapOddEvenBits(1023), 1023)

if __name__ == "__main__":
  unittest.main()
