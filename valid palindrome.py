# 125. Valid Palindrome
# Difficulty: Easy
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


# Time Complexity: O(n) where n is the length of the input string, since we traverse the string once to filter and convert it, and then compare it with its reverse
# Space Complexity: O(n) for the filtered string, in the worst case where all characters