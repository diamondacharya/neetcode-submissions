# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # helper to get kth node after 
    def getKth(self, node, k): 
        while node and k > 0: 
            node = node.next
            k -= 1
        return node
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True: 
            kth = self.getKth(groupPrev, k)
            if not kth: 
                break
            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next #prev=gNext(curr first node should point to gnext after being reversed)
            while curr != groupNext: 
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth # kth is now the first node in the group (after reversing)
            groupPrev = temp
        return dummy.next

        
