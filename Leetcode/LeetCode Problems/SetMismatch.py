class Solution:
    def findErrorNums(self, nums):
        length = (len(nums)*(len(nums)+1))//2
        result = []
        remaining = []
        for i in range(len(nums)):
            if nums[i] in result:
                remaining.append(nums[i])
            else:
                result.append(nums[i])
        remaining.append(length-sum(result))
        return remaining

s = Solution()
print(s.findErrorNums([1,2,2,4]))