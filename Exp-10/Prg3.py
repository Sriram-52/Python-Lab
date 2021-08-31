def gcd(a, b):
  return a if(b == 0) else gcd(b, a % b)


def lcm(a, b):
  return (a * b) // gcd(a, b)


if __name__ == "__main__":
  a, b = list(map(int, input("Enter a,b: ").split()))[:2]
  print("GCD of", a, "and", b, "is", gcd(a, b))
  print("LCM of", a, "and", b, "is", lcm(a, b))
