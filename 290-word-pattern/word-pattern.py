class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        s=s.split()
        if len(s)!=len(pattern):
            return False
        for i,j in zip(pattern,s):
            if i not in d1:
                d1[i]=j
            if j not in d2:
                d2[j]=i
            if d1[i]!=j or d2[j]!=i:
                return False
        return True