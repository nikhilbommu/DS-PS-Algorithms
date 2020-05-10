class Solution:
    def decompressRLElist(self, nums):
        lst = []
        for i in range(0,len(nums),2):
            temp = [nums[i+1]]*nums[i]
            lst += temp
        return lst

s = Solution()
print(s.decompressRLElist([1,2,3,4]))