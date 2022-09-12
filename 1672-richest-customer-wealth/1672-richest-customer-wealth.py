class Solution:
    def maximumWealth(self, accounts):
        return max([sum(arr) for arr in accounts])