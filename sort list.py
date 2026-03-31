#leetcode 148: Sort List
#Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp:
            lst.append(temp.val)
            temp=temp=temp.next
        lst.sort()
        temp=head
        for i in lst:
            temp.val=i
            temp=temp.next

        return head    
# Time Complexity: O(n log n) where n is the number of nodes in the linked list, since we sort the list of values
# Space Complexity: O(n) since we store the values of the nodes in a list before