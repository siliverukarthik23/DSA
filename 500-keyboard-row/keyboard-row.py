class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1='qwertyuiop'
        r2='asdfghjkl'
        r3='zxcvbnm'
        d={}
        for i in r1:
            d[i]=1
        for i in r2:
            d[i]=2
        for i in r3:
            d[i]=3
        l=[]
        for word in words:
            flag=True
            temp=word.lower()
            m=d[temp[0]]
            for i in temp:
                if m!=d[i]:
                    flag=False
            if flag:
                l.append(word)
        return l