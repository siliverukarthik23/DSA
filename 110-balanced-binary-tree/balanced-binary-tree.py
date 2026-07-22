# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=True
        if root is None:
            return True
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        def inorder(root):
            if not root:
                return True
            if abs(height(root.left)-height(root.right))>1:
                return False
            return inorder(root.left) and inorder(root.right)
        return inorder(root)