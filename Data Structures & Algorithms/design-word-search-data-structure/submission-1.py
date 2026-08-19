class Node: 
    def __init__(self): 
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word: 
            if char not in node.children: 
                node.children[char] = Node()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):  
            for j in range(i, len(word)): 
                char = word[j]
                if char == '.': 
                    for child in node.children.values(): 
                        if dfs(j + 1, child): 
                            return True
                    return False
                else: 
                    if char not in node.children: 
                        return False
                    node = node.children[char]
            return node.word
        return dfs(0, self.root)
