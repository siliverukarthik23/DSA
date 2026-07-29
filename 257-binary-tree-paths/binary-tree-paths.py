# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def check(root,s):
            if root:
                if s is None:
                    s=str(root.val)
                else:
                    s+='->'+str(root.val)
                check(root.left,s)
                check(root.right,s)
                if root.left is None and root.right is None:
                    l.append(s)
        check(root,None)
        return l