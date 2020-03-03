class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        # finding smallest index
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
