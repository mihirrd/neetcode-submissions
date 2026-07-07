from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0]) 
        queue = deque()
        visited = set()
        def dfs(i,j):
            if i < 0 or i>= R or j < 0 or j>= C:
                return
            if grid[i][j] == 1:
                grid[i][j] = 0
                queue.append(((i,j),-1))
                for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                    dfs(i+x,j+y)
        
        found = False
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found: break
        
        min_dist = float("inf")
        while queue:
            (x,y),dist = queue.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if grid[x][y] == 1:
                min_dist = min(min_dist, dist)            
            for p,q in [(-1,0),(1,0),(0,1),(0,-1)]:
                if 0 <= x + p < R and 0 <= y + q < C:
                    queue.append(((x+p,y+q),dist+1))
        
        return min_dist
        
            