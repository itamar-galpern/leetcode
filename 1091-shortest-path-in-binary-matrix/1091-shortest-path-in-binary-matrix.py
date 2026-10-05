class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        directions = [(0,1),(1,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
        level = 1
        queue, visited = deque([(0,0)]), {(0,0)}
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if grid[0][0] == 1:
                    continue
                if (x, y) == (len(grid)-1,len(grid)-1):
                    return level
                for dx, dy in directions:
                    if x + dx >= len(grid) or x+dx < 0:
                        continue
                    if y + dy >= len(grid) or y+dy < 0:
                        continue
                    if (x+dx,y+dy) not in visited and grid[x+dx][y+dy] == 0:
                        queue.append((x+dx,y+dy))
                        visited.add((x+dx,y+dy))
            level += 1
        return -1


        