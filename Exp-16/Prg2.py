def knapsack(val, wt, size):
  n = len(val)

  # build n * size matrix with 0's
  k = [[0 for _ in range(size + 1)] for _ in range(n + 1)]

  for i in range(n + 1):
    for w in range(size + 1):
      if i == 0 or w == 0:
        k[i][w] = 0
      elif wt[i-1] <= w:
        k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
      else:
        k[i][w] = k[i-1][w]

  return k[n][size]


if __name__ == "__main__":
  val = list(map(int, input("Enter values: ").split()))
  wt = list(map(int, input("Enter weights: ").split()))
  size = int(input("Enter bag size: "))

  if len(val) > len(wt):
    val = val[:len(wt)]
  elif len(val) < len(wt):
    wt = wt[:len(val)]

  print("Maxium profit is", knapsack(val=val, wt=wt, size=size))
