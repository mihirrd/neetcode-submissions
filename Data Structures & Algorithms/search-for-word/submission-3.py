from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def exist(self, board: List[List[str]], targetWord: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(i,j,k):
            if k == len(targetWord): return True
            if i < 0 or i >= R or j < 0 or j >= C:
                return False
            if board[i][j] != targetWord[k]:
                return False
            if board[i][j] == "#":
                return False
            temp = board[i][j]
            board[i][j] = "#"
            ans = False
            for p,q in [(-1,0),(1,0),(0,1),(0,-1)]:
                ans = ans or dfs(i+p, j+q, k+1)
            board[i][j] = temp
            return ans

        res = False
        for i in range(R):
            for j in range(C):
                res = res or dfs(i,j,0)
        
        return res

















