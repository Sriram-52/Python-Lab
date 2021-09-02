import turtle
s = turtle.Turtle()


s.speed(0)


def sq():
  for _ in range(4):
    s.forward(50)
    s.left(90)


for _ in range(36):
  s.left(10)
  sq()

turtle.done()
