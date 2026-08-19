class Node: 
    def __init__(self, key = 0, val = 0, prev = None, next = None): 
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    # helper func to remove (disconnect) a node from the linked list
    def remove(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev

    # helper func to insert node to the right so it becomes most recently used
    def insertRight(self, node): 
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
            self.insertRight(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insertRight(newNode)
        self.cache[key] = newNode
        if (len(self.cache)) > self.capacity: 
            nodeToEvict = self.left.next
            self.remove(nodeToEvict)
            del self.cache[nodeToEvict.key] 

