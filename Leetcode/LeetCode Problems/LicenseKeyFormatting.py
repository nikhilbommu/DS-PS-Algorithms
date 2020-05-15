class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        temp = K
        S = list(S)
        end = len(S) - 1
        while end >= 0:
            if S[end].isalnum():
                if S[end].islower():
                    S[end] = S[end].upper()
                res.insert(0, S[end])
                K -= 1
            if K == 0 and end != 0:
                res.insert(0, '-')
                K = temp
            end -= 1
        res = ''.join(res)
        return res.lstrip('-')

s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w",4))