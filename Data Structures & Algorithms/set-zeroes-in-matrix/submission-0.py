class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for x,y in zeros:
            matrix[x] = [0]*len(matrix[x])
            for i in range(len(matrix)):
                matrix[i][y] = 0

        