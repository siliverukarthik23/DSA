class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=0
        for i in s:
            res+=abs(s.index(i)-t.index(i))
        return res