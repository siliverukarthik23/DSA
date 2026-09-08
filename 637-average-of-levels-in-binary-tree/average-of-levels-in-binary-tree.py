# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d=dict()
        def travel(root,h):
            if root:
                if h in d:
                    d[h].append(root.val)
                else:
                    d[h]=[root.val]
                travel(root.left,h+1)
                travel(root.right,h+1)
        travel(root,0)
        l=[]
        for i in d:
            res=sum(d[i])/len(d[i])
            print(res)
            l.append(res)
        return l         