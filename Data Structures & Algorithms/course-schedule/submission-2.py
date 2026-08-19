# path = (0, 1)
# ---------------cyclePresent(0)-----------------
    # ---------------cyclePresent(1)-----------------
        # ---------------cyclePresent(0)-----------------

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for a, b in prerequisites: 
            adjList[a].append(b)
        path = set()
        def cyclePresent(i): 
            if i in path: 
                return True
            path.add(i)
            for neighbor in adjList[i]: 
                if cyclePresent(neighbor): 
                    return True
            path.remove(i)
        for i in range(numCourses): 
            if cyclePresent(i): 
                return False
        return True
        