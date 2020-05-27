class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        first_lst = []
        second_lst = []
        result = []
        text = text.split()
        for i in range(len(text) - 1):
            if text[i] == first and text[i + 1] == second:
                first_lst.append(i)
                second_lst.append(i + 1)

        for i in range(len(first_lst)):
            if second_lst[i] - first_lst[i] == 1 and second_lst[i] + 1 != len(text):
                result.append(text[second_lst[i] + 1])

        return result

s = Solution()
print(s.findOcurrences("alice is a good girl she is a good student","a","good"))