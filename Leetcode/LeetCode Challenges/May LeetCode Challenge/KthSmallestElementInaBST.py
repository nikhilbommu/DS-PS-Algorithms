# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.resultList = []

    def inOrderTraversal(self, root):
        if not root:
            return self.resultList

        if root.left != None:
            self.inOrderTraversal(root.left)

        self.resultList.append(root.val)

        if root.right != None:
            self.inOrderTraversal(root.right)

        return self.resultList

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inOrderTraversal(root)
        return self.resultList[k - 1]