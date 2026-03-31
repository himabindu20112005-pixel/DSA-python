#leetcode 143: Reorder List
#Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        first = head
        second = prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        if first:
            first.next = None
        return head
# Time Complexity: O(n) where n is the number of nodes in the linked list, since we traverse the list a few times (to find the middle, reverse the second half, and merge the two halves)
# Space Complexity: O(1) since we are rearranging the nodes in place without using
