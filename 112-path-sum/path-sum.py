# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        l=[]
        def check(root,sum):
            if root is None:
                return
            if root.left is None and root.right is None: 
                l.append(sum+root.val)
            if root.right:
                check(root.right,sum+root.val)
            if root.left:
                check(root.left,sum+root.val)
        check(root,0)
        print(l)
        return targetSum in l