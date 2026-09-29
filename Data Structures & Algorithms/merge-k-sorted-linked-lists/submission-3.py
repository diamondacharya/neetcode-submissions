# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergesort(l, r): 
            if l == r: 
                return lists[l]
            mid = l + (r - l) // 2
            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)
            dummy = ListNode()
            mover = dummy 
            while left and right: 
                if left.val <= right.val: 
                    mover.next = left 
                    mover = mover.next
                    left = left.next
                else: 
                    mover.next = right
                    mover = mover.next
                    right = right.next
            if left: 
                mover.next = left 
            if right: 
                mover.next = right
            return dummy.next
        if not lists: 
            return None
        return mergesort(0, len(lists) - 1)