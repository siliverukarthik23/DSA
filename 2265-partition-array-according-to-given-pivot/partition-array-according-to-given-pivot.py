class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n1=[]
        n2=[]
        n3=[]
        for i in nums:
            if i<pivot:
                n1.append(i)
            elif i>pivot:
                n3.append(i)
            else:
                n2.append(i)
        return n1+n2+n3