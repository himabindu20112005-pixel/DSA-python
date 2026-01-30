#leetcode 17: Letter Combinations of a Phone Number
#Difficulty: Medium
from ast import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ('', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        res = []
        path = [''] * len(digits)

        def dfs(pos: int):
            if pos == len(digits):
                res.append(''.join(path))
                return
            letters = phone[int(digits[pos])]
            for ch in letters:
                path[pos] = ch
                dfs(pos + 1)

        dfs(0)
        return res
# Time Complexity: O(3^m * 4^n) where m is the number of digits mapping to 3 letters and n is the number of digits mapping to 4 letters
# Space Complexity: O(m + n) for the recursion stack and path array