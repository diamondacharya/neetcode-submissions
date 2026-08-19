# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def helper(lists, l, r): 
            if l == r: 
                return lists[l]
            mid = l + (r - l) // 2
            left = helper(lists, l, mid)
            right = helper(lists, mid + 1, r)
            dummy = ListNode()
            t = dummy 
            while left and right: 
                if left.val < right.val: 
                    t.next = left
                    left = left.next
                else: 
                    t.next = right
                    right = right.next
                t = t.next
            if left: 
                t.next = left
            if right: 
                t.next = right
            return dummy.next
        if not lists: 
            return None
        return helper(lists, 0, len(lists) - 1)