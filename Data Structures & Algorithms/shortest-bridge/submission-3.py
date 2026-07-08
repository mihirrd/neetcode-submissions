from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        R = len(grid)
        C = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] != 1:
                return

            grid[i][j] = -1
            q.append((i,j,0))
            for dr,dc in dirs:
                dfs(i+dr, j+dc)
        
        found = False
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break

        while q:
            r,c, dist = q.popleft()                        
            for dr,dc in dirs:
                nr,nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == 1:
                        return dist
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        q.append((nr,nc,dist+1))
    
        return -1