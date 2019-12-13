class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    # Loops through array and places next new number it sees at the index
    # Then we incrememnt the index to reflect the new new number
    # Then we return the index position for new len of arr
    # in this case we are "removing" by reassigng new value
    
        index = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
        return index
