import unittest


def even_numbers(l):
  if(l != list(l)):
      return False
  for i in l:
      if(i % 2 != 0):
          return False
  return True


class TestEven(unittest.TestCase):
  def test_fact(self):
      res = even_numbers([2, 4, 6, 8])
      self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
