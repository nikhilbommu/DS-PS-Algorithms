class Solution:
    def oddCells(self, n, m, indices )-> int:
        mat = [[0 for i in range(m)] for j in range(n)]
        for r,c in indices:
            for i in range(m):
                mat[r][i] ^= 1
            for j in range(n):
                mat[j][c] ^= 1
        print(mat)
        return sum([mat[i][j] % 2 for i in range(n) for j in range(m)])

s = Solution()
print(s.oddCells(2,3,[[0,1],[1,1]]))