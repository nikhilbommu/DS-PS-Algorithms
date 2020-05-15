class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        sdct,tdct = {},{}
        flag = 0
        str1 = str1.split(" ")
        if len(pattern) != len(str1):
            return False
        for i, j in enumerate(range(len(pattern))):
            if pattern[i] not in sdct and str1[j] not in tdct:
                sdct[pattern[i]] = 1
                tdct[str1[j]] = 1
            elif pattern[i] in sdct and str1[j] in tdct:
                if sdct[pattern[i]] == tdct[str1[i]] and list(sdct.values()) == list(tdct.values()):
                    sdct[pattern[i]] += 1
                    tdct[str1[j]] += 1
                else:
                    return False
            else:
                return False
        if list(sdct.values()) == list(tdct.values()):
            return True
        else:
            return False

s = Solution()
print(s.wordPattern("abba","cat dog dog cat"))