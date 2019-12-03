class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_ht = dict()
        intersections = []
        for i in range(len(nums1)):
            n1_ht[nums1[i]] = n1_ht.get(nums1[i],0) + 1
        
        for i in range(len(nums2)):
            if nums2[i] in n1_ht and n1_ht.get(nums2[i],0) > 0:
                intersections.append(nums2[i])
                n1_ht[nums2[i]] -= 1
        return intersections
