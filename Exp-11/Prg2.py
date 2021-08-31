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


def add_matrix(mat1, mat2):
  mat3 = mat1.copy()
  row = len(mat1)
  col = len(mat1[0])

  for i in range(row):
    for j in range(col):
      mat3[i][j] = mat1[i][j] + mat2[i][j]

  print_matrix(mat3)


if __name__ == "__main__":
  row1, col1 = list(map(int, input("Enter mat1 rows, cols: ").split()))[:2]
  row2, col2 = list(map(int, input("Enter mat2 rows, cols: ").split()))[:2]

  if(row1 == row2 and col1 == col2):
    mat1 = []
    print("Matrix 1:")
    read_matrix(mat=mat1, rows=row1, cols=col1)
    print("Matrix 2:")
    mat2 = []
    read_matrix(mat=mat2, rows=row2, cols=col2)
    print("The sum of matrices is")
    add_matrix(mat1, mat2)
  else:
    print("Rows and cols should be of same length")
