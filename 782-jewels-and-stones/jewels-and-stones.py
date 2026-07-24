class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c2=Counter(stones)
        c1=Counter(jewels)
        s=0
        for i,j in c2.items():
            if i in c1:
                s+=j
        return s
