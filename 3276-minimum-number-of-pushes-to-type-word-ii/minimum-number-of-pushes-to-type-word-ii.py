class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
        c = list(sorted(c.items(), key=lambda x: x[1], reverse=True))
        print(c)
        i=0
        j=0
        res=0
        while i<len(c):
            if i%8==0:
                j+=1
            res+=c[i][1]*j
            i+=1
        return res
