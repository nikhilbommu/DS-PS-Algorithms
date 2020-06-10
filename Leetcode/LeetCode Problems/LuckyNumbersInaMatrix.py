from typing import List
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if min(matrix[i]) == max(transpose_matrix[j]) == matrix[i][j]:
                    lst.append(matrix[i][j])

        return lst

s = Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))

