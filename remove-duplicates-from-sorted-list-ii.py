#leetcode 82: Remove Duplicates from Sorted List II
#Difficulty: Medium
# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head)  
        prev = dummy               
        while head:
           
            if head.next and head.val == head.next.val:
               
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  
            else:
                prev = prev.next  
            head = head.next      
        
        return dummy.next
# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(1) since we are modifying the list in place