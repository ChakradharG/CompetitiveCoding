class Solution:
    def totalNQueens(self, n: int) -> int:
        def addQ(x, y):
            if y in cols or \
            (x - y) in priDiag or \
            (x + y) in secDiag:
                return False
            cols.add(y)
            priDiag.add(x - y)
            secDiag.add(x + y)
            return True

        def remQ(x, y):
            cols.remove(y)
            priDiag.remove(x - y)
            secDiag.remove(x + y)

        def backtrack(row):
            nonlocal cnt
            if row == n:
                cnt += 1
                return

            for j in range(n):
                if addQ(row, j):
                    backtrack(row + 1)
                    remQ(row, j)

        cnt = 0
        cols, priDiag, secDiag = set(), set(), set()
        backtrack(0)
        return cnt
