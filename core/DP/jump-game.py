class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndexPosition = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= lastGoodIndexPosition:
                lastGoodIndexPosition = i
                
        return lastGoodIndexPosition == 0
        
