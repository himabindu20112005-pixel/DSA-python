#leetcode 70: Climbing Stairs
#Difficulty: Easy
class Solution:
    def climbStairs(self, n: int) -> int:#space optimization technique in dp
        if n<=2:
            return n
        a=1
        b=2
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b


#Time Complexity: O(n) where n is the number of stairs
#Space Complexity: O(1)
   