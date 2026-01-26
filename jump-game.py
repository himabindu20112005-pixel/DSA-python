#leetcode 55: Jump Game
#Difficulty: Medium
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True
#Time Complexity: O(n) where n is length of nums
#Space Complexity: O(1)