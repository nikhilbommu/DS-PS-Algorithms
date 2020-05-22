import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        dct = {}
        paragraph = paragraph.lower()

        for each in string.punctuation:
            paragraph = paragraph.replace(each,' ')

        list_paragraph = paragraph.split()
        for word in list_paragraph:
            if word not in banned:
                if word not in dct:
                    dct[word] = 1
                else:
                    dct[word] += 1

        return max(dct,key=dct.get)

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit." , ["hit"]))