class Solution:
    def countSquares(self, matrix) -> int:
        result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            result[i][0] = matrix[i][0]

        for i in range(len(matrix[0])):
            result[0][i] = matrix[0][i]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1], result[i - 1][j - 1])

        sum1 = 0
        for each in result:
            sum1 += sum(each)

        return sum1

s = Solution()
print(s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))