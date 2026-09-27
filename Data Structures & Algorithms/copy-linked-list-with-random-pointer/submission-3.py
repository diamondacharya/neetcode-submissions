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
        d = {}
        dummy = Node(0, head)
        while head: 
            if head not in d: 
                d[head] = Node(head.val)
            head = head.next 
        head = dummy.next 
        while head: 
            copy = d[head]
            copy.next = d.get(head.next, None)
            copy.random = d.get(head.random, None)
            head = head.next
        return d.get(dummy.next, None)
        
            