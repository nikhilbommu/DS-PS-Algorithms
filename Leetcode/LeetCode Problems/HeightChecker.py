class Solution:
    def heightChecker(self, heights) -> int:
        count = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count

s = Solution()
print(s.heightChecker([1,3,2,4,5]))