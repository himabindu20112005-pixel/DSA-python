# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#leetcode 86: Partition List
#Difficulty: Medium
class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next
# Time Complexity: O(n) where n is the number of nodes in the linked list, since we traverse the list once
# Space Complexity: O(1) since we are rearranging the nodes in place without using