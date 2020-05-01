class Solution:
    def findDuplicate(nums):
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1]==0:
                return nums[i]


    print(findDuplicate([1,2,3,4,2]))