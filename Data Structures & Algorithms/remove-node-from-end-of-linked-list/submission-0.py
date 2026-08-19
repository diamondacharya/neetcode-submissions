# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        back = front = dummy
        # front will need to be (n + 1) steps ahead
        i = 0
        while i < n + 1: 
            front = front.next
            i += 1
        while front: 
            back = back.next
            front = front.next
        back.next = back.next.next
        return dummy.next
        
        
