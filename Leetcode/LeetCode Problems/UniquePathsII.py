class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        bool_row = False
        for i in range(n):
            if obstacleGrid[0][i] != 1 and bool_row == False:
                res[0][i] = 1
            else:
                bool_row = True

        bool_col = False
        for j in range(m):
            if obstacleGrid[j][0] != 1 and bool_col == False:
                res[j][0] = 1
            else:
                bool_col = True

        print(res)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        print(res)
        return res[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0],[0,0,0],[0,1,0],[0,0,0]]))


