class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        n1=[i for i in nums if i>=0]
        n2=[i for i in nums if i<0]
        n1.sort(reverse=True)
        n2.sort()
        s1=float('-inf')
        s2=float('-inf')
        if len(n2)==0:
            return n1[0]*n1[1]*n1[2]
        if len(n1)==0:
            return n2[-3]*n2[-1]*n2[-2]
        if len(n2)>=2 and len(n1)>=1:
            s1=n1[0]*n2[0]*n2[1]
        if len(n1)>2:
            s2=n1[0]*n1[1]*n1[2]
        return max(s1,s2)