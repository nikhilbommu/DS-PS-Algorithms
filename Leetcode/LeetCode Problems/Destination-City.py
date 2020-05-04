class Solution:
    def destCity(self, paths) :
        if len(paths) == 1:
            return paths[0][-1]
        source, destination = [], []
        for i in paths:
            source.append(i[0])
            destination.append(i[1])
        for i in destination:
            if i not in source:
                return i

s = Solution()
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))