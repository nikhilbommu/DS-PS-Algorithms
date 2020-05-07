from collections import Counter
class Solution:
    def findLucky(self, arr) :
        c = Counter(arr)
        set_arr = sorted(list(set(arr)),reverse=True)
        for i in set_arr:
            if c[i] == i:
                return i
        return -1

s = Solution()
print(s.findLucky([3,2,2,4]))