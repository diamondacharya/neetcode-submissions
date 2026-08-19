class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        SHIFT = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        output = []
        x, y = 0, 0
        for _ in range(len(matrix) * len(matrix[0])):
            output.append(matrix[x][y])
            matrix[x][y] = 'x'
            next_x = x + SHIFT[direction][0]
            next_y = y + SHIFT[direction][1]
            if next_x not in range(len(matrix)) or next_y not in range(len(matrix[0])) or matrix[next_x][next_y] == 'x': 
                direction = (direction + 1) % 4
                next_x = x + SHIFT[direction][0]
                next_y = y + SHIFT[direction][1]
            x = next_x
            y = next_y
        return output
                
            