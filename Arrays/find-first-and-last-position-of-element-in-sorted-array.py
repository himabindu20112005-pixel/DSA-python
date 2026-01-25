#leetcode 34: Find First and Last Position of Element in Sorted Array
#Difficulty: Medium
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(x):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        left = findIndex(target)
        right = findIndex(target + 1) - 1

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]

        
