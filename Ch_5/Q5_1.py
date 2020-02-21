import unittest

def mask(bit, start, end):
    mask_start = (-1 << start+1)
    mask_end = (1 << end) - 1
    mask = mask_start | mask_end

    bit = bit & mask
    return bit

def insert(bit1, bit2, start, end):
    bit1 = mask(bit1, start, end)
    bit2 = bit2 << end
    return bin(bit1 | bit2)

class Test(unittest.TestCase):
  def test_insertion(self):
    self.assertEqual(insert(27, 4, 3, 1), bin(0b11001))
    self.assertEqual(insert(99,7,4,2), bin(0b1111111))

if __name__ == "__main__":
  unittest.main()


# print(bin(99))
# print(bin(7))
# print(insert(99,7,4,2))

