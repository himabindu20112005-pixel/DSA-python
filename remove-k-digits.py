#leetcode 402: Remove K Digits
#Difficulty: Medium
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k still > 0, remove from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Build result and strip leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else "0"
# Time Complexity: O(n) where n is length of num
# Space Complexity: O(n) for the stack