class Solution:
    def isSubsequence(self, s, t ):
        s_start,t_start = 0,0
        while t_start < len(t) and s_start < len(s):
            if t[t_start] == s[s_start]:
                t_start += 1
                s_start += 1
            else:
                t_start += 1
        if len(s) == s_start :
            return True
        return False

s = Solution()
print(s.isSubsequence("abc","ahbcdf"))
print(s.isSubsequence("axc","ahbcdf"))