class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert int to str
        x = str(x)
        return x == x[::-1]
        