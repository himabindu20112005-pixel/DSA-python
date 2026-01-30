#leetcode 19: Remove Nth Node From End of List
#Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, fast and slow
        fast = dummy
        slow = dummy

        # Move the fast pointer 'n' steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end of the list
        # When fast reaches the end, slow will be at the node before the one to be removed
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the nth node from the end
        slow.next = slow.next.next

        return dummy.next
# Time Complexity: O(L) where L is the length of the linked list
# Space Complexity: O(1)