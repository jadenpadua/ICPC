class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = self.binarySearch(arr,k,x)
        low = closest
        high = closest
        while high - low + 1 < k and low > 0 and high < len(arr) - 1:
            if abs(arr[low-1] - x) <= abs(arr[high+1]-x):
                low -= 1
            else:
                high += 1
                
        while high - low + 1 > k:
            if low > 0:
                low -= 1
            else:
                high += 1
        
        ans = []
        while low <= high:
            ans.append(arr[low])
            low += 1
        return ans
        
      
    def binarySearch(self,arr,k,x):
        left = 0
        right = len(arr) - 1
        minDiff = float("inf")
        closest = -1
        while left <= right:
            mid = (left + right) // 2
            cand = arr[mid]
            if abs(cand - x) < minDiff:
                minDiff = abs(arr[mid]-x)
                closest = mid
            if cand == x:
                return mid
            elif cand < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return closest
            
