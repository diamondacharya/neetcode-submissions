class CountSquares:

    def __init__(self):
        self.pointCountMap = defaultdict(int) # (x, y) --> count       

    def add(self, point: List[int]) -> None:
        self.pointCountMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in list(self.pointCountMap.keys()):  
            if x == px and y == py: # diagonal can't be same point
                continue
            if not (abs(px - x) == abs(py - y)): # not a potential diagonal
                continue
            res += (self.pointCountMap[(px, y)] * self.pointCountMap[(x, py)] * self.pointCountMap[(x, y)])
        return res
            
