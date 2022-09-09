class Solution:
    def sortedSquares(self, nums: list) -> list:
        
        for index in range(len(nums)):
            
            nums[index] = nums[index] ** 2
            
        nums.sort()
        return nums