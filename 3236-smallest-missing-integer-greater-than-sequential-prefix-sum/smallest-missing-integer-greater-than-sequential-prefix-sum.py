class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prev=nums[0]
        s=prev
        if len(nums)==1:
            return prev+1
        i=1
        while i<len(nums):
            if nums[i]==prev+1:
                s+=nums[i]
                prev+=1
                i+=1
            else:
                break
        while True:
            if s not in nums:
                return s
            else:
                s+=1
