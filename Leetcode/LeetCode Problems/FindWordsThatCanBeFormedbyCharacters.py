from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            if all(collections.Counter(word)[ch] <= collections.Counter(chars)[ch] for ch in word):
                result += len(word)
        return result

s = Solution()
print(s.countCharacters(["cat","bt","hat","tree"],"atach"))