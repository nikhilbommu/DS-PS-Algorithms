class Solution:
    def toGoatLatin(self, S: str) -> str:
        result = []
        S = S.split()
        for i in range(len(S)):
            if S[i][0] in "aeiouAEIOU":
                result.append(S[i]+"ma"+("a"*(i+1)))
            else:
                result.append(S[i][1:]+S[i][0]+"ma"+("a"*(i+1)))
        return ' '.join(result)

s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))