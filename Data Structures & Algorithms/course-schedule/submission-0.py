class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i: [] for i in range(numCourses)} # maps courses to prereqs
        for course, prereq in prerequisites: 
            adjlist[course].append(prereq)
        path = set()
        def dfs(course): 
            if adjlist[course] == []: 
                return True
            if course in path: 
                return False
            path.add(course)
            for prereq in adjlist[course]: 
                if not dfs(prereq): 
                    return False
            path.remove(course)
            return True
        for course in range(numCourses): 
            if not dfs(course): 
                return False
        return True
