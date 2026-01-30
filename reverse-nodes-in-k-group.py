#leetcode 25: Reverse Nodes in k-Group
#Difficulty: Hard
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
        if not head or k == 1:
            return head

        # Create a dummy node to simplify handling the head of the new list
        # and connecting reversed groups.
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev_group_tail' points to the last node of the previously reversed group (or dummy initially)
        prev_group_tail = dummy

        while True:
            # 1. Check if there are enough nodes for a full group of 'k'
            k_head = prev_group_tail.next # This is the potential head of the current k-group
            k_tail = k_head
            for _ in range(k - 1): # Move k_tail 'k-1' steps to reach the end of the k-group
                if not k_tail: # Not enough nodes for a full group
                    return dummy.next
                k_tail = k_tail.next
            
            # If after moving k-1 steps, k_tail is None, it means the remaining nodes are < k
            if not k_tail:
                return dummy.next

            # 'next_group_head' is the node immediately after the current k-group
            next_group_head = k_tail.next

            # 2. Reverse the current k-group
            # Disconnect the k-group from the rest of the list temporarily to reverse it
            k_tail.next = None 
            
            # Perform standard linked list reversal on the k-group
            # The result is new_k_head (original k_tail) and new_k_tail (original k_head)
            new_k_head, new_k_tail = self._reverse_list(k_head)

            # 3. Connect the reversed group back to the main list
            # The node before the group should now point to the new head of the reversed group
            prev_group_tail.next = new_k_head
            
            # The new tail of the reversed group (original k_head) should point to the
            # head of the next unprocessed group
            new_k_tail.next = next_group_head

            # 4. Update 'prev_group_tail' for the next iteration
            # It should now point to the original head of the just-reversed group (which is now its tail)
            prev_group_tail = new_k_tail

    # Helper function to reverse a linked list
    def _reverse_list(self, head: ListNode) -> tuple[ListNode, ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # 'prev' is the new head (original tail), 'head' is the new tail (original head)
        return prev, head
# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(1) since we are reversing the list in place