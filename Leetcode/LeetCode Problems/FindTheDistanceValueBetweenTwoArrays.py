class Solution:
    def findTheDistanceValue(self, arr1, arr2, d) -> int:
        count=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count+=1
                    break
        return len(arr1)-count

s = Solution()
print(s.findTheDistanceValue([4,5,8],[10,9,1,8],2))