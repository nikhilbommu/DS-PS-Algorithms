class Solution:
    def findRestaurant(self, list1, list2):
        d = dict()
        for index, item in enumerate(list1):
            d[item] = index

        mini_index = float('inf')
        mini_index_value = []

        for index, item in enumerate(list2):
            if item in d and index + d[item] < mini_index:
                mini_index = index + d[item]
                mini_index_value.clear()
                mini_index_value.append(item)
            elif item in d and index + d[item] == mini_index:
                mini_index_value.append(item)
        return mini_index_value

s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))