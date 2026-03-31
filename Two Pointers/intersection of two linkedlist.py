# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#leetcode 160: Intersection of Two Linked Lists
#Difficulty: Easy
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists
# Space Complexity: O(1) since we are using only two pointers and no additional data
