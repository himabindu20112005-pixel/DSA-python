# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        # Create a dummy node that points to the head of the list.
        # This simplifies handling the head of the new list and edge cases.
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' pointer keeps track of the node before the pair being swapped.
        prev = dummy

        # Iterate as long as there are at least two nodes to swap
        # (i.e., 'prev.next' is the first node of the pair, and 'prev.next.next' is the second)
        while prev.next and prev.next.next:
            # node1 is the first node of the pair
            node1 = prev.next
            # node2 is the second node of the pair
            node2 = prev.next.next

            # Perform the swap:
            # 1. 'prev' should now point to 'node2' (the new first node of the pair)
            prev.next = node2
            # 2. 'node1' (the original first node) should point to whatever 'node2' was pointing to
            node1.next = node2.next
            # 3. 'node2' (the original second node) should now point to 'node1'
            node2.next = node1

            # Move 'prev' pointer forward by two steps to the new 'node1',
            # which is now the last node of the swapped pair.
            # This sets up for the next pair.
            prev = node1
            
        return dummy.next

        