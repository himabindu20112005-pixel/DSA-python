#leetcode 300: Longest Increasing Subsequence
#Difficulty: Medium
import bisect


class Solution:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

#Time Complexity: O(n log n) where n is the length of nums
#Space Complexity: O(n)
