def isprime(n):
  if n <= 1: return False
  
  if n <= 3: return True

  if n % 2 == 0 or n % 3 == 0: return False

  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0: return False

    i += 6

  return True


prime_sum = 0
for i in range(0, 20000000):
  if isprime(i):
    print("Adding", i)
    prime_sum += i

print(prime_sum)
  
