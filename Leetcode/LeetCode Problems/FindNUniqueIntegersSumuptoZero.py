class Solution:
    def sumZero(self, n):
        if n % 2 != 0:
            temp=-n//2
            for i in range(n):
                temp += 1
                yield temp
        else:
            temp=-n//2-1
            for i in range(n+1):
                temp += 1
                if temp != 0:
                    yield temp

s = Solution()
print(s.sumZero(4))