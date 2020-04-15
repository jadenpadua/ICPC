class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= product
            product *= nums[i]
            
        product = 1
        for i in reversed(range(len(nums))):
            output[i] *= product
            product *= nums[i]
            
        return output
