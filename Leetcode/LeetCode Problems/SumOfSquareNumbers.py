import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(math.sqrt(c))
        left = 0
        right = sqrt_c
        while left <= right:
            res = left * left + right * right
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False

s = Solution()
print(s.judgeSquareSum(5))