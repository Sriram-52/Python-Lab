def print_matrix(l, row_len, col_len):
  print("The matrix is")
  for i in range(row_len):
    for j in range(col_len):
      print(l[i][j], end=" ")
    print()


if __name__ == "__main__":
  row, col = list(map(int, input("Enter rows, cols: ").split()))[:2]
  mat = []
  for i in range(row):
    l = list(
        map(int, input("Enter row " + str(i) + " elements: ").split()))[:col]
    mat.append(l)
  print_matrix(l=mat, row_len=row, col_len=col)
