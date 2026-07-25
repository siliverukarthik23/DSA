class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        s=sum(nums)
        target=s%k
        return target