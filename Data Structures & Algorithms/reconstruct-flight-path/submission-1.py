class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {src: [] for src, dest in tickets}
        tickets.sort()
        for src, dest in tickets: 
            adjList[src].append(dest)
        res = ['JFK']
        def dfs(src): 
            if len(res) == len(tickets) + 1: 
                return True
            if src not in adjList: # got stuck early -- need to take different route
                return False
            for i, neighbor in enumerate(adjList[src]): 
                adjList[src].pop(i)
                res.append(neighbor)
                if dfs(neighbor): 
                    return True
                adjList[src].insert(i, neighbor)
                res.pop()
            return False
        dfs('JFK')
        return res