if __name__ == "__main__":
  path = input("Enter path of the file: ")

  fp = open(path, 'r')

  count = {}

  for line in fp:
    for char in line:
      if char in count.keys(): count[char] += 1
      else: count[char] = 1
  
  print(count)

  print("Checking the type of file...")

  ext = path.split("\\").pop().split(".").pop()

  if ext == "py": print("It's a python file")
  elif ext == "txt": print("It's a text file")
  else: print("It's extension is ", ext)