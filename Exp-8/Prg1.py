from math import sqrt

class Ball:
   def __init__(self, x, y, r):
       self.x = x
       self.y = y
       self.r = r


def ball_collide(b1, b2):
    distance_between_centers = sqrt((b1.x - b2.x) ** 2 - (b1.y - b2.y) ** 2)
    sum_of_radii = b1.r + b2.r

    if distance_between_centers <= sum_of_radii:
        return True
    return False

if __name__ == "__main__":
    x1, y1 = list(map(int, input("Enter ball-1 coordinates: ").split()))
    x2, y2 = list(map(int, input("Enter ball-2 coordinates: ").split()))
    r1, r2 = list(map(int, input("Enter r1 and r2: ").split()))
    b1 = Ball(x1, y1, r1)
    b2 = Ball(x2, y2, r2)

    if(ball_collide(b1, b2)):
        print("The balls will collide")
    else:
        print("The balls will not collide")