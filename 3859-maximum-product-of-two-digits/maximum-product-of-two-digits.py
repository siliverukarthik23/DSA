class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while n>0:
            r=n%10
            l.append(r)
            n//=10
        l.sort(reverse=True)
        return l[0]*l[1]