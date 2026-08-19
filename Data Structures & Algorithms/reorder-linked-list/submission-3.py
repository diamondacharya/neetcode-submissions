# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3, 4, 5, 6]
# 3/4 split --> [0, 1, 2], [6, 5, 4, 3] --> merged to get [0, 6, 1, 5, 2, 4, ]
# 4/3 split! 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        slow, fast, first = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev
        while second: 
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1 
            second = temp2 
        

        