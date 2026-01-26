#leetcode 39: Combination Sum
#Difficulty: Medium
from ast import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[] for _ in range(target+1)]
        dp[0]=[[]]
        for num in candidates:
            for i in range(num,target+1):
                for combination in dp[i-num]:
                    newcomb=combination+[num]
                    dp[i].append(newcomb)
        return dp[target]
#Time Complexity: O(n*m) where n is target and m is number of candidates
#Space Complexity: O(n*m)