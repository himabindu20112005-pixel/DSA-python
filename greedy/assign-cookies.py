#leetcode 455: Assign Cookies
#Difficulty: Easy
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        #c=0
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1 
                #j+=1
            #else:  # child satisfied
            j += 1       # move to next cookie

        return i # c
# Time Complexity: O(n log n + m log m) where n and m are lengths of g and s respectively
# Space Complexity: O(1)
