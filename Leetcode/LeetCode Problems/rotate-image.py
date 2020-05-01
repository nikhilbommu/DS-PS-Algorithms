matrix=[[1,2,3],[4,5,6],[7,8,9]]
"""
1 2 3                       1 4 7                           7 4 1
4 5 6     ->(transpose)     2 5 8   ->reverse each row      8 5 2
7 8 9                       3 6 9                           9 6 3
"""
for i in range(len(matrix)):
    for j in range(i,len(matrix)):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
print(matrix)