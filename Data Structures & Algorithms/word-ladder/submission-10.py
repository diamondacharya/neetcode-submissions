class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjList = {word: [] for word in wordList}
        for wordone in wordList: 
            for wordtwo in wordList: 
                difflen = 0
                for i in range(len(wordone)): 
                    if wordone[i] != wordtwo[i]: 
                        difflen += 1
                if difflen == 1: 
                    adjList[wordone].append(wordtwo)
                    adjList[wordtwo].append(wordone)
        q = collections.deque()
        q.append(beginWord)
        visited = set()
        dist = 1
        while q: 
            for _ in range(len(q)): 
                popped = q.popleft()
                if popped == endWord: 
                    return dist
                for neighbor in adjList[popped]: 
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            dist += 1
        return 0



