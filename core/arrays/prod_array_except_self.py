class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #The approach here would be to multiply nums that come before and after said num
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            #traversering the array in forward direction and multiplying to product
            output[i] *= product
            product *= nums[i]
    
        product = 1
        for i in range(len(nums)-1,-1,-1):
        #traversing the array in backward direction and multiplying to product
            output[i] *= product
            product *= nums[i]
        return output
    # O(n) time and O(n) space
