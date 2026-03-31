#leetcode 202 Happy Number
#Difficulty: Easy
class Solution:
    def isHappy(self,n):
        seen = set()
        while n not in seen:
            seen.add(n)
            total = 0
            for c in str(n):
                total += int(c) * int(c)
            if total == 1:
                return True
            n = total
        return False
# Time Complexity: O(log n) where n is the input number, since the number of digits decreases with each iteration
# Space Complexity: O(log n) for the seen set, in the worst case where all