class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        SHIFT = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0 # tracks right, down, left, and up (0,1,2,3 respectively)
        x, y = 0, 0
        m = len(matrix)
        n = len(matrix[0])
        spiral = []
        for _ in range(m * n): 
            spiral.append(matrix[x][y]) 
            matrix[x][y] = 'x' # mark as visited 
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
            if next_x not in range(m) or next_y not in range(n) or matrix[next_x][next_y] == 'x': 
                direction = (direction + 1) % 4
                next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
            x = next_x
            y = next_y
        return spiral



