# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 0
        right = n
        firstBadVersion = -1
        while left < right:
            mid = int(left + right) // 2
            if isBadVersion(mid) == True:
                right = mid
                firstBadVersion = mid
            
            else:
                left = mid + 1
                firstBadVersion = left
        
        return firstBadVersion
        """
        :type n: int
        :rtype: int
        """
        
