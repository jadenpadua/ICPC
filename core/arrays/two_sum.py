class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = dict()
        for i in range(len(nums)):
            potentialMatch = target - nums[i]
            if nums[i] in ht:
                output = [ht[nums[i]], i]
                return output
            else:
                ht[potentialMatch] = i
    
        return []
