class Solution:
    def groupAnagrams(strs):
        dict1 = {}
        result = []
        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in dict1:
                dict1[sorted_item] = [item]
            else:
                dict1[sorted_item].append(item)

        for key in dict1:
            result.append(dict1[key])

        return result
s= Solution
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))