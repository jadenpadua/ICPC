class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ht = dict()
        output = []
        for i in range(len(nums)):
            ht[nums[i]] = ht.get(nums[i],0) + 1
            
            
        for i in range(1,len(nums)+1):
            if i not in ht:
                output.append(i)
        
        return output
