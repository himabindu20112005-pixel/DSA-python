#leetcode 22: Generate Parentheses
#Difficulty: Medium
from ast import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        # Backtracking function
        # current_string: The current combination of parentheses being built
        # open_count: Number of opening parentheses currently used
        # close_count: Number of closing parentheses currently used
        def backtrack(current_string, open_count, close_count):
            # Base Case: If the current string has reached the total length of 2*n
            if len(current_string) == 2 * n:
                ans.append(current_string)
                return

            # Rule 1: Add an opening parenthesis if we haven't used all 'n' of them
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # Rule 2: Add a closing parenthesis if it balances a previously added opening one
            # (i.e., we have more open parentheses than closed ones)
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Start the backtracking process
        backtrack("", 0, 0)
        return ans
#Time Complexity: O(4^n / sqrt(n)) - Catalan number growth
#Space Complexity: O(4^n / sqrt(n)) - for storing the result