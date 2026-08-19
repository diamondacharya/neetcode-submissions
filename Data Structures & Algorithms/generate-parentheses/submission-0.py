class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        def backtrack(openCount, closedCount): 
            if openCount == closedCount == n: 
                res.append("".join(path))
            if openCount < n: 
                path.append('(')
                backtrack(openCount + 1, closedCount)
                path.pop()
            if closedCount < openCount: 
                path.append(')')
                backtrack(openCount, closedCount + 1)
                path.pop()
        backtrack(0, 0)
        return res
