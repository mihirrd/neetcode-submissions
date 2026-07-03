class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["."]*n for _ in range(n)]
        pos = set()
        neg = set()
        col = set()
        def backtrack(r):
            if r == n:
                sol = ["".join(board[i]) for i in range(len(board))]
                self.res.append(sol)
            
            for c in range(n):
                if (r-c) not in pos and (r+c) not in neg and c not in col:
                    board[r][c] = "Q"
                    pos.add(r-c)
                    neg.add(r+c)
                    col.add(c)
                    backtrack(r+1)

                    board[r][c] = "."
                    pos.remove(r-c)
                    neg.remove(r+c)
                    col.remove(c)

        backtrack(0)
        return self.res
