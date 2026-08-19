# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # [1, 2, 3, 4]
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n + 1): 
            fast = fast.next
        while fast: 
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        

