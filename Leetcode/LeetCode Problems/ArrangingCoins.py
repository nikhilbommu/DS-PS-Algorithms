class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 1
        count = 0
        while n>0:
            n -= step
            step += 1
            count += 1
        if n>=0:
            return count
        return count - 1

s = Solution()
print(s.arrangeCoins(10))