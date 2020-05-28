class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        dct = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j - i in dct:
                    dct[j - i] += [matrix[i][j]]
                else:
                    dct[j - i] = [matrix[i][j]]

        for i in dct:
            if len(set(dct[i])) != 1:
                return False
        return True

s = Solution()
print(s.isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))