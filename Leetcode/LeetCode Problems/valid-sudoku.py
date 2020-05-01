class Solution:
    def isValidSudoku(self):
        board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
        seen_set = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    if (str(board[i][j]) + " in row " + str(i)) in seen_set:
                        return False
                    else:
                        seen_set.add(str(board[i][j]) + " in row " + str(i))
                    if (str(board[i][j]) + " in col " + str(j)) in seen_set:
                        return False
                    else:
                        seen_set.add(str(board[i][j]) + " in col " + str(j))
                    if (str(board[i][j]) + " in block " + str(i//3) + " - " + str(j//3)) in seen_set:
                        return False
                    else:
                        seen_set.add(str(board[i][j]) + " in block " + str(i//3) + " - " + str(j//3))
        return True

s=Solution()
print(s.isValidSudoku())