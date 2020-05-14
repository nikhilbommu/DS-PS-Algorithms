class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxi = -1
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            maxi = max(count, maxi)

        return maxi

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))