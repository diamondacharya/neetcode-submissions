class Node: 
    def __init__(self, key=0, val=0, next=None, prev=None): 
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # stores key --> node mappings
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node): 
        node.prev.next = node.next 
        node.next.prev = node.prev

    def insertRight(self, node: Node): 
        temp = self.right.prev
        self.right.prev = node
        node.prev = temp 
        temp.next = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insertRight(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: 
            node = Node(key, value)
            self.cache[key] = node
            self.insertRight(node)
        else: 
            node = self.cache[key]
            self.remove(node)
            self.insertRight(node)
            node.val = value
        if len(self.cache) > self.capacity: 
            toRemove = self.left.next
            self.remove(toRemove)
            del self.cache[toRemove.key]


        
