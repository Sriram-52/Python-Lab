class Ball:
   def __init__(self, x, y, r):
       self.x = x
       self.y = y
       self.r = r


if __name__ == "__main__":
    b1 = Ball(0, 0, 5)
    b2 = Ball(1, 0, 5)

    print(b1.x, b1.y, b1.r)