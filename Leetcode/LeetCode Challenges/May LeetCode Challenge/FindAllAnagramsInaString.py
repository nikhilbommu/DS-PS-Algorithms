class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        result = []
        if len(s)<20100 and len(p)<20100:
            for i in range(len(s)-len(p)+1):
                temp = sorted(s[i:i+len(p)])
                if temp == p:
                    result.append(i)
            return result

s = Solution()
print(s.findAnagrams("cbaebabacd","abc"))