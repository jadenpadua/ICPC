class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht = dict()
        for i in range(len(nums)):
            ht[nums[i]] = ht.get(nums[i],0) + 1
        
        for key,value in ht.items():
            if value == 1:
                return key
