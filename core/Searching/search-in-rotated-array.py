class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums is None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        #finding smallest index
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        
        start = left
        left = 0
        right = len(nums) - 1
        
        if target >= nums[start] and target <= nums[right]:
            left = start
        
        
        else:
            right = start
            
            
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        return - 1
