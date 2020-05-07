class Solution:
    def countLargestGroup(self, n):
        dct = {}
        for i in range(1,n+1):
            i = str(i)
            temp = 0
            for j in i:
                temp += int(j)
            if temp in dct:
                dct[temp] += 1
            else:
                dct[temp] = 1
        lst = list(dct.values())
        maxi = max(lst)
        return lst.count(maxi)

s = Solution()
print(s.countLargestGroup(13))