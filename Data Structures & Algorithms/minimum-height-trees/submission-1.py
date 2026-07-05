from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def height(node):
            h = 0
            q = deque([(node, 1)])
            while q:
                node,h = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nei in adj[node]:
                    q.append((nei, h+1))
            return h

        min_height = float('inf')
        res = []
        for i in range(n):
            visited = set()
            h = height(i)
            if h < min_height:
                res = [i]
                min_height = h
            elif h == min_height:
                res.append(i)
        return res
    
            
            


