class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIdx] = nums[i]
                lastNonZeroIdx += 1
        
        for i in range(lastNonZeroIdx,len(nums)):
            nums[i] = 0
        
        return nums
