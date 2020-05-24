class Solution:
    def findWords(self, words):
        l1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        l2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        l3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        res = []
        for i in words:
            lower_i = i.lower()
            temp = []
            for j in lower_i:
                if j in l1:
                    temp.append(1)
                elif j in l2:
                    temp.append(2)
                elif j in l3:
                    temp.append(3)
            if len(set(temp)) == 1:
                res.append(i)

        return res

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))