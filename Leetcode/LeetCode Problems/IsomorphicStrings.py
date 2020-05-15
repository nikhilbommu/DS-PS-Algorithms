class Solution:
    def isIsomorphic(self, s, t) :
        sdct, tdct = {}, {}
        flag = 0
        for i, j in enumerate(range(len(s))):
            if s[i] not in sdct and t[j] not in tdct:
                sdct[s[i]] = 1
                tdct[t[j]] = 1
            elif s[i] in sdct and t[j] in tdct:
                if sdct[s[i]] == tdct[t[i]] and list(sdct.values()) == list(tdct.values()):
                    sdct[s[i]] += 1
                    tdct[t[j]] += 1
                else:
                    return False
            else:
                return False
        if list(sdct.values()) == list(tdct.values()):
            return True
        else:
            return False


s = Solution()
print(s.isIsomorphic("aba","baa"))
print(s.isIsomorphic("egg","add"))