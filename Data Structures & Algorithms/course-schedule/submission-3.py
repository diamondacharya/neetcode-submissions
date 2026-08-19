class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for i in range(numCourses)] # maps courses to prereqs
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)
        path = set()
        # returns true if there is a cycle 
        def dfs(course):
            if adjlist[course] == []:
                return False
            if course in path:
                return True
            path.add(course)
            for prereq in adjlist[course]:
                if dfs(prereq):
                    path.remove(course)
                    return True
            path.remove(course)
            return False
        for course in range(numCourses):
            if dfs(course): # return False if there is a cycle
                return False
        return True 