# leetcode 50: Pow(x, n)
# Difficulty: Medium
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        
        while n > 0:
            # If n is odd, multiply result by current x
            if n % 2 == 1:
                result *= x
            
            # Square the base
            x *= x
            
            # Divide n by 2
            n //= 2
        
        return result
# Time Complexity: O(log n) where n is the exponent, since we are halving n in each iteration
# Space Complexity: O(1) since we are using a constant amount of space