from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        R = len(grid)
        C = len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] == 0:
                return

            grid[i][j] = 0
            q.append([(i,j),0])
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i+x, j+y)
        
        found = False
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break

        visited = set()
        min_dist = float("inf")
        while q:
            point, dist = q.popleft()
            if point in visited:
                continue
            visited.add(point)
            i,j = point
            if grid[i][j] == 1:
                min_dist = min(min_dist, dist-1)
            
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= i+x < R and 0 <= j+y < C:
                    q.append([(i+x,j+y),dist+1])
        
        return min_dist




