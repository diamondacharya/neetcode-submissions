class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        print('wordList is ', wordList)
        adjList = collections.defaultdict(set)
        for i in range(len(wordList)): 
            for j in range(len(wordList)): 
                word1 = wordList[i]
                word2 = wordList[j]
                differCount = 0
                for k in range(len(word1)): 
                    if word1[k] != word2[k]: 
                        differCount += 1
                if differCount == 1: 
                    adjList[word1].add(word2)
                    adjList[word2].add(word1)
        print(adjList)
        q = deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        dist = 1
        while q: 
            for _ in range(len(q)): 
                word = q.popleft()
                if word == endWord: 
                    return dist
                for neighbor in adjList[word]: 
                    if neighbor not in visited: 
                        q.append(neighbor)
                        visited.add(neighbor)
            dist += 1
        return 0