class Node: 
    def __init__(self): 
        self.children = {}
        self.word = False

class Trie: 
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word): 
        node = self.root
        for char in word: 
            if char not in node.children: 
                node.children[char] = Node()
            node = node.children[char]
        node.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        root = trie.root
        res = set()
        path = set()
        for word in words: 
            trie.addWord(word)
        def dfs(row, col, node, accum): 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in path or board[row][col] not in node.children: 
                return
            char = board[row][col]
            accum += char
            path.add((row, col))
            node = node.children[char]
            if node.word: 
                res.add(accum)
            dfs(row + 1, col, node, accum)
            dfs(row - 1, col, node, accum)
            dfs(row, col + 1, node, accum)
            dfs(row, col - 1, node, accum)
            path.remove((row, col))
        for row in range(len(board)): 
            for col in range(len(board[0])):
                dfs(row, col, root, "") 
        return list(res)