class Solution:
    def minPathSum(self, grid) -> int:
        res = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        sum1 = 0
        for i in range(len(grid)):
            sum1 += grid[i][0]
            res[i][0] = sum1

        sum2 = 0
        for j in range(len(grid[0])):
            sum2 += grid[0][j]
            res[0][j] = sum2

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                res[i][j] = grid[i][j] + min(res[i - 1][j], res[i][j - 1])

        return res[-1][-1]


s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))