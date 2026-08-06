class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            res=1
            temp=i
            while temp>0:
                rem=temp%10
                res*=rem
                temp//=10
            if res%t==0:
                return i

