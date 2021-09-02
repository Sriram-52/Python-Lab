import turtle
j = turtle.Turtle()


for i in range(12):
  if(i % 3 == 0):
      j.color("green")
      j.circle(50)
      j.left(30)
  elif(i % 2 == 0) and (i % 3 != 0):
      j.color("blue")
      j.circle(50)
      j.left(30)
  else:
      j.color("red")
      j.circle(50)
      j.left(30)
turtle.done()
