# leetcode 231: Power of Two
# Difficulty: Easy
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


# Time Complexity: O(1) since we are performing a constant number of operations
# Space Complexity: O(1) since we are using a constant amount of space