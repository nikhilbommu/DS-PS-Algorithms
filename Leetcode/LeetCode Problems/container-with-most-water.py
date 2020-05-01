class Solution:
    def maxArea(height) -> int:
        length = len(height) - 1
        start, end = 0, len(height) - 1
        result = 0
        while start < end:
            if height[start] < height[end]:
                temp = height[start] * length
                start += 1
            else:
                temp = height[end] * length
                end -= 1
            length -= 1
            result = max(result, temp)
        return result
s = Solution
print(s.maxArea([1,8,6,2,5,4,8,3,7]))