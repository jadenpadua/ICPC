# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        leftMostIndex = float("inf")
        rowCount = 0
        isOne = False
        for i in range(dimensions[0]):
            left = 0
            right = dimensions[1] - 1
            while left < right:
                mid = int(left + right) // 2
                
                if binaryMatrix.get(rowCount,mid) == 1:
                    right = mid
                    
                
                else:
                    left = mid + 1
                    
            currentLeftMostIndex = left
            
            if binaryMatrix.get(rowCount,currentLeftMostIndex) == 1:
                isOne = True
            
            
            leftMostIndex = min(leftMostIndex,currentLeftMostIndex)
            rowCount += 1
        
    
        if isOne == False:
            return -1
    
        
        else:
            return leftMostIndex 
