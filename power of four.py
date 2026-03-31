# leetcode 342: Power of Four
# Difficulty: Easy
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
# Time Complexity: O(log n) where n is the input number, since we divide the number by 4 in each iteration
# Space Complexity: O(1) since we are using a constant amount of space