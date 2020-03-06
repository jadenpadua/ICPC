class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = float("inf")
        i = 0
        j = len(height) - 1
        #While pointers do not overlap
        while i < j:
            #take minimum between two heights
            minimum = min(height[i], height[j])
            #Comparfe that minimum and its distance with the current Max
            maximum = max(maximum, minimum * (j-i))
            #Need to make the heights meet 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        # Max is found once they have met in middle
        return maximum
    
    # O(n) one pass solution | O(1) space
