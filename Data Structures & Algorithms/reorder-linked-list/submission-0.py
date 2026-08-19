# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        second = slow.next # pointer to the second portion
        slow.next = None # set end of first portion to null
        # reverse the second portion
        prev = None
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev # prev will point to the beginning of reversed 2nd portion
        first = head
        # now merge in that alternate way
        while second: # second portion will be equal to or shorter than first
            temp1 = first.next 
            temp2 = second.next
            first.next = second
            second.next = temp1 
            first = temp1
            second = temp2 