"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapp = {} # maps old node to copy 
        curr = head
        while curr: 
            copy = Node(curr.val)
            mapp[curr] = copy
            curr = curr.next
        curr = head
        while curr: 
            copy = mapp[curr]
            copy.next = mapp.get(curr.next, None)
            copy.random = mapp.get(curr.random, None)
            curr = curr.next
        return mapp.get(head, None)
        