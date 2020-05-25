class Solution:
    def maximumProduct(self, nums) -> int:
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])

s = Solution()
print(s.maximumProduct([1,0,100]))
print(s.maximumProduct([-20,-5,4,3,5]))