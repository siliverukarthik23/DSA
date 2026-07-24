class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=0
        for i in words:
            if set(i).issubset(set(allowed)):
                s+=1
        return s