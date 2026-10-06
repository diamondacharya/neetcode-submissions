class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites: 
            adjList[course].append(prereq)
        res = []
        visited = set()
        path = set()
        # returns true if there is a cycle
        def dfs(i): 
            if i in path: 
                return True
            if i in visited: 
                return False
            visited.add(i)
            path.add(i)
            for neighbor in adjList[i]: 
                if dfs(neighbor): 
                    return True
            res.append(i)
            path.remove(i)
        for i in range(numCourses): 
            if i not in visited and dfs(i): 
                return []
        return res