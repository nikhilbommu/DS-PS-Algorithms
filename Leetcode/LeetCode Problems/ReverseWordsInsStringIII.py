class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split(" ")
        for i in range(len(lis)):
            lis[i] = lis[i][::-1]

        res = ""
        for i in lis:
            res += i + " "

        return res[:-1]

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))