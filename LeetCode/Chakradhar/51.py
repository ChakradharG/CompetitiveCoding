class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        board = [[0 for i in range(n)] for j in range(n)]

        def addQ(x, y):
            if board[x][y] != 0:
                return False
            for i in range(n):
                for j in range(n):
                    if i == x or \
                       j == y or \
                       (i - j) == (x - y) or \
                       (i + j) == (x + y):
                       board[i][j] += 1
            board[x][y] = -1
            return True

        def remQ(x, y):
            for i in range(n):
                for j in range(n):
                    if i == x or \
                       j == y or \
                       (i - j) == (x - y) or \
                       (i + j) == (x + y):
                       board[i][j] -= 1
            board[x][y] = 0

        def replace(row):
            res = ''
            for sq in row:
                if sq < 0:
                    res += 'Q'
                else:
                    res += '.'
            return res

        def backtrack(nRem, row):
            if row == len(board):
                if nRem == 0:
                    boards.append(list(map(replace, board)))
                return
            for j in range(n):
                if addQ(row, j):
                    backtrack(nRem-1, row+1)
                    remQ(row, j)

        backtrack(n, 0)
        return boards
