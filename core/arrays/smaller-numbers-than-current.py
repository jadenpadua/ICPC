class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            newArr = nums[:i] + nums[i+1:]
            for j in range(len(newArr)):
                if newArr[j] < nums[i]:
                    res[i] += 1
        return res
