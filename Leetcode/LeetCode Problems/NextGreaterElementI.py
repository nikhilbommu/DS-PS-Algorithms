class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        res = []
        for i in nums1:
            temp = nums2.index(i)
            flag = 0
            while temp < len(nums2):
                if nums2[temp] > i:
                    res.append(nums2[temp])
                    flag = 1
                    break
                temp += 1
            if flag == 0 and temp == len(nums2):
                res.append(-1)
        return res

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))
