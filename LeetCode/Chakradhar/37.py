class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            for x in '123456789':
                if x in rows[i] and x in cols[j] and x in subs[3*(i//3) + (j//3)]:
                    board[i][j] = x
                    rows[i].remove(x)
                    cols[j].remove(x)
                    subs[3*(i//3) + (j//3)].remove(x)

                    if dfs(idx+1):
                        return True

                    board[i][j] = '.'
                    rows[i].add(x)
                    cols[j].add(x)
                    subs[3*(i//3) + (j//3)].add(x)

            return False

        rows = [set('123456789') for _ in range(9)]
        cols = [set('123456789') for _ in range(9)]
        subs = [set('123456789') for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    subs[3*(i//3) + (j//3)].remove(board[i][j])

        dfs(0)
