class Solution(object):
    def addBinary(self, a, b):
        
        # Convert the binary strings to integers
        int_a = int(a, 2)
        int_b = int(b, 2)

        # Perform the binary addition
        sum_ab = int_a + int_b

        # Convert the sum back to binary representation
        result = bin(sum_ab)[2:]

        return result
