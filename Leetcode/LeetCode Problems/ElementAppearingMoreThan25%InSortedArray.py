class Solution:
    def findSpecialInteger(self, arr):
        if len(arr) == 1:
            return 1
        maxi = 0
        ele = 0
        count = 1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                count += 1
            else:
                count = 1
            if count > maxi :
                maxi = count
                ele = arr[i]
        return ele

s = Solution()
print(s.findSpecialInteger([1,2,2,3,3,3,6,6,6,6,6]))