#leetcode 21: Merge Two Sorted Lists
#Difficulty: Easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Definition for singly-linked list.

        # This helps in avoiding special handling for the head of the new list.
        dummy = ListNode()
        current = dummy # This 'current' pointer will build our merged list

        # Iterate while both lists have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # Move current pointer forward

        # If one of the lists is not fully traversed, append the rest of it
        # directly to the merged list, as it's already sorted.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The merged list starts from dummy.next
        return dummy.next
# Time Complexity: O(m + n) where m and n are the lengths of list1 and list2 respectively
# Space Complexity: O(1) since we are reusing the existing nodes and not creating
