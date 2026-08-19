class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites: 
            adjList[course].append(prereq)
        output = []
        path = set()
        visited = set()
        # returns true if a cycle is present 
        def dfs(course): 
            if course in path: 
                return True
            if course in visited: 
                return False
            path.add(course)
            for prereq in adjList[course]: 
                if dfs(prereq) == True: 
                    return True
            path.remove(course)
            visited.add(course)
            output.append(course)
            return False
        for course in range(numCourses): 
            if dfs(course) == True: 
                return []
        return output
        