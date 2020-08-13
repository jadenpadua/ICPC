class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        maxArea = float("-inf")
        
        while left < right:
            minHeight = min(height[left],height[right]) 
            maxArea = max(maxArea, minHeight * (right - left))
            
            if height[right] > height[left]:
                left += 1
            
            else:
                right -= 1
            
        return maxArea
