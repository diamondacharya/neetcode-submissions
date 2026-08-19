# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # list1=[1,2,4]*
    # list2=[1,3,5*]
    # l = dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 5

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        l = dummy 
        while l1 and l2: 
            if (l1.val < l2.val): 
                l.next = l1
                l = l.next 
                l1 = l1.next 
            else: 
                l.next = l2
                l = l.next
                l2 = l2.next
        if (l1): 
            l.next = l1
        if (l2):
            l.next = l2
        return dummy.next
