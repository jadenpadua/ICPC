class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        runningSum = 0
        result = 0
        ht = {0:1}
        
        for i in range(len(nums)):
            runningSum += nums[i]
            currentSum = runningSum - k
            
            if currentSum in ht:
                result += ht[currentSum]
                
            if runningSum in ht:
                ht[runningSum] += 1
                
            else:
                ht[runningSum] = 1
                
        return result
