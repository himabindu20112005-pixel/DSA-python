from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If target is impossible to reach
        if abs(target) > total_sum:
            return 0
        
        # (total_sum + target) must be even
        if (total_sum + target) % 2 != 0:
            return 0
        
        subset_sum = (total_sum + target) // 2

        # dp[s] = number of ways to get sum s
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # one way to make sum 0 (choose nothing)

        for num in nums:
            # iterate backwards to avoid reusing the same number
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]
