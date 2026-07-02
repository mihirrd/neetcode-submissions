from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def exist(self, board: List[List[str]], targetWord: str) -> bool:
        R = len(board)
        C = len(board[0])
        self.root = TrieNode()

        def addWord(word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.word = word

        def search(word):
            node = self.root
            for w in word:
                if w not in node.children:
                    return False
                node = node.children[w]
            return True


        def dfs(i,j,path):
            if i < 0 or i >= R or j < 0 or j >= C:
                return False
            path += board[i][j]
            if path == targetWord:
                return True
            if board[i][j] == "#":
                return False
            temp = board[i][j]
            board[i][j] = "#"
            ans = False
            for p,q in [(-1,0),(1,0),(0,1),(0,-1)]:
                ans = ans or dfs(i+p, j+q, path)
            board[i][j] = temp
            return ans

        res = False
        for i in range(R):
            for j in range(C):
                res = res or dfs(i,j,"")
        
        return res

















