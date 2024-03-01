class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i, j):
            slc = set()
            for j2 in range(9):
                if board[i][j2] in slc:
                    return False
                if board[i][j2] != '.':
                    slc.add(board[i][j2])
            slc.clear()
            for i2 in range(9):
                if board[i2][j] in slc:
                    return False
                if board[i2][j] != '.':
                    slc.add(board[i2][j])
            slc.clear()
            i3, j3 = 3 * (i//3), 3 * (j//3)
            for i2 in range(i3, i3 + 3):
                for j2 in range(j3, j3 + 3):
                    if board[i2][j2] in slc:
                        return False
                    if board[i2][j2] != '.':
                        slc.add(board[i2][j2])
            return True

        def dfs(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            for x in range(1, 10):
                board[i][j] = str(x)
                if isValid(i, j) and dfs(idx+1):
                    return True
                else:
                    board[i][j] = '.'

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))

        dfs(0)
