if __name__ == "__main__":
  n = int(input("Enter range of n: "))
  a = 0
  b = 1

  while n != 0:
    print(a)
    c = a + b
    a, b = b, c
    n -= 1