class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        for i in candies:
            if i + extraCandies >= maxi:
                yield True
            else:
                yield False

s = Solution()
print(s.kidsWithCandies([2,3,4,1,5],3))