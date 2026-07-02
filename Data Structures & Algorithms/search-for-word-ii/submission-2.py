from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.idx = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])
        self.root = TrieNode()
        for i,word in enumerate(words):
            node = self.root
            for w in word:
                node = node.children[w]
            node.idx = i
        self.res = []
        def dfs(i,j,node):
            if i < 0 or i >= R or j < 0 or j >= C:
                return False
            if board[i][j] not in node.children:
                return False
            c = board[i][j]
            node = node.children[c]
            if node.idx != -1:
                self.res.append(words[node.idx])
                node.idx = -1
            board[i][j] = "#"
            for p,q in [(-1,0),(1,0),(0,1),(0,-1)]:
                dfs(i+p, j+q, node)
            board[i][j] = c
        
        for i in range(R):
            for j in range(C):
                node = self.root
                dfs(i,j,node)
        
        return self.res



