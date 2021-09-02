class Stack:
  def __init__(self):
    self.__s = []

  def push(self, x):
    self.__s.append(x)

  def pop(self):
    return self.__s.pop()

  def display(self):
    print("Stack from bottom to top: ")
    print("->".join(list(map(str, self.__s))))


if __name__ == "__main__":
  stack = Stack()
  while True:
    print("****MENU****")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
      n = int(input("Enter number to push: "))
      stack.push(n)
    elif ch == 2:
      print("Popped", stack.pop())
    elif ch == 3:
      stack.display()
    elif ch == 4:
      break
    else:
      print("Please choose the correct options")
