if __name__ == "__main__":
  path = input("Enter path of the file: ")

  fp = open(path, "r")

  words = []
  lines = []
  char_count = 0

  for line in fp:
    lines.append(line)
    words.extend(line.split())
  
  for word in words:
    char_count += len(word)
  
  char_count += len(words) - 1
  
  print("Character count:", char_count)
  print("Words count:", len(words))
  print("Lines count:", len(lines))
