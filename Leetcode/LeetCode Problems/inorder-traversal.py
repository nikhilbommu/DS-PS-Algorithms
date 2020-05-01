# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(root) -> List[int]:
        """
        #recursive method
        l=[]
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)

        inorder(root)
        return l

"""
        #iterative method
        out = []
        stack = []
        top = root
        while top or len(stack):
            while top:
                stack.append(top)
                top = top.left
            top = stack.pop()
            out.append(top.val)
            top = top.right
        return out

