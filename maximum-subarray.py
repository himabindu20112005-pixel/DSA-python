#leetcode 53: Maximum Subarray
#Difficulty: Easy
from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxi=nums[0]
        for num in nums:
            currsum+=num
            maxi=max(currsum,maxi)
            currsum=max(currsum,0)
        return maxi
#Time Complexity: O(n) where n is length of nums
#Space Complexity: O(1)