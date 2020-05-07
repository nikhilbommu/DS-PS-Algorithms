class Solution:
    def stringMatching(self, words):
        wordlst = ' '.join(words)
        for i in words:
            if wordlst.count(i) >= 2:
                yield i
s = Solution()
print(s.stringMatching(["leetcode","et","code"]))