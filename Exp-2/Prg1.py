from math import sqrt

if __name__ == "__main__":
  x1,y1 = list(map(int, input().split()))
  x2,y2 = list(map(int, input().split()))
  d2 = (x1-x2)**2 + (y1-y2)**2
  print("Distance between ({0}, {1}) and ({2}, {3}) is ".format(x1,y1,x2,y2), sqrt(d2))