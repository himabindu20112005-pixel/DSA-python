#leetcode 88 Merge Sorted Array
#Difficulty: Easy
class Solution:
    def merge(self, nums1, m, nums2, n):
       
        i = m - 1   
        j = n - 1   
        k = m + n - 1        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1
# Time Complexity: O(m + n) where m and n are the lengths of nums1 and nums2 respectively
# Space Complexity: O(1) since we are merging in place without using extra space
