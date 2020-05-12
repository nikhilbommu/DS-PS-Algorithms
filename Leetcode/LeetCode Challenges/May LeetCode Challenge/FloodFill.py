class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def DFSsearch(row, col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row >= 1: DFSsearch(row-1, col)
                if row+1 < rows: DFSsearch(row+1, col)
                if col >= 1: DFSsearch(row, col-1)
                if col+1 < cols: DFSsearch(row, col+1)

        DFSsearch(sr, sc)
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,  1, 2))