def reverse_list(l):
  rev = []
  for i in range(1, len(l) + 1):
    ele = l[-i]
    rev.append(ele)
  return rev


if __name__ == "__main__":
  l = list(map(int, input("Enter your list: ").split()))
  print("Reversed list is", reverse_list(l))
