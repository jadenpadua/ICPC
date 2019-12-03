class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        numberCount = 0
        hash_set = dict()
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set[nums[i]] = hash_set.get(nums[i],0) + 1
                
        for i in range(len(hash_set)):
            numberCount += 1
            if i not in hash_set:
                return i
        return numberCount
