#leetcode 11: Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Width of container
            width = right - left

            # Choose the smaller height
            if height[left] < height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1

            # Update maximum area found
            if area > max_area:
                max_area = area

        return max_area
# Time Complexity: O(n) where n is the number of elements in height
# Space Complexity: O(1)
