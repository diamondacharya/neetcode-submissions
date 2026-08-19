# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def helper(lists, l, r): 
            if (l == r): 
                return lists[l]
            mid = (l + r) // 2
            l1 = helper(lists, l, mid)
            l2 = helper(lists, mid + 1, r)
            dummy = ListNode(0, l1)
            mover = dummy
            while (l1 and l2): 
                if (l1.val < l2.val): 
                    mover.next = l1
                    mover = mover.next
                    l1 = l1.next
                else: 
                    mover.next = l2
                    mover = mover.next
                    l2 = l2.next
            if (l1): 
                mover.next = l1
            if (l2):
                mover.next = l2
            return dummy.next
        if not lists: 
            return None
        return helper(lists, 0, len(lists) - 1)
