# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        h=[0]
        def check(root):
            if root:
                if root.left  and root.left.left is None and root.left.right is None:
                    h[0]+=root.left.val
                check(root.left)
                check(root.right)
        check(root)
        return h[0]