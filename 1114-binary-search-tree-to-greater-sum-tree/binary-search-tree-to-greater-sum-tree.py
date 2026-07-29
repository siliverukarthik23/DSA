# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d={}
        def travel(root):
            if root:
                d[root.val]=root.val
                travel(root.left)
                travel(root.right)
        def update(root):
            if root:
                for i in d:
                    if root.val>i:
                        d[i]+=root.val
                update(root.left)
                update(root.right)
        def final(root):
            if root:
                root.val=d[root.val]
                final(root.left)
                final(root.right)
        travel(root)
        update(root)
        final(root)
        return root