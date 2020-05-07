class Solution:

    def __init__(self):
        self.lookup = dict()
    def addValuesToDict(self, root, i, parent_value):
        if root is None:
            return
        self.lookup[root.val] = [i, parent_value]  # adding keys and values to dictionary
        self.addValuesToDict(root.left, i + 1, root.val)  # recursive call on left sub-tree
        self.addValuesToDict(root.right, i + 1, root.val)  # recursive call on right sub-tree

    def isCousins(self, root, x: int, y: int) -> bool:
        self.addValuesToDict(root, 0, None)
        print(self.lookup)
        # checking for depth and parent values
        return self.lookup[x][0] == self.lookup[y][0] and self.lookup[x][1] != self.lookup[y][1]
