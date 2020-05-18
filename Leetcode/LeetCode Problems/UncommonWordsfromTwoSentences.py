from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) :
        A, B = A.split(" "), B.split(" ")
        result = []
        A = A + B
        dct = Counter(A)
        for word in dct:
            if dct[word] == 1:
                result.append(word)

        return result

s = Solution()
print(s.uncommonFromSentences("this is a apple","this is a sour"))