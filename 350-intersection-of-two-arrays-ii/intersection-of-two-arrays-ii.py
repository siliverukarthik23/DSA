class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1)
        c2=Counter(nums2)
        nums1=set(nums1)
        nums2=set(nums2)
        res=list(nums1.intersection(nums2))
        l=[]
        for i in res:
            l.extend([i]*min(c1[i],c2[i]))
        return l