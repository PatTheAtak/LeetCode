class Solution:
    def findNumbers(self, nums: list) -> int:
        count = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
        
        