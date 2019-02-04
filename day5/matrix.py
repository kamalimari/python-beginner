

matrix1_ = [[0]*3]*3
matrix1_[1][2] = "*"
print(matrix1_)
matrix1 = [
    [1,2,3,4],
    [4,5,6,5],
    [7,8,9,8]]
matrix1[1][2] = "*"
print(matrix1)

column = [];
for row in matrix1:
    column.append(row[2])
print(column)





