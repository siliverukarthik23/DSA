# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0
        def travel(root):
            if root is None:
                return 0,0
            leftsum,leftcount=travel(root.left)
            rightsum,rightcount=travel(root.right)

            totalsum=leftsum+rightsum+root.val
            totalcount=leftcount+rightcount+1
            if totalsum//totalcount ==root.val:
                self.ans+=1
            return totalsum,totalcount
        travel(root)
        return self.ans
