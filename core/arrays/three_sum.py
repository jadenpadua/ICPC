class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        triplets = []
        #we are comparing 3 indeces, so we don't need to traverse the whole array
        for i in range(len(nums)-2):
            #left pointer will increment with i
            left = i + 1
            right = len(nums) - 1
            while left < right:
                #currentSum is the sum of three triplests ast all target locations
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
        return triplets
