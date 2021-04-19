if __name__ == "__main__":
  n = int(input("Enter range of n: "))
  a = 0
  b = 1
  fib_sum = 0

  while n != 0:
    if a % 2 == 0: fib_sum += a
    c = a + b
    a, b = b, c
    n -= 1
  
  print(fib_sum)