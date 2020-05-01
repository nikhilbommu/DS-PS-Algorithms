class Solution:
    def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_seen, cols_seen = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_seen.add(i)
                    cols_seen.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i not in rows_seen and j not in cols_seen:
                    matrix[i][j] = matrix[i][j]
                else:
                    matrix[i][j] = 0
        return matrix
s=Solution
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
