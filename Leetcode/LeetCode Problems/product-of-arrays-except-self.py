class Solution:
    def productExceptSelf(nums):
        left=[0]*len(nums)
        right=[0]*len(nums)
        left[0]=1
        right[-1]=1
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        print(left)
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1]*right[i+1]
        print(right)
        final=[]
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        return final
    print(productExceptSelf([1,2,3,4]))