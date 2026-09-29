# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # gets the kth node after node node 
    def getkth(self, node, k): 
        i = 0
        while node and i < k: 
            node = node.next
            i += 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True: 
            kth = self.getkth(groupPrev, k)
            if not kth: 
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next
            i = 0
            while i < k: 
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp 
                i += 1
            temp = groupPrev.next  
            groupPrev.next = kth 
            groupPrev = temp
        return dummy.next
            


