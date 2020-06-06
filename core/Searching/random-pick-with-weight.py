class Solution:

    def __init__(self, w: List[int]):
        self.buckets = [0] * len(w)
        running_sum = 0
        for i in range(len(w)):
            running_sum += w[i]
            self.buckets[i] = running_sum
        self.totalWeight = running_sum

    def binarySearch(self,num):
        left = 0
        right = len(self.buckets)
        while left < right:
            mid = (left + right) // 2
            if num == self.buckets[mid]:
                return mid
            elif num > self.buckets[mid]:
                left = mid + 1
            else:
                right = mid
        return left
                
        
    
    def pickIndex(self) -> int:
        num = random.randint(1, self.totalWeight)
        idx = self.binarySearch(num)
        return idx
