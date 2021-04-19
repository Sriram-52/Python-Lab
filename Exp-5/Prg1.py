if __name__ == "__main__":
  string = input("Enter any string: ")
  dict = {}

  for char in string:
    if char in dict.keys():
      dict[char] += 1
    else:
      dict[char] = 1
  
  print(dict)