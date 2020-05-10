class Solution:
    def replaceElements(self, arr):
        lst = [0] * len(arr)
        lst[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            maxi = max(lst[i + 1], arr[i + 1])
            lst[i] = maxi
        return lst

s = Solution()
print(s.replaceElements([17,18,5,4,6,1]))