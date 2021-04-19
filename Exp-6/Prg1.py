if __name__ == "__main__":
  list1 = list(map(int, input("Enter list1: ").split()))
  list2 = list(map(int, input("Enter list2: ").split()))

  z = zip(list1, list2)

  print(dict(z))