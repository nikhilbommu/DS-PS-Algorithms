class Solution:
    def commonChars(self, A):
        res = []
        if not A:
            return []
        check = set(A[0])
        for ch in check:
            n = []
            for word in A:
                n.append(word.count(ch))
            mini = min(n)

            res += [ch] * mini

        return res

s = Solution()
print(s.commonChars(["bella","label","roller"]))