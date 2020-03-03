class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        # loop breaks when left is at smallest idx
        start = left
        # reset boundaries after finding smallest elem
        left = 0
        right = len(nums) - 1
        
        #now given smallest elem, choosing where to start,
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
            
        # Now after adjusted correct boundaries to search for, simple binary search
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
