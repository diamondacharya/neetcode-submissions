class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.wordEnd = False

class Trie: 
    def __init__(self, root): 
        self.root = root

    def addWord(self, word): 
        node = self.root
        for char in word: 
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.wordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        myTrie = Trie(root)
        for word in words: 
            myTrie.addWord(word)
        res = set()
        path = set() # set of visited (row, col) tuples
        def dfs(row, col, node, accum): 
            if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] not in node.children or (row, col) in path): 
                return 
            char = board[row][col]
            path.add((row, col))
            accum += char
            node = node.children[char]
            if node.wordEnd: 
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
