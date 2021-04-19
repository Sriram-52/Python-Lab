if __name__ == "__main__":
  birthday_dict = {'Sriram': '06-12-2000', 'Roshini': '02-06-2001'}

  names = input().split()

  for name in names:
    if name in birthday_dict.keys(): 
      print(" ".join([name + "'s", "birthday is", birthday_dict[name]]))
    else:
      print(" ".join([name, "do not exist in database"]))
