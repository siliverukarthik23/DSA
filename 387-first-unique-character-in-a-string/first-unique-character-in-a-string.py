class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=Counter(s)
        l=[i for i,j in d.items() if j==1]
        if len(l)==0:
            return -1
        m=float('inf')
        for i in l:
            m=min(m,s.index(i))
        print(l)
        return m
