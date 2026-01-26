#leetcode 121: Best Time to Buy and Sell Stock
#Difficulty: Easy
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('inf')
        maxp=0
        for p in prices:
            mp=min(mp,p)
            maxp=max(maxp,p-mp)
        return maxp
#Time Complexity: O(n) where n is number of prices
#Space Complexity: O(1)