if __name__ == "__main__":
  path = input("Enter path of the file: ")
  
  fp = open(path, "r")

  for line in fp:
    print(line[::-1])