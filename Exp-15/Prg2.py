import unittest


def reverse_string(str):
  return str[::-1]


class TestFactorial(unittest.TestCase):
  def test_fact(self):
    res = reverse_string("Hello World")
    self.assertEqual(res, "dlroW olleH")


if __name__ == '__main__':
  unittest.main()
