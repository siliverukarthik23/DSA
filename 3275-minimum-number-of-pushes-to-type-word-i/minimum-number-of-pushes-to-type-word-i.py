class Solution:
    def minimumPushes(self, word: str) -> int:
        s=len(word)
        i=1
        res=0
        while s>8:
            res+=8*i
            s=s-8
            i+=1
        res+=i*s
        return res