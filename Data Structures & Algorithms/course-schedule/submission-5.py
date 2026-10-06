class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites: 
            adjList[course].append(prereq)
        visited = set()
        path = set()
        # returns true if there is a cycle present 
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
            path.remove(i)
            return False
        for i in range(numCourses): 
            if i not in visited and dfs(i): 
                return False
        return True


        
        
        