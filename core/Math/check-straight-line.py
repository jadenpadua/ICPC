class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = coordinates
        if len(n) <= 2:
            return True
        
        if n[1][0] - n[0][0] == 0:
            return False

        runningSlope = (n[1][1] - n[0][1]) / (n[1][0] - n[0][0])
        for i in range(len(n)-1):
            pt1 = n[i]
            pt2 = n[i+1]
            if pt2[0] - pt1[0] == 0:
                return False
            currentSlope = self.compareSlopes(pt1,pt2)
            if currentSlope != runningSlope:
                return False
            else:
                runningSlope = currentSlope
        return True
    
    def compareSlopes(self,pt1,pt2):
        slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
        return slope
