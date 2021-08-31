def read_matrix(rows, cols, mat):
  for i in range(rows):
    l = list(
        map(int, input("Enter row " + str(i) + " elements: ").split()))[:cols]
    mat.append(l)


def print_matrix(mat):
  row = len(mat)
  col = len(mat[0])
  for i in range(row):
    for j in range(col):
      print(mat[i][j], end=" ")
    print()


def multiply_matrix(mat1, mat2):
  r1, r2 = len(mat1), len(mat2)
  c1, c2 = len(mat1[0]), len(mat2[0])

  res = []
  for _ in range(r1):
    l = [0 for _ in range(c2)]
    res.append(l)

  for i in range(r1):
    for j in range(c2):
      res[i][j] = 0
      for k in range(c1):
        res[i][j] += mat1[i][k] * mat2[k][j]

  print_matrix(res)


if __name__ == "__main__":
  row1, col1 = list(map(int, input("Enter mat1 rows, cols: ").split()))[:2]
  row2, col2 = list(map(int, input("Enter mat2 rows, cols: ").split()))[:2]

  if col1 == row2:
    mat1 = []
    print("Matrix 1:")
    read_matrix(mat=mat1, rows=row1, cols=col1)
    print("Matrix 2:")
    mat2 = []
    read_matrix(mat=mat2, rows=row2, cols=col2)
    print("Multiplication of two matrices is")
    multiply_matrix(mat1, mat2)
  else:
    print("Matrices are not compactable")
