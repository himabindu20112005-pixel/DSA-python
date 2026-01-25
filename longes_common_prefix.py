#leetcode 14: Longest Common Prefix
#Difficulty: Easys
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate over characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare with every string
            for s in strs[1:]:
                # Check if index out of range or char mismatch
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
