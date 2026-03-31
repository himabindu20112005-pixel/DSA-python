# leetcode 326: Power of Three
# Difficulty: Easy
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

# Time Complexity: O(log n) where n is the input number, since we divide the number by 3 in each iteration
# Space Complexity: O(1) since we are using a constant amount of space
