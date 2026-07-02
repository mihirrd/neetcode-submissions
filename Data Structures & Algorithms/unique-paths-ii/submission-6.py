class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        dp = [[-1]*(C+1) for _ in range(R+1)]
        def backtrack(i,j):            
            if i < 0 or i >= R:
                return 0
            if j < 0 or j >= C:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if obstacleGrid[i][j] in {-1,1}:
                return 0
            if i == R-1 and j == C-1: return 1

            
            obstacleGrid[i][j] = -1
            dp[i][j] = backtrack(i+1,j) + backtrack(i,j+1)
            obstacleGrid[i][j] = 0
            return dp[i][j]
        return backtrack(0,0)