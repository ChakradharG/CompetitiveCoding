class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        board = [['.' for i in range(n)] for j in range(n)]
        cols = set()
        priDiag = set()
        secDiag = set()

        def addQ(x, y):
            if y in cols or \
               (x - y) in priDiag or \
               (x + y) in secDiag:
                return False
            cols.add(y)
            priDiag.add(x - y)
            secDiag.add(x + y)
            board[x][y] = 'Q'
            return True

        def remQ(x, y):
            cols.remove(y)
            priDiag.remove(x - y)
            secDiag.remove(x + y)
            board[x][y] = '.'

        def backtrack(row):
            if row == len(board):
                boards.append([''.join(row) for row in board])
                return
            for j in range(n):
                if addQ(row, j):
                    backtrack(row+1)
                    remQ(row, j)

        backtrack(0)
        return boards
