class Solution:
    def spiralOrder(matrix):
        k = 0
        l = 0
        if len(matrix) == 0:
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        temp = []
        while (k < rows and l < cols):
            for i in range(l, cols):
                temp.append(matrix[k][i])
            k += 1
            for i in range(k, rows):
                temp.append(matrix[i][cols - 1])
            cols -= 1
            if (k < rows):
                for i in range(cols - 1, (l - 1), -1):
                    temp.append(matrix[rows - 1][i])
                rows -= 1
            if (l < cols):
                for i in range(rows - 1, k - 1, -1):
                    temp.append(matrix[i][l])
                l += 1
        return temp

obj = Solution
print(obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))