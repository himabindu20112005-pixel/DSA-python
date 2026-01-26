#leetcode 119: Pascal's Triangle II
#Difficulty: Easy
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = [1]  # First element is always 1

        for i in range(1, rowIndex + 1):
            

        # We build the row in reverse to avoid overwriting values needed for computation
            for j in range(len(result) - 1, 0, -1):

                result[j] = result[j] + result[j - 1]
            result.append(1)  # Last element is always 1

        return result

        
        
        # Time complexity: O(n^2)
        # Space complexity: O(n)