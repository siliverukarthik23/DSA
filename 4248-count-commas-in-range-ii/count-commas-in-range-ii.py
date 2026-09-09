class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        i=3
        while i<=15:
            if n>=10**i:
                ans+=n-((10**i)-1)
            i+=3
        return(ans)