# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# lists = [[1, 2,], [2, 3]]
# helper(lists, 0, 1) = 34
    # helper(lists, 3, 1)
        # helper()
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def helper(lists, l, r): #sort this section of the list and return the head
            if (l == r): 
                return lists[l]
            mid = l + (r - l)//2
            l1 = helper(lists, l, mid)
            l2 = helper(lists, mid + 1, r)
            # merge the two sorted portions
            dummy = ListNode() 
            tail = dummy
            while l1 and l2: 
                if l1.val < l2.val: 
                    tail.next = l1
                    l1 = l1.next
                else: 
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2: 
                tail.next = l2
            return dummy.next
        if not lists or len(lists) == 0: 
            return None
        return helper(lists, 0, len(lists) - 1) # need to return the pointer to the head of the linked list 