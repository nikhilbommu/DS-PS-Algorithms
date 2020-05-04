class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = 0
        count = 0
        if len(strs) == 0:
            return ""
        mini = min(len(i) for i in strs)
        while i < mini:
            val = 0
            for j in range(len(strs)):
                temp = strs[0][i]
                if temp == strs[j][i]:
                    val += 1
            if val == len(strs):
                count += 1
            else:
                break
            i += 1
        print(count)
        return strs[0][:count]

s = Solution()
print(s.longestCommonPrefix(["abc","cba"]))