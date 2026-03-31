# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#leetcode 141: Linked List Cycle
#Difficulty: Easy
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

# Time Complexity: O(n) where n is the number of nodes in the linked list, since we may visit each node at most once
# Space Complexity: O(n) in the worst case if there is no cycle and we store
