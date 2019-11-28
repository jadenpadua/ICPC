class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0.5
        ht = dict()
        for i in range(len(nums)):
            ht[nums[i]] = ht.get(nums[i],0) + 1
        
        for key,value in ht.items():
            if value / len(nums) > majority:
                return key
        
        
