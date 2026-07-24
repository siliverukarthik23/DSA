class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        while n>0:
            r=n%10
            if r not in d:
                d[r]=1
            else:
                d[r]+=1
            n//=10
        s=0
        for i,j in d.items():
            s+=(i*j)
        return s