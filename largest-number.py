#leetcode 179: Largest Number
#Difficulty: Medium
class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(reverse=True, key=lambda x: x*10)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result

# Time Complexity: O(n log n) where n is the number of elements in nums
# Space Complexity: O(n) for the string conversion and sorting