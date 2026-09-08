# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total=[0]
        def dfs(root):
            if not root:
                return 0
            leftsum=dfs(root.left)
            rightsum=dfs(root.right)

            total[0]+=abs(leftsum-rightsum)

            return root.val+leftsum+rightsum
        dfs(root)
        return total[0]