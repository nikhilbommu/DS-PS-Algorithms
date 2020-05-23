class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B and len(A) == len(set(A)):
            return False
        elif A == B[::-1]:
            return True
        else:
            i = 0
            A, B = list(A), list(B)
            while i < len(A):
                if A[i] == B[i]:
                    del A[i]
                    del B[i]
                    i -= 1
                    if len(A) == 0:
                        return True
                i += 1
            if A == B[::-1]:
                return True
            return False

s = Solution()
print(s.buddyStrings("ab","ba"))
print(s.buddyStrings("abcde","abcd"))