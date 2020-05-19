class Solution:
    def longestWord(self, words) -> str:
        words = sorted(words)
        setwords, res = set(), ""
        setwords.add("")
        for word in words:
            if word[:-1] in setwords:
                if len(word) > len(res):
                    res = word
                setwords.add(word)

        return res

s = Solution()
print(s.longestWord(["w","wo","wor","worl", "world"]))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))