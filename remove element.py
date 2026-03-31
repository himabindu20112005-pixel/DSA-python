#leetcode 27: Remove Element
#Difficulty: Easy
from ast import List



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
# Time Complexity: O(n) where n is the length of the input array, since we traverse the array once
# Space Complexity: O(1) since we are modifying the array in place without using extra