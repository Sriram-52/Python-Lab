from sys import argv

if __name__ == "__main__":
  if len(argv) == 3:
    a, b = argv[1], argv[2]
    if a.isdigit() and b.isdigit():
      print("Sum of {0} and {1}".format(a, b), "is", int(a) + int(b))
    else:
      print("Please give numbers only")
  else:
    print("Format Prg.py num1 num2")
